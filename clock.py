from tkinter import *

# ttk module stands for "Themed Tkinter". Designed to give widgets  a better and more modern look
from tkinter import ttk
from time import strftime
import datetime

root = Tk()
root.title('Clock')

tabs = ttk.Notebook(root)
tabs.pack()

clock_tab = ttk.Frame(tabs)
timer_tab = ttk.Frame(tabs)
stopwatch_tab = ttk.Frame(tabs)
alarm_tab = ttk.Frame(tabs)
international_time_tab = ttk.Frame(tabs)
tabs.add(clock_tab, text='Clock')
tabs.add(timer_tab, text='Timer')
tabs.add(stopwatch_tab, text='Stopwatch')
tabs.add(alarm_tab, text='Alarm')
tabs.add(international_time_tab, text='International time')

def time():
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    time_label.config(text = time_str)
    time_label.after(1000, time)
    date_label.config(text = date_str)
    date_label.after(1000, time)

time_label = Label(root,font = ('calibri', 20))
time_label.pack()
date_label = Label(root,font = ('calibri', 15))
date_label.pack()

exit_btn = ttk.Button(
    root,
    text = 'Exit',
    command = lambda: root.quit()
        )
exit_btn.pack(fill = 'x')

def exit_func(event):
    root.quit()
root.bind('<Return>', exit_func)

time()
mainloop()
