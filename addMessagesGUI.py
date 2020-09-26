#RespondTo by 4rlenrey

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
import json
from basicFunctions import gettype, get_response_type, addtotypef, match_response_type, add_new_type, respond
import random

def get_type_list():
    FILE = open("data.json", 'r')
    DATA = json.load(FILE)
    FILE.close()
    return DATA["Type"]

class addMessagesGUI:
    def handleClickType(self):
        type1 = self.listOfTypes1.get()
        type2 = self.listOfTypes2.get()
        if type1 in get_type_list() and type2 in get_type_list():
            match_response_type(type1, type2)

    def handleClickWord(self):
        text = self.inputMessage.get()
        type = self.listOfcat.get()
        if gettype(text) == type:
            pass
        elif gettype(text) == "unknown" and type != "":
            addtotypef(gettype(text), text, type)

    def getResponse(self):
        rem = self.reMessage.get()
        typetor = gettype(rem)
        typer = get_response_type(typetor) 
        if typer != "unknown":
            x = respond(typetor)
            self.relab.configure(text = x)

    def __init__(self, master):
        self.master = master
        master.title("RespondTo")
        master.geometry("700x300")

        responseRow = int(8) #row for response
        self.responseLabel = tk.Label(master, text="GET RESPONSE")
        self.responseLabel.grid(row=responseRow-1, columnspan = 2, sticky="W")
        self.responselab = tk.Label(master, text="Message:")
        self.responselab.grid(column=0, row=responseRow)
        self.reMessage = tk.Entry(master)
        self.reMessage.grid(column=1, row=responseRow)
        self.relab = tk.Label(master, text="Response:")
        self.relab.grid(column=2, row=responseRow)
        self.relab = tk.Label(master, text="")
        self.relab.grid(column=3, row=responseRow)
        self.typeButton = tk.Button(master, text="Enter", command = self.getResponse, width=20)
        self.typeButton.grid(column=4, row=responseRow)


        matchTypeRow = int(6) #row for matching types
        self.matchTypeLabel = tk.Label(master, text="MATCH TYPES")
        self.matchTypeLabel.grid(row=matchTypeRow-1, columnspan = 2, sticky="W")
        self.Type1lab = tk.Label(master, text="Type 1:")
        self.Type1lab.grid(column=0, row=matchTypeRow)
        self.listOfTypes1 = ttk.Combobox(master)
        self.listOfTypes1['values'] = get_type_list()
        self.listOfTypes1.grid(column=1, row = matchTypeRow)
        self.Type2lab = tk.Label(master, text="Type 2:")
        self.Type2lab.grid(column=2, row=matchTypeRow)
        self.listOfTypes2 = ttk.Combobox(master)
        self.listOfTypes2['values'] = get_type_list()
        self.listOfTypes2.grid(column=3, row = matchTypeRow)
        self.typeButton = tk.Button(master, text="Enter", command = self.handleClickType, width=20)
        self.typeButton.grid(column=4, row=matchTypeRow)

        addMessageRow = int(4) #row for adding message
        self.addMsgLabel = tk.Label(master, text="ADD NEW MESSAGE")
        self.addMsgLabel.grid(row=addMessageRow-1, columnspan = 2, sticky="W")
        self.inMsgLabel = tk.Label(master, text="Message:")
        self.inMsgLabel.grid(column=0, row=addMessageRow)
        self.inputMessage = tk.Entry(master)
        self.inputMessage.grid(column=1, row=addMessageRow)
        self.inMsgLabel = tk.Label(master, text="Type:")
        self.inMsgLabel.grid(column=2, row=addMessageRow)
        self.listOfcat = ttk.Combobox(master)
        self.listOfcat['values'] = get_type_list()
        self.listOfcat.grid(column=3, row = addMessageRow)
        self.inMsgButton = tk.Button(master, text="Enter", command = self.handleClickWord, width=20)
        self.inMsgButton.grid(column=4, row=addMessageRow)  

ROOT = tk.Tk()
GUI = addMessagesGUI(ROOT)
ROOT.mainloop()
