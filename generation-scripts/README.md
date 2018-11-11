# oagamepack_scripts
Script to generate the Radiant ent file from csv files.

Requires python3 and pandas.
I had hoped to only use pure python without libraries but the build in csv reader was not good enough.


./create_ent.py will print the ent file to stdout.

There are no keys at the moment. Only descriptions from the source.

Notes:
The panda package is called python3-pandas in Ubuntu.
On Windows the python3 version of Anaconda (https://www.anaconda.com/download/)

Output is located in the output folder.

# Compiling
The scripts "create_output.bat" and "create_output.sh" can be used to generate the output file. The bat file expects to be executed on Windows with a python3 install of Anaconda.

# Editing
See an example on how to use the CSV files here: https://docs.google.com/document/d/1xmpfXyfEj-K2Jjw-cRO470kog62AId5NVvTteQ-tXz4/edit?usp=sharing

# License
Data in entities.csv is extracted from OpenArena source and is under GPLv2 or later and so is the rest of the data and therefore also the result.
The script is MIT licensed.
