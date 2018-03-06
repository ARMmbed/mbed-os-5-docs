#!/usr/bin/env python

import re
import os
import requests
import urllib
import json
from requests.auth import HTTPBasicAuth
from subprocess import check_output

# NOTE Does not follow docs.json, instead relies heavily on
# remembering successful urls

MBED_BOT_USER  = "mbed-pr-bot"
MBED_BOT_EMAIL = MBED_BOT_USER + "@arm.com"
MBED_BOT_TOKEN = "9038ab8321dbe1581185c1dc0b33572acd215426"
REPO_SLUG = "ARMmbed/Handbook"
REPO_API_URL = "https://api.github.com/repos/" + REPO_SLUG
REPO_PUSH_URL = ("https://" + MBED_BOT_USER + ":" + MBED_BOT_TOKEN +
    "@github.com/" + MBED_BOT_USER + "/" + REPO_SLUG.split('/')[1])

REDIRECT_NEW_TEMPLATE = (
    "<span class=\"warnings\">**Out of date**: "
    "This is not the most recent version of this page. "
    "Please see [the most recent version]({url})</span>\n"
)
REDIRECT_OLD_TEMPLATE = REDIRECT_NEW_TEMPLATE
DOCS_URL_PREFIX  = "https://os.mbed.com/docs/v{version}"
DOCS_PATH_PREFIX = "docs"
DOCS_BRANCH = 'mbed-pr-bot-redirect-{version}'

COMMIT_MESSAGE = "Updated version redirects from {version} to {latest}"
PR_BODY = (
    "This is an automated PR to update outdated doc pages with note pointing "
    "to the most recent version of that page. Feel free to reject or modify "
    "this PR as needed.\n\n"
    "Updated:\n```\n{redirects}\n```\n"
)

def edit(path, latest, seen):
    assert path.endswith('.md')
    url = None
    exists = False

    with open(os.path.join(DOCS_PATH_PREFIX, path), 'r+') as file:
        data = file.read()
        pattern = REDIRECT_NEW_TEMPLATE.split('{url}')
        if data.startswith(pattern[0]):
            begin = len(pattern[0])
            end = data[begin:].find(pattern[1]) + begin
            if end > begin:
                url = data[begin:end]
                exists = True

            try:
                if url:
                    requests.get(url).raise_for_status()
            except requests.exceptions.RequestException:
                url = None

        if not url:
            if path in seen:
                url = seen[path]

        if not url:
            print "Can't find \"%s\"" % path
            url = raw_input("What url should I use? ").strip()
            if not url:
                url = None

            try:
                if url:
                    requests.get(url).raise_for_status()
            except requests.exceptions.RequestException:
                url = None

        if url:
            seen[path] = url

        if url and not exists:
            print path, '->', url
            file.seek(0)
            file.write(REDIRECT_NEW_TEMPLATE.format(url=url))
            file.write(data)
            return path, url

def main():
    # Get root
    root = check_output(['git', 'rev-parse', '--show-toplevel']).strip()
    os.chdir(root)
    print 'Using repo at:', root

    # Get branch info
    orig_branch = check_output(['git', 'name-rev', '--name-only', 'HEAD']).strip()
    branches = requests.get(REPO_API_URL+"/branches").json()

    # Ask for versions
    latest = raw_input('What is the latest version? ').lstrip('v')
    print 'Using latest:', latest

    versions = raw_input('What versions do you want to update? ')
    versions = [
        version.lstrip('v') for version in re.split('[, ]*', versions)
        if version]
    if not versions:
        versions = [
            branch['name'] for branch in branches
            if re.match(r'^\d*\.\d*$', branch['name'])]

    if latest in versions:
        versions.remove(latest)

    branches = {
        branch['name']: branch for branch in branches
        if branch['name'] in versions}
    
    print 'Using versions:'
    print ', '.join(branches[version]['name'] for version in versions)

    seen = {}
    redirects = {}

    # Edit stuff
    for version in versions:
        print 'Checking out %s...' % version
        check_output(['git', 'checkout', '-q',
            branches[version]['commit']['sha']])
        print 'Editing %s...' % version
        redirects[version] = []

        for dir, dirs, files in os.walk(DOCS_PATH_PREFIX):
            for file in files:
                if not file.endswith('.md'):
                    continue

                path = os.path.join(
                    os.path.relpath(dir, DOCS_PATH_PREFIX).lstrip('./'),
                    file)

                redirect = edit(path, latest, seen)
                if redirect:
                    redirects[version].append(redirect)

            for dir in dirs:
                if dir.startswith('.'):
                    dirs.remove(dir)

        if redirects[version]:
            print 'Committing %s...' % version
            check_output(['git', 'checkout', '-B',
                DOCS_BRANCH.format(version=version)])
            check_output(['git',
                '-c', 'user.name=' + MBED_BOT_USER,
                '-c', 'user.email=' + MBED_BOT_EMAIL,
                'commit', '-a',
                '-m', COMMIT_MESSAGE.format(version=version, latest=latest)])

    # Push/pr stuff
    print 'Done redirecting version!'
    create_prs = raw_input('Create prs? ')
    if create_prs in ['y', 'yes']:
        branch_names = [DOCS_BRANCH.format(version=version)
            for version in versions
            if redirects[version]]
        check_output(['git', 'push', '-f', REPO_PUSH_URL] + branch_names)

        for version in versions:
            if not redirects[version]:
                continue

            res = requests.post(REPO_API_URL+"/pulls",
                auth=(MBED_BOT_USER, MBED_BOT_TOKEN),
                json={
                    "title": COMMIT_MESSAGE.format(version=version, latest=latest),
                    "body": PR_BODY.format(version=version, latest=latest,
                        redirects='\n'.join('%s -> %s' % r for r in redirects[version])),
                    "head": "%s:%s" % (MBED_BOT_USER, DOCS_BRANCH.format(version=version)),
                    "base": version,
                })
            res.raise_for_status()
            print 'Created #%d' % res.json()['number']

    check_output(['git', 'checkout', '-q', orig_branch])
    print 'Done!'

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
