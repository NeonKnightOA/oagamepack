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

import create_common as common

def printKeys(item_name):
    for item in sorted(common.KEY_TEXTS):
        if item_name in common.KEYS.keys():
            keyLine = common.KEYS[item_name]
            if item in keyLine.keys():
                hasKey = keyLine[item]
                #The hasKey == hasKey us used to check for NaN. Blank fields are NaNs in Pandas
                if (hasKey and hasKey == hasKey):
                    defaultText = ""
                    basename = item
                    basekey = common.KEY_TEXTS[item]["basekey"]
                    if isTrue(basekey):
                        basename = basekey
                    name = basename
                    fullname = common.KEY_TEXTS[item]["fullname"]
                    if (isinstance(fullname, str) and fullname):
                        name = fullname
                    try:
                        defaultTextActual = keyLine[item+"_default"]
                        if common.KEY_TEXTS[item]["type"] == "integer":
                            defaultText = " Default: "+str(int(defaultTextActual))+"."
                        else:
                            defaultText = " Default: "+str(defaultTextActual)+"."
                    except:
                        defaultText = ""
                    text = common.KEY_TEXTS[item]["text"]
                    if (text and text == text):
                        print("\""+basename+"\" : "+str(common.KEY_TEXTS[item]["text"])+defaultText)
                    else:
                        print("\""+basename+"\" : No text"+defaultText)

def printNotes(item_name):
    for item in common.NOTE_TEXTS.keys():
        if item_name in common.NOTES.keys():
            keyLine = common.NOTES[item_name]
            if item in sorted(keyLine.keys()):
                hasKey = keyLine[item]
                if (hasKey and hasKey == hasKey):
                    print(str(common.NOTE_TEXTS[item]["text"]))
                    

def isTrue(some_value):
    # True is represented by the string "true". Note that pandas uses NaN for blank strings
    if (isinstance(some_value, str) and some_value):
        return True
    return False

def main():
    for item in sorted(common.ENTITIES):
        row = common.ENTITIES[item]
        print(row["quaked"])
        if isinstance(row["model"], str):
            model = row["model"]
            print("--------- MODEL FOR RADIANT ONLY - DO NOT SET THIS AS A KEY --------")
            print("model=\""+model+"\"")
        if isinstance(row["description"], str):
            print(row["description"])
        print("--------- KEYS --------")
        printKeys(item)
        print("--------- NOTES --------")
        printNotes(item)
        print("*/")
        
main()
    