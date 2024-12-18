# gTTS cli must be installed

import os 
"""Saving Voice to a files"""

name = "der-fuenfte-elefantl"
nameOrg = name

vpnPostList = ["122106","124117","135116","144113","150125","192102","243132","279104","292124","293119","100122"]
vpnPre = "NL-FREE#"

errorlist = []

mainPartFactor = 4


singleRequest = True
singleRequestParts = [14,19]
singleRequestVPN = len(vpnPostList) - 1
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
    if singleRequest:
        mp = int(part / 4)
        fileName = "mp3_" + getIntAsString(mp, 2) + "/" + nameOrg + "_" + getIntAsString(part, 4) + ".mp3"
        hint = "mp3wrap mp3_" + getIntAsString(mp, 2) + "/" + nameOrg + "_text-to-speak-gtts_" + getIntAsString(mp, 2) + "_2.mp3 mp3_" + getIntAsString(mp, 2) + "/" + nameOrg + "der-fuenfte-elefantl_0*.mp3"
        command = "rm " + fileName
        print(command)
        os.system(command)
        print(hint)
    command = "gtts-cli \"" + partContend.strip().replace("*","") + "\" --lang de --output " + fileName
    print(fileName + ": Offset:" + str(offset) + " (bytes: " + str(len(partContend)) + ")")
    try:
        #print(command)
        os.system(command)
        #print("No Actiom")
    except BaseException as e:
        print("[ERROR] " + e)
        errorlist.append(str(part) + ": " + name + "_" + getIntAsString(part, 4) + "(" + e + ")")
    print("done")


def changeVPM(number):
    server = vpnPre + vpnPostList[number]
    command = "protonvpn-cli d"
    #print(command)
    os.system(command)
    command = "protonvpn-cli connect " + server
    #print(command)
    os.system(command)
    command = "protonvpn-cli s"
    #print(command)
    os.system(command)
    


file_path = 'der-fuenfte-elefantl.txt'
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

partLength = 16000
part = 1
offset = 0

mainPart = 0

"mp3_"
finished = False


if singleRequest:
    changeVPM(singleRequestVPN)


while not finished:
    if not singleRequest:
        changeVPM(mainPart)

    mainPartString = getIntAsString(mainPart, 2)
    mainpartStart = mainPart * mainPartFactor
    mainpartEnd = mainpartStart + mainPartFactor - 1
    path = "mp3_" + mainPartString
    mainPath = "mp3_main"

    command = "mkdir -p " + mainPath
    print(command)
    os.system(command)

    command = "mkdir -p " + path
    print(command)
    os.system(command)

    name = path + "/" + nameOrg

    partContend = ""
    diff = fullLength - offset
    while diff > (partLength + 10):
        optimized = optimizeCutPosition(
            text = fileContent[offset:fullLength],
            desired = partLength)
        partContend = fileContent[offset:(offset + optimized)]
        if singleRequest:
            if part in singleRequestParts:
                saveParttoFile(part=part,
                    partContend=partContend,
                    offset=offset)
            else:
                print ("switch part: " + str(part)) 
        else:
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
    if singleRequest:
        if part in singleRequestParts:
            saveParttoFile(part=part,
                partContend=partContend,
                offset=offset)
        else:
            print ("switch part: " + str(part)) 
    else:    
        if part < mainpartStart or part > mainpartEnd:
            print ("switch part: " + str(part)) 
        else:
            saveParttoFile(part=part,
                partContend=partContend,
                offset=offset)

    mergeName = name + "_text-to-speak-gtts_" + mainPartString
    targetName = mergeName.replace(path, mainPath)
    
    if not singleRequest:
        command = "mp3wrap " + mergeName + ".mp3 " + name + "_*.mp3"
        print(command)
        os.system(command)

        command = "mv " + mergeName + "*.mp3 " + mergeName + ".mp3"
        print(command)
        os.system(command)

        
        command = "cp " + mergeName + ".mp3 " + targetName + ".mp3"
        print(command)
        os.system(command)
        print("Out: " + mergeName + ".mp3 / " + targetName + ".mp3")
    mainPart += 1
    finished = mainPart * 4 > part
    if singleRequest:
        finished = True
        print(run: mp3wrap der-fuenfte-elefantl_text-to-speak-gtts_03_2.mp3 /home/hendrik/tmp/test_espeag-ng/gtts/mp3_03/der-fuenfte-elefantl_0*.mp3)
    part = 1
    offset = 0
if len(errorlist) > 0:
    print("\n\nErrors:")
    for err in errorlist:
        print("\t* " + err)
