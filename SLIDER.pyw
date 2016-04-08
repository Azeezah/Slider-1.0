'''
JAC:
    replace urlbar with tkinter.ttk.Combobox
    use tkinter.ttk.Notebook for tabs
'''

from os.path import dirname, realpath
from DocStruct import document
from tkinter import *

#I'm not using os.path.abspath because it uses cwd.
dir = dirname(realpath(__file__))+'\\'
doneicon = dir+"Slider3.ico"
waiticon = dir+"Slider5.ico"
erroricon = dir+"Slider4.ico"

root = Tk()
root.wm_title("Slider")
root.wm_iconbitmap(doneicon)

signals = (
    lambda:root.wm_iconbitmap(erroricon),
    lambda:root.wm_iconbitmap(waiticon), 
    lambda:root.wm_iconbitmap(doneicon)
    )

#root.geometry("170x200+30+30")

top = Frame(root, relief=SUNKEN, bg='yellow', width=100)
top.pack(side=TOP, fill=X)

content = Frame(root, bg='orange', width=100)
content.pack(fill=BOTH)

#progressbar=Label(root, text='fetching...', bg='blue')
#progressbar.pack(fill=X, side=BOTTOM)

DOM = document(content, signals)

url = StringVar()

#urlbar:
Entry(top, bg='green', fg='white', textvariable = url, width=80).pack(fill=X, padx=5, side=LEFT)
#Fetch doc:
Button(top, text='Fetch', bg='orange', fg='white', command=lambda:DOM.fetch(url.get())).pack(padx=5, side=RIGHT)
#Back:
Button(top, text='Back', bg='orange', fg='white', command=DOM.back).pack(padx=5, side=RIGHT)

mainloop()








'''
title = Label(content, text=DOM.title, bg='green', fg='white')
red = Label(content, text="red\nand\npinkish", bg='blue', fg='white')
blue = Label(content, text="blue", bg='red', fg='white', relief=RIDGE)
green = Label(content, text="green", bg='green', fg='black', relief=SUNKEN)

#Widget Attribute: 'relief' in ['RIDGE', 'SUNKEN'] 
#Method: grid(int row, int column), where row and col increment from 0
#Method: widget.place(int x, int y, int width, int height)
title.pack(fill=X, side=TOP)
red.pack(padx=5, pady=10, side=LEFT)
blue.pack(padx=5, pady=10, side=RIGHT)
green.pack(padx=5, pady=10)

import random
channels = [random.randrange(256) for _ in range(3)]
brightness = int(round(0.29*channels[0])+0.587*channels[1]+0.114*channels[2])
fontcolor = 'white' if brightness < 120 else 'black'
hex = "%02x%02x%02x" % tuple(channels)
color = '#'+hex
'''