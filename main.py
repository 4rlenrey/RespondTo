#RespondTo by 4rlenrey

import json
import random

#load json file
FILE = open("data.json", 'r')
DATA = json.load(FILE)

#get Message-type from known types in json
def gettype(message):
    types = DATA["Type"]
    options_t = len(types)
    for i in range(options_t):
        msg_type = DATA[types[i]]
        options = len(msg_type)
        for j in range(options):
            message_tested = msg_type[j]
            if message_tested == message:
                return types[i]
    return "unknown"

#Take care of input text
def handle_input():
    recived = input("Message: ")
    if recived == "quit":
        exit()
    recived_type = gettype(recived)
    try:
        addtotypef(recived_type, recived)
    except:
        print("No response type for ", recived_type)

#Add message to existing message_type
def addtotypef(recived_type, recived):
    if recived_type == "unknown":
        print("To wich type do you want to add this word? \n", json.dumps(DATA["Type"]))
        add_to_type = input()
        if add_to_type in DATA["Type"]:
            print("adding to ", add_to_type)
            DATA[add_to_type].append(recived)
            file_write = open("data.json", mode='w')
            file_write.write(json.dumps(DATA, indent=2))
            file_write.close()
        else:
            print("Type does not exist")
            add_new_type(recived, add_to_type)
    else:
        respond(recived_type)

#Add new message-type to JSON
def add_new_type(recived, add_to_type):
    print("Creating new type", add_to_type)
    list_r = []
    list_r.append(recived)
    DATA[add_to_type] = list_r
    DATA["Type"].append(add_to_type)
    file_write = open("data.json", mode='w')
    file_write.write(json.dumps(DATA, indent=2))
    file_write.close()

#Get response type for specific message
def getresponsetype(recived_type):
    list_r = DATA["Response"]
    response_type = list_r[recived_type]
    return response_type

#Print response
def respond(recived_type):
    response_type = getresponsetype(recived_type)
    response = DATA[response_type]
    print(random.choice(response))

def train():
    while True:
        #Just handle console messages for now
        handle_input()

train()
