#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# maintainer (@johnsondnz)
import yaml
import json
import sys
import argparse


def _run_test(filename):
    """
    Inital entrypoint from __main__:
    params:
        filename: path to file that is checked
    Comments: Prints results to stdout as part of test run.
    """
    tested = []
    error = False
    try:
        with open(filename) as f:
            site_vlans = yaml.load(f, Loader=yaml.FullLoader)["site_vlans"]

        for vlan in site_vlans:
            if vlan.get("vlan_id") not in tested:
                tested.append(vlan.get("vlan_id"))
            else:
                print(f"File: {filename} - {vlan['vlan_id']} appears more than once")
                error = True

    except (IOError, Exception):
        print(f"Something went wrong opening the file: {filename}")
        error = True
        pass

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

if __name__ == "__main__":
    sys.exit(main())
