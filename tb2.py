import os 
"""Saving Voice to a files"""

name = "der-fuenfte-elefant"

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
    os.system(command)
    print("done")

file_path = '5_wn.txt'
print("start read")
with open(file_path, 'r') as file:
    fileContent = ""
    line = file.readline()
    
    while line:
        fileContent += line
        line = file.readline()
print("read finished")
fullLength = len(fileContent)
print("Lenth: " + str(fullLength))

partLength = 10000
part = 1
offset = 0
partContend = ""
diff = fullLength - offset
while diff > partLength:
    partContend = fileContent[offset:(offset + partLength)]
    saveParttoFile(part=part,
        partContend=partContend,
        offset=offset)
    offset += partLength
    diff = fullLength - offset
    part += 1
partContend = fileContent[offset:fullLength]
saveParttoFile(part=part,
    partContend=partContend,
    offset=offset)

print("finished")
