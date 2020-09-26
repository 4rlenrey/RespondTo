#RespondTo by 4rlenrey

import json
import random


#get Message-type from known types in json
def gettype(message):
    FILE = open("data.json", 'r')
    DATA = json.load(FILE)
    types = DATA["Type"]
    options_t = len(types)
    for i in range(options_t):
        msg_type = DATA[types[i]]
        options = len(msg_type)
        for j in range(options):
            message_tested = msg_type[j]
            if message_tested == message:
                return types[i]
    FILE.close()
    return "unknown"


#Add message to existing message_type
def addtotypef(recived_type, recived, add_to_type):
    FILE = open("data.json", 'r')
    DATA = json.load(FILE)
    if recived_type == "unknown":
        if add_to_type in DATA["Type"]:
            print("adding to ", add_to_type)
            DATA[add_to_type].append(recived)
            file_write = open("data.json", mode='w')
            file_write.write(json.dumps(DATA, indent=2))
            file_write.close()
        else:
            add_new_type(recived, add_to_type)
    else:
        respond(recived_type)
    FILE.close()

#Add new message-type to JSON
def add_new_type(recived, add_to_type):
    FILE = open("data.json", 'r')
    DATA = json.load(FILE)
    print("Creating new type", add_to_type)
    list_r = []
    list_r.append(recived)
    DATA[add_to_type] = list_r
    DATA["Type"].append(add_to_type)
    file_write = open("data.json", mode='w')
    file_write.write(json.dumps(DATA, indent=2))
    file_write.close()
    FILE.close()

#Get response type for specific message
def get_response_type(recived_type):
    FILE = open("data.json", 'r')
    DATA = json.load(FILE)
    list_r = DATA["Response"]
    try:
        response_type = list_r.get(recived_type)
    except:
        response_type = "unknown"
    FILE.close()
    return response_type
        

#Print response
def respond(recived_type):
    FILE = open("data.json", 'r')
    DATA = json.load(FILE)
    response_type = get_response_type(recived_type)
    response = DATA[response_type]
    FILE.close()
    return random.choice(response)

#add new response type for message
def match_response_type(message_type, response_type):
    FILE = open("data.json", 'r')
    DATA = json.load(FILE)
    DATA["Response"][message_type] = response_type
    file_write = open("data.json", mode='w')
    file_write.write(json.dumps(DATA, indent=2))
    file_write.close()
    FILE.close()

