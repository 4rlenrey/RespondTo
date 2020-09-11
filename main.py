#LearnYourBot by 4rlenrey

import json
import os
import random

#load json file
file = open("data.json", 'r')
data = json.load(file)

#get Message-type from known types in json
def gettype(message):
    Types = data["Type"]
    OptionsT = len(Types)
    for i in range(OptionsT):
        Type = data[Types[i]]
        Options = len(Type)
        for j in range(Options):
            messageTested = Type[j]
            if messageTested == message:
                return Types[i]
    return "unknown"

#Take care of input text
def handleInput():
    Recived = input("Message: ")
    if Recived == "quit":
        print("Exit")
        exit()
    Recivedtype = gettype(Recived)
    try:
        addtotypef(Recivedtype, Recived)
    except:
        print("No response type for ", Recivedtype)

#Add message to existing message_type
def addtotypef(Recivedtype, Recived):
    if Recivedtype == "unknown":
        print("To wich type do you want to add this word?")
        print(json.dumps(data["Type"]))
        addtoType = input()
        if addtoType in data["Type"]:
            print("adding to ", addtoType)
            data[addtoType].append(Recived)
            fileWrite = open("data.json", mode='w')
            fileWrite.write(json.dumps(data, indent=2))
            fileWrite.close()
        else:
            print("Type does not exist")
            addNewType(Recived, addtoType)
    else:
        respond(Recivedtype)

#Add new message-type to JSON
def addNewType(Recived, addtoType):
    print("Creating new type", addtoType)
    list = []
    list.append(Recived)
    data[addtoType] = list
    data["Type"].append(addtoType)
    fileWrite = open("data.json", mode='w')
    fileWrite.write(json.dumps(data, indent=2))
    fileWrite.close()

#Get response type for specific message
def getresponsetype(Recivedtype):
    list = data["Response"]
    response_type = list[Recivedtype]
    return response_type

#Print response
def respond(Recivedtype):
    response_type = getresponsetype(Recivedtype)
    response = data[response_type]
    print(random.choice(response))

def train():
    while True:
        #Just handle console messages for now
        handleInput()

train()
