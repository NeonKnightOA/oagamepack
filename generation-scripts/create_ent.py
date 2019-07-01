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

import re
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
                    if (isinstance(basekey, str) and basekey):
                        basename = basekey
                    name = basename
                    fullname = common.KEY_TEXTS[item]["fullname"]
                    if (isinstance(fullname, str) and fullname):
                        name = fullname
                    try:
                        defaultTextActual = keyLine[item+"_default"]
                        if common.KEY_TEXTS[item]["type"] == "integer":
                            defaultText = ". Default: "+str(int(defaultTextActual))+"."
                        else:
                            defaultText = ". Default: "+str(defaultTextActual)+"."
                        if not (defaultTextActual and defaultTextActual == defaultTextActual):
                            defaultText = ""
                    except:
                        defaultText = ""
                    text = common.KEY_TEXTS[item]["text"]
                    if not (text and text == text):
                        text = "No text"
                    print("<"+str(common.KEY_TEXTS[item]["type"])+
                          " key=\""+str(basename)+"\" name=\""+str(name)+"\">"+
                          text+str(defaultText)+"</"+str(common.KEY_TEXTS[item]["type"])+">")

def printNotes(item_name):
    for item in common.NOTE_TEXTS:
        if item_name in sorted(common.NOTES.keys()):
            keyLine = common.NOTES[item_name]
            if item in sorted(keyLine.keys()):
                hasKey = keyLine[item]
                if (hasKey and hasKey == hasKey):
                    print(common.NOTE_TEXTS[item]["text"])

def printSpawnflags(item_name):
    for item in sorted(common.SPAWNFLAG_TEXTS):
        if item_name in sorted(common.SPAWNFLAGS.keys()):
            keyLine = common.SPAWNFLAGS[item_name]
            if item in sorted(keyLine.keys()):
                hasKey = keyLine[item]
                flagRow = common.SPAWNFLAG_TEXTS[item]
                if (hasKey and hasKey == hasKey):
                    print("<flag key=\""+str(flagRow["key"])+"\" name=\""+
                          str(flagRow["fullname"])+"\" bit=\""+str(flagRow["bit"])+
                          "\">"+str(flagRow["text"])+"</flag>")

def main():
    print("<?xml version=\"1.0\"?>")
    print("<classes>")
    for item in sorted(common.ENTITIES):
        row = common.ENTITIES[item]
        quaked = row["quaked"]
        model = ""
        box1 = ""
        box2 = ""
        p = re.compile('\((.+?)\)')
        parans = p.findall(quaked)
        try:
            color = parans[0]
        except AttributeError:
            common.fatal("Failed it find color in: "+quaked)
        if len(parans) > 1:
            box1 = parans[1]
        if len(parans) > 2:
            box2 = parans[2]
        if isinstance(row["model"], str):
            model = row["model"]
        xmlType = "point"
        if not (box1 or box2):
            xmlType = "group"
        print("  <"+xmlType+" name=\"" + item + "\" color=\""+color+"\"", end="")
        if (box1 and box2):
            print(" box=\""+box1+" "+box2+"\"", end="")
        print(" model=\""+model+"\">")
        if isinstance(row["description"], str):
            print(row["description"])
        print("-------- KEYS --------")
        printKeys(item)
        print("-------- SPAWNFLAGS --------")
        printSpawnflags(item)
        print("-------- NOTES --------")
        printNotes(item)
        print("  </"+xmlType+">")
    print("</classes>")

main()
