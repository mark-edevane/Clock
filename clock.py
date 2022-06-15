# ttk module stands for "Themed Tkinter". Designed to give widgets a better and more modern look
from tkinter import ttk

from tkinter import *
from time import strftime
import datetime

root = Tk()
root.title('Clock')

# Tabs
tabs = ttk.Notebook(root)
tabs.pack()

clock_tab = ttk.Frame(tabs)
alarm_tab = ttk.Frame(tabs)
timer_tab = ttk.Frame(tabs)
stopwatch_tab = ttk.Frame(tabs)

tabs.add(clock_tab, text='Clock')
tabs.add(alarm_tab, text='Alarm')
tabs.add(timer_tab, text='Timer')
tabs.add(stopwatch_tab, text='Stopwatch')


# Clock components
time_label = Label(root, font = ('calibri', 20))
time_label.pack()
date_label = Label(root, font = ('calibri', 15))
date_label.pack()

# Time function
def time_func():
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    time_label.config(text = time_str)
    date_label.config(text = date_str)
    root.after(1000, time_func)


# Alarm function
# def alarm_func():


# Alarm components
alarm_time = Entry(alarm_tab, font = 'calibri 15')
alarm_time.pack()
alarm_instructions = Label(alarm_tab, font = 'calibri 10', text = 'Enter alarm time. E.g. 15:55')
alarm_instructions.pack()
alarm_button = Button(alarm_tab, text = 'Set alarm'''', command = alarm_func''')
alarm_button.pack()
alarm_status = Label(alarm_tab, font = 'calibri 10', text = 'Here will be something')
alarm_status.pack()


# Exit button
exit_btn = ttk.Button(
    root,
    text = 'Exit',
    command = lambda: root.quit()
        )
exit_btn.pack(fill = 'x')

# Pressing Enter triggers the exit
def exit_func(event):
    root.quit()
root.bind('<Return>', exit_func)

time_func()
mainloop()
