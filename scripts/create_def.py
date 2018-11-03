#! /usr/bin/python3

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

import pandas as pd
import sys
import os.path


def readCsvToDictsAppend(result,filename,keyname):
    reader = pd.read_csv(filename)
    for row in reader.itertuples():
        rowDict = row._asdict()
        key = rowDict[keyname]
        if key in result:
            sys.exit("fatal error, the file: "+filename+" has double key: "+key)
        result[key] = rowDict
    return result

def readCsvToDicts(filename,keyname):
    result = {}
    return readCsvToDictsAppend(result,filename,keyname)

def fatal(errorMsg):
    print(errorMsg)
    exit(1)
    
entities = readCsvToDicts("entities.csv","item")
if (os.path.isfile("entities_extra.csv")):
    entities = readCsvToDictsAppend(entities, "entities_extra.csv", "item")
keys = readCsvToDicts("keys.csv","name")
key_texts = readCsvToDicts("key_text.csv","key")
q3map2keys = readCsvToDicts("q3map2keys.csv","name")
q3map2key_texts = readCsvToDicts("q3map2key_text.csv","key")
q3map2terrainkeys = readCsvToDicts("q3map2terrainkeys.csv","name")
q3map2terrainkey_texts = readCsvToDicts("q3map2terrainkey_text.csv","key")
notes = readCsvToDicts("note.csv","name")
note_texts = readCsvToDicts("note_text.csv", "key")
# There are no spawnflags.csv at the moment. We only have suspended and it is part if the QUAKED line
spawnflags = readCsvToDicts("spawnflags.csv","item")
spawnflag_texts = readCsvToDicts("spawnflag_text.csv","key")

def printKeys(item_name):
    for item in sorted(key_texts):
        if (item_name in keys.keys()):
            keyLine = keys[item_name]
            if (item in keyLine.keys()):
                hasKey = keyLine[item]
                #The hasKey == hasKey us used to check for NaN. Blank fields are NaNs in Pandas
                if (hasKey and hasKey == hasKey):
                    defaultText = ""
                    basename = item
                    basekey = key_texts[item]["basekey"]
                    if (isTrue(basekey)):
                        basename = basekey
                    name = basename
                    fullname = key_texts[item]["fullname"]
                    if (isinstance(fullname, str) and len(fullname)>0):
                        name = fullname
                    try:
                        defaultTextActual = keyLine[item+"_default"]
                        if key_texts[item]["type"] == "integer":
                            defaultText = " Default: "+str(int(defaultTextActual))+"."
                        else:
                            defaultText = " Default: "+str(defaultTextActual)+"."
                    except:
                        defaultText = ""
                    text = key_texts[item]["text"]
                    if (text and text == text):
                        print("\""+basename+"\" : "+str(key_texts[item]["text"])+defaultText)
                    else:
                        print("\""+basename+"\" : No text"+defaultText)

def printNotes(item_name):
    for item in sorted(note_texts):
        if (item_name in notes.keys()):
            keyLine = notes[item_name]
            if (item in keyLine.keys()):
                hasKey = keyLine[item]
                if (hasKey and hasKey == hasKey):
                    print(str(note_texts[item]["text"]))
                    

def isTrue(some_value):
    # True is represented by the string "true". Note that pandas uses NaN for blank strings
    if (isinstance(some_value, str) and len(some_value)>0):
        return True
    return False
    
for item in sorted(entities):
    row = entities[item]
    print(row["quaked"])
    if isinstance(row["model"],str):
        model = row["model"]
        print("--------- MODEL FOR RADIANT ONLY - DO NOT SET THIS AS A KEY --------")
        print("model=\""+model+"\"")
    if isinstance(row["description"],str):
        print(row["description"])
    print("--------- KEYS --------")
    printKeys(item)
    # print("--------- Q3MAP2 KEYS --------")
    # printQ3Map2Keys(item)
    # print("--------- Q3MAP2 TERRAIN KEYS --------")
    # printQ3Map2TerrainKeys(item)
    # print("--------- SPAWNFLAGS --------")
    # printSpawnflags(item)
    print("--------- NOTES --------")
    printNotes(item)
    print("*/")
    