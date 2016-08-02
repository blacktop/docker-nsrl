#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
search.py
~~~~~~~~

This module searches the bloomfilter for a given MD5 hash.

:copyright: (c) 2014 by Josh "blacktop" Maine.
:license: MIT
:improved_by: https://github.com/kost
"""

import argparse
import binascii

from pybloom import BloomFilter


def main():
    parser = argparse.ArgumentParser(prog='blacktop/nsrl')
    parser.add_argument("-v", "--verbose", help="Display verbose output message", action="store_true", required=False)
    parser.add_argument('hash', metavar='MD5', type=str, nargs='+', help='a md5 hash to search for.')
    args = parser.parse_args()

    with open('nsrl.bloom', 'rb') as nb:
        bf = BloomFilter.fromfile(nb)

        for hash_hex in args.hash:
            hash = binascii.unhexlify(hash_hex)
            if args.verbose:
                if hash in bf:
                    print "Hash {} found in NSRL Database.".format(hash_hex)
                else:
                    print "Hash {} was NOT found in NSRL Database.".format(hash_hex)
            else:
                print hash in bf
    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print "Error: %s" % e

# test_hash = 'AABCA0896728846A9D5B841617EBE746'
# calc_hash = '60B7C0FEAD45F2066E5B805A91F4F0FC'
