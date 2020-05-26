#!/usr/bin/env python
# Copyright (c) 2019-2020 Arm Limited and Contributors. All rights reserved.
#


# Script to automatically update the configuration parameters list in
# each configuration doc page with the output from `mbed compile --config -v`
# for the page's appropriate prefix.
#
# By default, when run from the check_tools directory, the script runs
# through each Markdown file in `docs/reference/configuration/`. An
# optional file or directory path may be passed in a parameter to run the
# script on a specific file or directroy outside the default path.
#
# You need to copy the mbed-os-5-docs repository to a Mbed OS repository
# in order to run the script.
#
# The config markdown files will be updated using the content of the mbed_lib.json
# files found in the Mbed OS repository. Ensure your current working directory is
# mbed-os-5docs/check_tools when running the script as there is a relative path in the script.
# When in the check_tools directory, run `$ python2 config-update` to update all config markdown files.
#
# If you only want to update a single config markdown file run
# `$ python2 config-update.py ../docs/reference/configuration/xxxx.md`
#
# Note: The script does not produce a correct output with Python 3.x

import argparse
import logging
import os
import pathlib
import re
import subprocess
import sys
from enum import Enum


LOG = logging.getLogger(__name__)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


DEFAULT_PATH = os.path.join(
    pathlib.Path(__file__).parent.absolute(),
    "..",
    "docs",
    "reference",
    "configuration"
)

class ReturnCode(Enum):
    """Return codes."""

    SUCCESS = 0
    ERROR = 1
    INVALID_OPTIONS = 2


class ArgumentParserWithDefaultHelp(argparse.ArgumentParser):
    """Subclass that always shows the help message on invalid arguments."""

    def error(self, message):
        """Error handler."""
        sys.stderr.write(f"error: {message}\n")
        self.print_help()
        raise SystemExit(ReturnCode.INVALID_OPTIONS.value)


def set_log_verbosity(increase_verbosity):
    """Set the verbosity of the log output."""
    log_level = logging.DEBUG if increase_verbosity else logging.INFO

    LOG.setLevel(log_level)
    logging.basicConfig(level=log_level, format=LOG_FORMAT)


def split_into_pairs(l):
    """ Split the provided list into a, b pairs.
        [1, 2, 3, 4] -> [[1, 2], [3, 4]]
    Args:
    l - list of values to be split

    Returns:
    List of split pairs
    """
    for i in range(0, len(l), 2):
        yield l[i:i + 2]


def is_string(line):
    """ Determine if the provided string contains
        alphabetical characters (case insensitive)
    Args:
    line - string to scan

    Returns:
    Match object if the string contains [a-z], else None
    """
    regexp = re.compile(r'[a-z]', re.IGNORECASE)
    return regexp.search(line)


