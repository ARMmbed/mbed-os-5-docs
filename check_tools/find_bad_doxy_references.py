#!/usr/bin/env python

import os
import sys
import re
import requests

PATTERN = (
    "\[!\[View code\]\(https://www\.mbed\.com/embed/\?type=library\)\]"
    "\((.*)\)"
)

def main(path):
    bad = False

    for dir, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.md'):
                continue

            path = os.path.join(dir, file)
            with open(path) as file:
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
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
