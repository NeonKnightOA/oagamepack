#! /bin/bash

echo "*** WARNING! ***"
echo " "
echo "This file is designed to be executed from a Python 3 version of the
echo Anaconda terminal."
echo " "
echo "Python 3 and the 'pandas' module are required in order to run these scripts."
echo " "
echo "Before running this script, make sure you have these installed, otherwise"
echo "install Python and run 'pip install pandas'. Otherwise, press Ctrl + C."
echo "and do the aforementioned steps."
echo " "
printf 'Press Enter to continue...'
read _
./dos2unix.py
echo "Creating entity files for OA 0.8.8..."
./create_ent.py > ../install/OAPack/install/baseoa/entities.ent
./create_def.py > ../install/OAPack/install/baseoa/entities.def
./create_ent.py > ../oa.game/baseoa/entities.ent
./create_def.py > ../oa.game/baseoa/entities.def
echo "Creating entity files for OAX (for OA 0.8.8)..."
./create_ent_oax.py > ../install/OAPack/install/baseoa/entities_oax.ent
./create_def_oax.py > ../install/OAPack/install/baseoa/entities_oax.def
./create_ent_oax.py > ../oa.game/baseoa/entities_oax.ent
./create_def_oax.py > ../oa.game/baseoa/entities_oax.def
echo "Creating entity files for OA SVN r951..."
./create_ent.py > ../install/OASVNPack/install/baseoa/entities.ent
./create_def.py > ../install/OASVNPack/install/baseoa/entities.def
./create_ent.py > ../oasvn.game/baseoa/entities.ent
./create_def.py > ../oasvn.game/baseoa/entities.def
echo "Creating entity files for OAX (for OA SVN r951)..."
./create_ent_oax.py > ../install/OASVNPack/install/baseoa/entities_oax.ent
./create_def_oax.py > ../install/OASVNPack/install/baseoa/entities_oax.def
./create_ent_oax.py > ../oasvn.game/baseoa/entities_oax.ent
./create_def_oax.py > ../oasvn.game/baseoa/entities_oax.def
printf 'Press Enter to finish...'
read _
