#!/bin/bash

# TODO : Also add http://www.mandiant.com/library/RedlineWL//m-whitelist-1.0.zip
# Grab NSRL Reduced Sets
wget http://www.nsrl.nist.gov/RDS/rds_2.44/rds_244m.zip 2> /dev/null
# Unzip NSRL Database zip to /nsrl/
unzip -uo /rds_244m.zip -d /nsrl/
rm -f /nsrl/rds_244m.zip
# Build bloomfilter from NSRL Database
python /nsrl/build.py
# Delete large NSRL database files.
rm -rf /nsrl/minimal/
