#!/bin/bash

# TODO : Also add http://www.mandiant.com/library/RedlineWL//m-whitelist-1.0.zip
echo "[INFO] Downloading NSRL Reduced Sets..."
wget http://www.nsrl.nist.gov/RDS/rds_2.44/rds_244m.zip 2> /dev/null
echo "[INFO] Unzip NSRL Database zip to /nsrl/ ..."
unzip -uo /rds_244m.zip -d /nsrl/
echo "[INFO] Deleting rds_244m.zip ..."
rm -f /rds_244m.zip
# Build bloomfilter from NSRL Database
cd /nsrl && python /nsrl/build.py
echo "[INFO] Deleting large NSRL database files ..."
rm -rf /nsrl/minimal/
