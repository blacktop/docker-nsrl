#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
search.py
~~~~~~~~

This module searches the bloomfilter for a given FILE name.

:copyright: (c) 2014 by Josh "blacktop" Maine.
:license: MIT
:improved_by: https://github.com/kost
"""

import argparse

from pybloom import BloomFilter


def main():
    parser = argparse.ArgumentParser(prog='blacktop/nsrl')
    parser.add_argument("-v", "--verbose", help="Display verbose output message", action="store_true", required=False)
    parser.add_argument('name', metavar='FILE', type=str, nargs='+', help='a file name to search for.')
    args = parser.parse_args()

    with open('nsrl.bloom', 'rb') as nb:
        bf = BloomFilter.fromfile(nb)

        for file_name in args.name:
            if args.verbose:
                if file_name in bf:
                    print "File {} found in NSRL Database.".format(file_name)
                else:
                    print "File {} was NOT found in NSRL Database.".format(file_name)
            else:
                print file_name in bf
    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print "Error: %s" % e
