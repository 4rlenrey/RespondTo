#RespondTo by 4rlenrey

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
import json
from basicFunctions import gettype, get_response_type, addtotypef, match_response_type, add_new_type, respond
import random

FILE = open("data.json", 'r')
DATA = json.load(FILE)

def handleClickType():
    type1 = listOfTypes1.get()
    type2 = listOfTypes2.get()
    if type1 in DATA["Type"] and type2 in DATA["Type"]:
        match_response_type(type1, type2)


def handleClickWord():
    text = inputMessage.get()
    type = listOfcat.get()
    if gettype(text) == type:
        pass
    elif gettype(text) == "unknown" and type != "":
        addtotypef(gettype(text), text, type)

def getResponse():
    rem = reMessage.get()
    typetor = gettype(rem)
    typer = get_response_type(typetor) 
    if typer in DATA["Type"]:
        x = respond(typer)
        print(x)
        relab.configure(text = x)


window = tk.Tk()

responseRow = int(8) #row for response

responseLabel = tk.Label(window, text="GET RESPONSE")
responseLabel.grid(row=responseRow-1, columnspan = 2, sticky="W")

responselab = tk.Label(window, text="Message:")
responselab.grid(column=0, row=responseRow)

reMessage = tk.Entry(window)
reMessage.grid(column=1, row=responseRow)

relab = tk.Label(window, text="Response:")
relab.grid(column=2, row=responseRow)

relab = tk.Label(window, text="")
relab.grid(column=3, row=responseRow)

typeButton = tk.Button(window, text="Enter", command = getResponse, width=20)
typeButton.grid(column=4, row=responseRow)


matchTypeRow = int(6) #row for matching types

matchTypeLabel = tk.Label(window, text="MATCH TYPES")
matchTypeLabel.grid(row=matchTypeRow-1, columnspan = 2, sticky="W")

Type1lab = tk.Label(window, text="Type 1:")
Type1lab.grid(column=0, row=matchTypeRow)

listOfTypes1 = ttk.Combobox(window)
listOfTypes1['values'] = DATA["Type"]
listOfTypes1.grid(column=1, row = matchTypeRow)

Type2lab = tk.Label(window, text="Type 2:")
Type2lab.grid(column=2, row=matchTypeRow)

listOfTypes2 = ttk.Combobox(window)
listOfTypes2['values'] = DATA["Type"]
listOfTypes2.grid(column=3, row = matchTypeRow)

typeButton = tk.Button(window, text="Enter", command = handleClickType, width=20)
typeButton.grid(column=4, row=matchTypeRow)



addMessageRow = int(4) #row for adding message

addMsgLabel = tk.Label(window, text="ADD NEW MESSAGE")
addMsgLabel.grid(row=addMessageRow-1, columnspan = 2, sticky="W")

inMsgLabel = tk.Label(window, text="Message:")
inMsgLabel.grid(column=0, row=addMessageRow)

inputMessage = tk.Entry(window)
inputMessage.grid(column=1, row=addMessageRow)

inMsgLabel = tk.Label(window, text="Type:")
inMsgLabel.grid(column=2, row=addMessageRow)

listOfcat = ttk.Combobox(window)
listOfcat['values'] = DATA["Type"]
listOfcat.grid(column=3, row = addMessageRow)

inMsgButton = tk.Button(window, text="Enter", command = handleClickWord, width=20)
inMsgButton.grid(column=4, row=addMessageRow)


window.geometry("700x300")
window.title("RespondTo")

window.mainloop()
