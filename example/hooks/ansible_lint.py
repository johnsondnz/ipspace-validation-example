#!/usr/bin/python3
# -*- coding: utf-8 -*-
# maintainer (@johnsondnz)
import re
import sys
import argparse
from ansiblelint.__main__ import main as ansible_lint


def _run_test(filename):
    """
    Inital entrypoint from __main__:
    params:
        filename: path to file that is checked

    Passes either a playbook or role dir into ansible-lint for processing
    As pre-commit passes a list of files that have changed there is need
    to track what has been parsed already
    """
    error = False
    checked = []  # instantiate list for appending checked file, avoids repeats on roles

    if "role" in filename:
        regex = r"^.+?/.+?/"  # matches `roles/*/`
        filename = re.match(regex, filename).group(0)  # extract the parent role dir
        sys.argv[1] = filename  # ansible-lint needs argv set
    if filename not in checked:
        error = ansible_lint() if error is not True else error  # ansible_lint() == traditional cmdline ansible-lint
        checked.append(filename)

    return error


def main(argv=None) -> bool:
    """
    Returns: bool as sys.exit code.  True = 1, False = 0.  Zero is good.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)
    error = False

    for filename in args.filenames:
        error = _run_test(filename) if error is not True else error

    try:
        return error
    except:
        return True


if __name__ == '__main__':
    sys.exit(main())
