import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
import json
from basicFunctions import gettype, get_response_type, addtotypef, match_response_type, add_new_type

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

window = tk.Tk()

matchTypeRow = int(6) #row for adding message

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


window.geometry("700x500")
window.title("RespondTo")

window.mainloop()
