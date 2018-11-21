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
import re

def readCsvToDictsAppend(result,filename,keyname):
    reader = pd.read_csv(filename, encoding = "ISO-8859-1")
    readerDict = reader.to_dict('records')
    for rowDict in readerDict:
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


if len(sys.argv) < 2:
    print('Must be called like: \n'+sys.argv[0]+' ENTITIES_CSV_FILE')
    exit(1)

entitiesCsvFilename = sys.argv[1]

print("<?xml version=\"1.0\"?>")

entities = readCsvToDicts(entitiesCsvFilename,"item")
for i in range (2,len(sys.argv)):
    readCsvToDictsAppend(entities,sys.argv[i],"item")
keys = readCsvToDicts("csv/keys.csv","name")
key_texts = readCsvToDicts("csv/key_text.csv","key")
notes = readCsvToDicts("csv/note.csv","name")
note_texts = readCsvToDicts("csv/note_text.csv", "key")
# There are no spawnflags.csv at the moment. We only have suspended and it is part if the QUAKED line
spawnflags = readCsvToDicts("csv/spawnflags.csv","item")
spawnflag_texts = readCsvToDicts("csv/spawnflag_text.csv","key")

def printKeys(item_name):
    for item in sorted(key_texts):
        if item_name in keys.keys():
            keyLine = keys[item_name]
            if item in keyLine.keys():
                hasKey = keyLine[item]
                #The hasKey == hasKey us used to check for NaN. Blank fields are NaNs in Pandas
                if (hasKey and hasKey == hasKey):
                    defaultText = ""
                    basename = item
                    basekey = key_texts[item]["basekey"]
                    if (isinstance(basekey, str) and len(basekey)>0):
                        basename = basekey
                    name = basename
                    fullname = key_texts[item]["fullname"]
                    if (isinstance(fullname, str) and len(fullname)>0):
                        name = fullname
                    try:
                        defaultTextActual = keyLine[item+"_default"]
                        if key_texts[item]["type"] == "integer":
                            defaultText = ". Default: "+str(int(defaultTextActual))+"."
                        else:
                            defaultText = ". Default: "+str(defaultTextActual)+"."
                        if not (defaultTextActual and defaultTextActual == defaultTextActual):
                            defaultText = ""
                    except:
                        defaultText = ""
                    text = key_texts[item]["text"]
                    if not (text and text == text):
                        text = "No text"
                    print("<"+str(key_texts[item]["type"])+" key=\""+str(basename)+"\" name=\""+str(name)+"\">"+text+str(defaultText)+"</"+str(key_texts[item]["type"])+">")

def printNotes(item_name):
    for item in note_texts:
        if item_name in sorted(notes.keys()):
            keyLine = notes[item_name]
            if item in sorted(keyLine.keys()):
                hasKey = keyLine[item]
                if (hasKey and hasKey == hasKey):
                    print(note_texts[item]["text"])

def printNonSuspendedSpawnflags(item_name):
    for item in spawnflag_texts:
        if item_name in sorted(spawnflags.keys()):
            keyLine = spawnflags[item_name]
            if item in sorted(keyLine.keys()):
                hasKey = keyLine[item]
                flagRow = spawnflag_texts[item]
                if (hasKey and hasKey == hasKey):
                    print("<flag key=\""+str(flagRow["key"])+"\" name=\""+str(flagRow["fullname"])+"\" bit=\""+str(flagRow["bit"])+"\">"+str(flagRow["text"])+"</flag>")


def printSpawnflags(item_name):
    if (item == "SUSPENDED" and "suspended" in entities[item_name]["quaked"]):
        flagRow = spawnflag_texts["SUSPENDED"]
        print("<flag key=\""+str(flagRow["key"])+"\" name=\""+str(flagRow["fullname"])+"\" bit=\""+str(flagRow["bit"])+"\">"+str(flagRow["text"])+"</flag>")
    printNonSuspendedSpawnflags(item_name)


print("<classes>")
for item in sorted(entities):
    row = entities[item]
    quaked = row["quaked"]
    model = ""
    box1= ""
    box2= ""
    p = re.compile('\((.+?)\)')
    parans = p.findall(quaked)
    try:
        color = parans[0]
    except AttributeError:
        fatal("Failed it find color in: "+quaked)
    if (len(parans) > 1):
        box1 = parans[1]
    if (len(parans) > 2):
        box2 = parans[2]
    if isinstance(row["model"],str):
        model = row["model"]
    xmlType = "point"
    if not (box1 or box2):
        xmlType = "group"
    print("  <"+xmlType+" name=\"" + item + "\" color=\""+color+"\"", end ="")
    if (box1 and box2):
        print(" box=\""+box1+" "+box2+"\"", end = "")
    print(" model=\""+model+"\">")
    if isinstance(row["description"],str):
        print(row["description"])
    print("-------- KEYS --------")
    printKeys(item)
    # print("-------- Q3MAP2 KEYS --------")
    # printQ3Map2Keys(item)
    # print("-------- Q3MAP2 TERRAIN KEYS --------")
    # printQ3Map2Terrain(item)
    print("-------- SPAWNFLAGS --------")
    printSpawnflags(item)
    print("-------- NOTES --------")
    printNotes(item)
    print("  </"+xmlType+">")
print("</classes>")
