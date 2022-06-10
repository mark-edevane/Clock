from tkinter import *
from time import strftime
root = Tk()

def time():
    string = strftime('%H:%M:%S')
    mark.config(text = string)
    mark.after(1000, time)

mark = Label(root,font = ('calibri', 40))
mark.pack(anchor = 'center')

time()

mainloop()
