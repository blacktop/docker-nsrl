# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
build.py
~~~~~~~~

This module builds a bloomfilter from the NSRL Whitelist Database.

:copyright: (c) 2014 by Josh "blacktop" Maine.
:license: GPLv3

"""

import os
import sys
from itertools import *
from pybloomfilter import BloomFilter
import collections
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer

error_rate = 0.01
# nsrl_path = '/nsrl/minimal/NSRLFile.txt'
nsrl_path = '/Volumes/Data/Projects/github/docker-nsrl/nsrl/NSRLFile.txt'
# nsrl_path = '/Volumes/Data/Projects/github/docker-nsrl/nsrl/NSRLFile_100.txt'

def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

# http://stackoverflow.com/a/9631635
def blocks(this_file, size=65536):
# def blocks(this_file, size=200):
    parts = ['', '']
    while True:
        b = this_file.read(size)
        chunck = parts[1] + b
        if not b:
            yield parts[1].split('\r\n')
            break
        parts = chunck.rsplit('\r\n', 1)
        yield parts[0].split('\r\n')


def get_hashes(this_file, count=1000):
    while True:
        lines = []
        for i in xrange(0, count):
            line = this_file.readline()
            if not line:
                break
            lines.append(line)
        if not lines:
            break
        # hashes = [line.split(",")[1].strip('"') for line in lines]
        yield [line.split(",")[1].strip('"') for line in lines]

def main():
    # num_lines = 37514128
    if os.path.isfile(nsrl_path):
        print "INFO: Reading in NSRL Database"
        with open(nsrl_path) as f_line:
            print "INFO: Calculating number of hashes in NSRL..."
            num_lines = sum(len(bl) for bl in blocks(f_line))
            print "INFO: There are %s hashes in the NSRL Database" % num_lines
        with open(nsrl_path) as f_nsrl:
            # Strip off header
            header = f_nsrl.readline()
            print "INFO: Creating bloomfilter"
            bf = BloomFilter(num_lines, error_rate, 'nsrl.bloom')
            print "INFO: Inserting hashes into bloomfilter"
            # bf.add((line.split(",")[1].strip('"') for line in f_nsrl))
            file_size = os.path.getsize(nsrl_path)
            # print 'Starting [          ]',
            # print '\b'*12,
            # sys.stdout.flush()
            # for lines in blocks(f_nsrl, size=(file_size / 50)):
            widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()]
            pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
            for hashes in get_hashes(f_nsrl, count=(num_lines / 10)):
                if hashes:
                    try:
                        bf.update(hashes)
                    except Exception as e:
                        print "ERROR: %s" % e
                # print '\b.',
                # sys.stdout.flush()
                pbar.update()
            pbar.finish()
            # print '\b]  Done!'
            print "INFO: NSRL bloomfilter contains {} items.".format(len(bf))
            print "Complete"
    else:
        print("ERROR: No such file or directory: %s", nsrl_path)
    return


if __name__ == "__main__":
    main()
