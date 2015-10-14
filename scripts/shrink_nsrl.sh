#!/bin/bash

echo "[INFO] Downloading NSRL Reduced Sets..."
NSRL_URL="http://www.nsrl.nist.gov/"
MIN_SET=$(curl ${NSRL_URL}Downloads.htm 2> /dev/null | \
  grep -m 1  "Minimal set" | \
  grep -o '<a href=['"'"'"][^"'"'"']*['"'"'"]' | \
  sed -e 's/^<a href=["'"'"']//' -e 's/["'"'"']$//')
curl -O $NSRL_URL$MIN_SET 2> /dev/null

echo "[INFO] Unzip NSRL Database zip to /nsrl/minimal ..."
mkdir /nsrl/minimal
unzip -juo /rds_*.zip -d /nsrl/minimal

echo "[INFO] Deleting rds_244m.zip ..."
rm -f /rds_*.zip

echo "[INFO] Build bloomfilter from NSRL Database ..."
cd /nsrl && python /nsrl/build.py
echo "[INFO] Listing created files ..."
ls -l /nsrl

echo "[INFO] Deleting large NSRL database files ..."
rm -rf /nsrl/minimal/

# TODO : Also add http://www.mandiant.com/library/RedlineWL//m-whitelist-1.0.zip