def generate_config_content(file):
    """..."""
    LOG.debug(f"_____ {file} _____")
    file_h = open(file, "r+")
    file   = file_h.read()

    # Collect indices of markdown code block ticks, split into start,end pairs
    # with `split_into_pairs` below. Collect the config parameter prefix used in
    # the current block if viable and replace the contents with the output of
    # the Mbed CLI config verbose list command.
    snippet_indices = [m.start() for m in re.finditer("```", file)]

    blocks = {}
    for i in range(0, int(len(snippet_indices) / 2)):
        snippet_indices = [m.start() for m in re.finditer("```", file)] # Need to rerun on every loop as the indices change each iteration

        ranges = list(split_into_pairs(snippet_indices))
        start = ranges[i][0]
        end = ranges[i][1]

        try:
            blocks[i] = file[start : end + 3]
            if "Name: " in blocks[i]:
                lib = blocks[i].split("Name: ")[1].split(".")[0]
                print(f"=================   {lib}   =================")
                cmd = ["mbed", "compile", "-m", "DISCO_L475VG_IOT01A", "--config", "-v", "--prefix", lib]
                LOG.debug(cmd)
                configuration_output = subprocess.check_output(cmd).decode()

                # Some APIs break config options into logical blocks in their config files.
                # If a tag is applied to a parameter block, only display parameter names that contain that tag
                # For example:
                #   ```heap
                #   mbed-mesh-api.heap-size
                #       ...
                #   mbed-mesh-api.heap-stat-info
                #       ..
                #   ......
                #   ```
                #
                # On encountering a block with a tag, collect the common parameter token,
                # and split the configuration list output into its components.
                # Collect tag (if present), split <TAG> from ```<TAG> at current index
                # Check with regex for string to cover for potential trailing whitespaces
                tag = file[start : file.find("\n", start)].split("`")[-1]
                if is_string(tag):
                    print(f"\t------- Tag: {tag} -------")

                    start_of_config_block = file.find("Name:", start)
                    updated_config = str(file[ : start_of_config_block])
                    for line in configuration_output.splitlines():
                        if "Name" in line and tag in line:
                            updated_config += line

                            # Collect all text until next parameter name. If there's no following 'Name:' token, its the last
                            # config option, match to 'Macros' instead to termiante the block. Offset starting index to avoid finding
                            # the current line's 'Name:' token.
                            eol = configuration_output.find("\n", configuration_output.find(line))
                            if configuration_output.find("Name:", configuration_output.find(line) + len("Name:")) > 0:
                                updated_config += configuration_output[eol : configuration_output.find("Name:", configuration_output.find(line) + len("Name:"))]
                            else:
                                updated_config += configuration_output[eol : configuration_output.find("Macros", configuration_output.find(line))]

                    updated_config += str(file[end:])
                else:
                    updated_config = str(file[:start+4] + configuration_output[:configuration_output.index("Macros") - 1] + file[end:])

                file = updated_config

        # Originally added for debugging purposes, catch and display exceptions before
        # continuing without exiting to provide a complete list of errors found
        except Exception as e:
            print("Error")
            print(e)
            print("____________________")
            exc_type, _ , exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    file_h.truncate(0)
    file_h.seek(0)
    file_h.write(file)
    file_h.close()


def config_update(args):
    """..."""
    if os.path.isfile(args.path):
        generate_config_content(args.path)
    else:
        for (root, _, filenames) in os.walk(args.path):
            for filename in filenames:
                if not filename == "configuration.md":
                    generate_config_content(os.path.join(root, filename))


def is_valid_file(parser, arg):
    """Check if the file or directory exists."""
    file = os.path.join(pathlib.Path().absolute(), arg)
    if not os.path.exists(file):
        parser.error(f"'{file}': No such file or directory.")
    else:
        return file


def parse_args():
    """Parse the command line args."""
    parser = ArgumentParserWithDefaultHelp(
        description=(
            "Copy mbed-os-5-docs (or make a symlink) to a mbed-os repository."
            "The script runs from mbed-os-5-docs/check_tools/ and iterates"
            f" through {DEFAULT_PATH}. You may"
            " pass a directory or a file. In case of a directory, the script"
            " will run on all files contained within it. "
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "path",
        type=lambda x: is_valid_file(parser, x),
        nargs="?",
        help="path to file or directory.",
        default=DEFAULT_PATH,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="increase verbosity of status information.",
    )

    parser.set_defaults(func=config_update)

    args_namespace = parser.parse_args()

    # We want to fail gracefully, with a consistent
    # help message, in the no argument case.
    # So here's an obligatory hasattr hack.
    if not hasattr(args_namespace, "func"):
        parser.error("No arguments given!")
    else:
        return args_namespace


def run_config_update():
    """Application main algorithm."""
    args = parse_args()

    set_log_verbosity(args.verbose)

    LOG.debug("Starting script")
    LOG.debug(f"Command line arguments:{args}")

    args.func(args)


def _main():
    """..."""
    try:
        run_config_update()
    except Exception as error:
        print(error)
        return ReturnCode.ERROR.value
    else:
        return ReturnCode.SUCCESS.value


if __name__ == "__main__":
    sys.exit(_main())
