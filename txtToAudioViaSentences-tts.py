# gTTS cli must be installed

import os 
"""Saving Voice to a files"""

name = "ruhig-blut"

def getIntAsString(value,minLength):
    stringValue = str(value)
    while len(stringValue) < minLength:
        stringValue = "0" + stringValue
    return stringValue

def saveSentanceToFile(mainPart,part,sentence):
    fileName = "mp3_" + getIntAsString(mainPart, 2) + "/" + name + "_" + getIntAsString(part, 8) + ".mp3"
    command = "gtts-cli \"" + sentence.strip() + "\" --lang de --output " + fileName
    print(fileName + ": bytes: " + str(len(sentence)) + ")")
    #print(command)
    os.system(command)
    if len(sentence) < 11:
        print("[WARNING] Short sentence: " + sentence)
    print("done")


file_path = "/home/hendrik/tmp/test_espeag-ng/gtts/ruhig-blut.txt"
print("start read")
with open(file_path, 'r') as file:
    fileContent = ""
    line = file.readline()
    while line:
        fileContent += line
        line = file.readline()


print("read finished")
fileContent = fileContent.replace("\n", "")

fullLength = len(fileContent)
print("Lenth: " + str(fullLength))

sentences = fileContent.split(". ")
numOfSentences = len(sentences)
print("Sentences: " + str(numOfSentences))

processed = 0
maxProcessed = 60000;
mainPart = 0
part = 0
convertMainPart = 7
convertMainPartString = getIntAsString(convertMainPart, 2)
path = "mp3_" + convertMainPartString
mainPath = "mp3_main" 

command = "mkdir -p " + mainPath
print(command)
os.system(command)

command = "mkdir -p " + path
print(command)
os.system(command)

for sentence in sentences:
    if sentence != "..":
        processed += len(sentence)
        part += 1
        if mainPart == convertMainPart:
            saveSentanceToFile(mainPart=mainPart,
                part=part,
                #sentence=(sentence + ".").replace("...","."))
                sentence=sentence.replace(".",""))
        #else:
            #print("switch sentence number " + str(part))
        if processed > maxProcessed:
            mainPart += 1
            processed = 0
            print("MP: " + str(mainPart))


mergeName = path + "/" +name + "_text-to-speak-gtts_" + convertMainPartString


command = "cat " + path + "/" + name + "_*.mp3 > " + mergeName + ".mp3"
#command = "mp3wrap " + mergeName + ".mp3 " + path + "/" + name + "_*.mp3"
print(command)
os.system(command)

#command = "mv " + mergeName + "*.mp3 " + mergeName + ".mp3"
#print(command)
#os.system(command)

targetName = mergeName.replace(path, mainPath)
command = "cp " + mergeName + ".mp3 " + targetName + ".mp3"
print(command)
os.system(command)

print("Out: " + mergeName + ".mp3 / " + targetName + ".mp3")