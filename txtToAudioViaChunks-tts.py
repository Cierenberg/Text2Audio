# gTTS cli must be installed

import os 
"""Saving Voice to a files"""

name = "ruhig-blut"


def optimizeCutPosition(text,desired):
    start = int(desired) - 200
    end = int(desired)
    while not (text[start] == "." and text[start + 1] == " ") and start < end:
        start += 1
    return start + 1

def getIntAsString(value,minLength):
    stringValue = str(value)
    while len(stringValue) < minLength:
        stringValue = "0" + stringValue
    return stringValue

def saveParttoFile(part,partContend,offset):
    fileName = name + "_" + getIntAsString(part, 4) + ".mp3"
    command = "gtts-cli \"" + partContend + "\" --lang de --output " + fileName
    print(fileName + ": Offset:" + str(offset) + " (bytes: " + str(len(partContend)) + ")")
    print(command)
    #os.system(command)
    print("done")



file_path = 'ruhig-blut.txt'
print("start read")
with open(file_path, 'r') as file:
    fileContent = ""
    line = file.readline()
    
    while line:
        fileContent += line
        line = file.readline()
print("read finished")
#fileContent = fileContent.replace("\n", "").replace("\"","\\\"").replace("!","\!")
fileContent = fileContent.replace("\n", "")

fullLength = len(fileContent)
print("Lenth: " + str(fullLength))

partLength = 20000
part = 1
offset = 0

mainPart = 0
mainPartString = getIntAsString(mainPart, 2)
mainpartStart = mainPart * 4
mainpartEnd = mainpartStart + 3
path = "mp3_" + mainPartString
mainPath = "mp3_main"

command = "mkdir -p " + mainPath
print(command)
os.system(command)

command = "mkdir -p " + path
print(command)
os.system(command)

name = path + "/" + name

partContend = ""
diff = fullLength - offset
while diff > (partLength + 10):
    optimized = optimizeCutPosition(
        text = fileContent[offset:fullLength],
        desired = partLength)
    partContend = fileContent[offset:(offset + optimized)]
    if part < mainpartStart or part > mainpartEnd:
        print ("switch part: " + str(part)) 
    else:
        saveParttoFile(part=part,
            partContend=partContend,
            offset=offset)
    offset += optimized
    diff = fullLength - offset
    part += 1
partContend = fileContent[offset:fullLength]
if part < mainpartStart or part > mainpartEnd:
    print ("switch part: " + str(part)) 
else:
    saveParttoFile(part=part,
        partContend=partContend,
        offset=offset)

mergeName = name + "_text-to-speak-gtts_" + mainPartString

command = "mp3wrap " + mergeName + ".mp3 " + name + "_*.mp3"
print(command)
os.system(command)

command = "mv " + mergeName + "*.mp3 " + mergeName + ".mp3"
print(command)
os.system(command)

targetName = mergeName.replace(path, mainPath)
command = "cp " + mergeName + ".mp3 " + targetName + ".mp3"
print(command)
os.system(command)

print("Out: " + mergeName + ".mp3 / " + targetName + ".mp3")
