#!/usr/bin/env python

import os
import sys
import re
import requests
from subprocess import check_output
from builtins import input, open

PATTERN = (
    "\[!\[View code\]\(https://www\.mbed\.com/embed/\?type=library\)\]"
    "\((.*)\)"
)

def main(path=None):
    bad = False
    interactive = False

    if not path:
        interactive = True

        # Go to root to make paths easier
        root = check_output(['git', 'rev-parse', '--show-toplevel']).strip()
        os.chdir(root)

        # Ask for path in case user is unfamiliar with command line
        path = input('What directory should I check? ')

    for dir, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.md'):
                continue

            path = os.path.join(dir, file)
            with open(path, encoding='utf-8') as file:
                for i, line in enumerate(file):
                    for match in re.findall(PATTERN, line):
                        if match.startswith('https:'):
                            sys.stderr.write("\n%s:%s: Bad URL (https):\n" % (path, i))
                            sys.stderr.write(match + '\n')
                            bad = True

                        try:
                            code = requests.get(match).status_code
                        except requests.exceptions.RequestException:
                            code = -1

                        if code != 200:
                            sys.stderr.write("\n%s:%s: Bad URL (%d):\n" % (path, i, code))
                            sys.stderr.write(match + '\n')
                            bad = True

                        sys.stdout.write('.')
                        sys.stdout.flush()

        for dir in dirs:
            if dir.startswith('.'):
                dirs.remove(dir)

    sys.stdout.write('\nDone!\n')
    if interactive:
        input('Hit any key to continue ')

    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
