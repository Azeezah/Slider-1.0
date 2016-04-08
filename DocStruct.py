from tkinter import *
from GET import GET

class document():
    def __init__(self, container, signals):
        self.container = container
        self.signals = signals
        self.history = []
        words = 'SLIDER BROWSER IS AWESOME!!!!'
        Label(self.container, text=words, bg='white', height=30, width=100).pack(fill=BOTH)

    def fetch(self, url):
        self.signals[1]()
        self.history+=[url]
        for sub in self.container.winfo_children():
            sub.destroy()
        x = GET(url)

        scrollbar=Scrollbar(self.container)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.container, wrap=WORD, yscrollcommand=scrollbar.set, bg='white', height=30, width=100)
        textbox.pack(fill=BOTH)
        scrollbar.config(command=textbox.yview)
        textbox.insert(END, x)
        textbox.config(state=DISABLED)
#        Label(self.container, text=x, bg='white', height=30, width=100).pack(fill=BOTH)
        self.signals[2]()

    def back(self):
        if len(self.history) > 1:
            self.history.pop()
            self.fetch(self.history.pop())
        else:
            self.signals[0]()    
        