#! /bin/bash
set -e

echo Testing create_def.py
python3 create_def.py > /dev/null
echo Passed
echo Testing create_ent.py
python3 create_ent.py > /dev/null
echo Passed
