#! /bin/bash

echo *** WARNING! ***
echo .
echo This file is designed to be executed from a Python 3 version of the
echo Anaconda terminal.
echo .
echo Python 3 and the 'pandas' module are required in order to run these scripts.
echo .
echo Before running this script, make sure you have these installed, otherwise
echo install Python and run 'pip install pandas'. Otherwise, press Ctrl + C.
echo and do the aforementioned steps.
echo .
printf 'Press any key to continue...'
read _
./create_ent.py > ../install/OAPack/install/baseoa/entities.ent
./create_def.py > ../install/OAPack/install/baseoa/entities.def
./create_ent.py > ../oa.game/baseoa/entities.ent
./create_def.py > ../oa.game/baseoa/entities.def
printf 'press any key to continue...'
read _
