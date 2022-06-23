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

tabs.add(alarm_tab, text='Alarm')
tabs.add(clock_tab, text='Clock')
tabs.add(timer_tab, text='Timer')
tabs.add(stopwatch_tab, text='Stopwatch')


# Clock components
time_label = Label(root, font = ('calibri', 20))
time_label.pack()
date_label = Label(root, font = ('calibri', 10))
date_label.pack()

# Time function
def time_func():
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    time_label.config(text = time_str)
    date_label.config(text = date_str)
    root.after(1000, time_func)

ticking = True

def on_start():
    global ticking
    ticking = True

def on_stop():
    global ticking
    ticking = False

# Alarm function
def alarm_func():
    main_time = datetime.datetime.now().strftime("%H:%M:%S")
    alarm_time = get_alarm_time_entry.get()
    alarm_hour, alarm_minutes, alarm_seconds = alarm_time.split(':')
    main_hour, main_minutes, main_seconds = main_time.split(':')

    if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and int(alarm_seconds) == int(main_seconds):
        on_stop()
        alarm_status_label.config(text='Time is up')
        get_alarm_time_entry.config(state='normal')
        set_alarm_button.config(state='normal')


    if ticking:
        alarm_status_label.config(text='Alarm Has Started')
        get_alarm_time_entry.config(state='disabled')
        set_alarm_button.config(state='disabled')
    alarm_status_label.after(1000, alarm_func)

# Alarm components
get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15')
get_alarm_time_entry.pack()
alarm_instructions = Label(alarm_tab, font = 'calibri 10', text = 'Enter alarm time. For instance: 10:11:12')
alarm_instructions.pack()
set_alarm_button = Button(alarm_tab, text = 'Set alarm', command=lambda: [on_start(), alarm_func()])
set_alarm_button.pack()
alarm_status_label = Label(alarm_tab, font = 'calibri 10', text = '')
alarm_status_label.pack()


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
