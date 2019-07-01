#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation files
#(the "Software"), to deal in the Software without restriction,
#including without limitation the rights to use, copy, modify, merge,
#publish, distribute, sublicense, and/or sell copies of the Software,
#and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
#BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
#ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

"""
This module is responsible for loading the CSV files.
"""

import sys
import collections
import pandas as pd


def read_csv_to_dicts_append(result, filename, keyname):
    """Appends entries from 'filename' to 'result' with 'keyname' as the key"""
    reader = pd.read_csv(filename, encoding="ISO-8859-1")
    reader_dict = reader.to_dict('records')
    for row_dict in reader_dict:
        key = row_dict[keyname]
        if key in result:
            sys.exit("fatal error, the file: "+filename+" has double key: "+key)
        result[key] = row_dict
    return result

def read_csv_to_dicts(filename, keyname):
    """Returns a dict with the content from the CSV file given by 'filename'"""
    result = {}
    return read_csv_to_dicts_append(result, filename, keyname)

def fatal(error_msg):
    """Prints message and terminates the program with an error code"""
    print(error_msg)
    exit(1)


if len(sys.argv) < 2:
    fatal('Must be called like: \n'+sys.argv[0]+' ENTITIES_CSV_FILE')

ENTITIESCSVFILENAME = sys.argv[1]


ENTITIES = read_csv_to_dicts(ENTITIESCSVFILENAME, "item")
for i in range(2, len(sys.argv)):
    read_csv_to_dicts_append(ENTITIES, sys.argv[i], "item")
KEYS = read_csv_to_dicts("csv/keys.csv", "name")
KEY_TEXTS = read_csv_to_dicts("csv/key_text.csv", "key")
NOTES = read_csv_to_dicts("csv/note.csv", "name")
NOTE_TEXTS = collections.OrderedDict()
read_csv_to_dicts_append(NOTE_TEXTS, "csv/note_text.csv", "key")
SPAWNFLAGS = read_csv_to_dicts("csv/spawnflags.csv", "item")
SPAWNFLAG_TEXTS = read_csv_to_dicts("csv/spawnflag_text.csv", "key")
