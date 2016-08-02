# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
build.py
~~~~~~~~
This module builds a bloomfilter from the NSRL Whitelist Database.
:copyright: (c) 2014 by Josh "blacktop" Maine.
:license: MIT
:improved_by: https://github.com/kost
"""

import os
import sys

from pybloom import BloomFilter

nsrl_path = '/nsrl/NSRLFile.txt'
error_rate = 0.01


# reference - http://stackoverflow.com/a/9631635
def blocks(this_file, size=65536):
    while True:
        b = this_file.read(size)
        if not b:
            break
        yield b


def main(argv):
    if argv:
        error_rate = float(argv[0])
    print "[BUILDING] Using error-rate: {}".format(error_rate)
    if os.path.isfile(nsrl_path):
        print "[BUILDING] Reading in NSRL Database"
        with open(nsrl_path) as f_line:
            # Strip off header
            _ = f_line.readline()
            print "[BUILDING] Calculating number of hashes in NSRL..."
            num_lines = sum(bl.count("\n") for bl in blocks(f_line))
            print "[BUILDING] There are %s hashes in the NSRL Database" % num_lines
        with open(nsrl_path) as f_nsrl:
            # Strip off header
            _ = f_nsrl.readline()
            print "[BUILDING] Creating bloomfilter"
            bf = BloomFilter(num_lines, error_rate)
            print "[BUILDING] Inserting hashes into bloomfilter"
            for line in f_nsrl:
                file_name = line.split(",")[3].strip('"')
                if file_name:
                    try:
                        bf.add(file_name)
                    except Exception as e:
                        print "[ERROR] %s" % e
            print "[BUILDING] NSRL bloomfilter contains {} items.".format(len(bf))
            with open('nsrl.bloom', 'wb') as nb:
                bf.tofile(nb)
            print "[BUILDING] Complete"
    else:
        print("[ERROR] No such file or directory: %s", nsrl_path)

    return


if __name__ == "__main__":
    main(sys.argv[1:])
