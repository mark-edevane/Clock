from tkinter import ttk
from tkinter import *
import time
import datetime

root = Tk()
root.title('Clock')

# Tabs
tabs = ttk.Notebook(root)
tabs.pack()

alarm_tab = ttk.Frame(tabs)
timer_tab = ttk.Frame(tabs)
stopwatch_tab = ttk.Frame(tabs)

tabs.add(stopwatch_tab, text='Stopwatch')
tabs.add(timer_tab, text='Timer')
tabs.add(alarm_tab, text='Alarm and Clock')


# Clock components within alarm tab
clock_label = Label(alarm_tab, font = ('calibri', 20))
clock_label.pack()
date_label = Label(alarm_tab, font = ('calibri', 10))
date_label.pack()


# Clock function
def clock_func():
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    clock_label.config(text = time_str)
    date_label.config(text = date_str)
    root.after(1000, clock_func)


# Variable and functions to start and stop the time
running = False

def start():
    global running
    running = True

def stop():
    global running
    running = False


# Alarm function
def alarm_func():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    alarm_time = get_alarm_time_entry.get()
    alarm_hour, alarm_minutes, alarm_seconds = alarm_time.split(':')
    current_hour, current_minutes, current_seconds = current_time.split(':')

    if int(alarm_hour) == int(current_hour) and int(alarm_minutes) == int(current_minutes) and int(alarm_seconds) == int(current_seconds):
        stop()
        alarm_status_label.config(text='Time is up')
        get_alarm_time_entry.config(state='normal')
        set_alarm_button.config(state='normal')

    if running:
        alarm_status_label.config(text='Alarm Has Started')
        get_alarm_time_entry.config(state='disabled')
        set_alarm_button.config(state='disabled')
    alarm_status_label.after(1000, alarm_func)

# Alarm components
get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15')
get_alarm_time_entry.pack()
alarm_instructions = Label(alarm_tab, font = 'calibri 10', text = 'Enter time as HH:MM:SS')
alarm_instructions.pack()
set_alarm_button = Button(alarm_tab, text = 'Set alarm', command=lambda: [start(), alarm_func()])
set_alarm_button.pack()
alarm_status_label = Label(alarm_tab, font = 'calibri 10', text = '')
alarm_status_label.pack()


# Stopwatch variables
seconds, minutes, hours = 0, 0, 0

# Stopwatch functions
def stopwatch_update():
    global seconds, minutes, hours
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    stopwatch_label.config(text = hours_string + ':' + minutes_string + ':' + seconds_string)
    if running:
        global stopwatch_after
        stopwatch_after = stopwatch_label.after(1000, stopwatch_update)

def stopwatch_func(command):
    if command == 'start':
        start()
        stopwatch_start.config(state='disabled')
        stopwatch_stop.config(state='normal')
        stopwatch_reset.config(state='normal')
        stopwatch_update()

    if command == 'stop':
        stop()
        stopwatch_start.config(state='normal')
        stopwatch_stop.config(state='disabled')
        stopwatch_label.after_cancel(stopwatch_after)

    if command == 'reset':
        stop()
        stopwatch_start.config(state='normal')
        stopwatch_stop.config(state='disabled')
        global hours, minutes, seconds
        hours, minutes, seconds = 0, 0, 0
        stopwatch_label.config(text='00:00:00')
        stopwatch_label.after_cancel(stopwatch_after)


# Stopwatch components
stopwatch_label = Label(stopwatch_tab, font='calibri 20', text='Stopwatch')
stopwatch_label.pack()
stopwatch_start = Button(stopwatch_tab, text='Start', state = 'normal', command=lambda: stopwatch_func('start'))
stopwatch_start.pack()
stopwatch_stop = Button(stopwatch_tab, text='Stop', state='disabled',command=lambda:stopwatch_func('stop'))
stopwatch_stop.pack()
stopwatch_reset = Button(stopwatch_tab, text='Reset', state='disabled', command=lambda:stopwatch_func('reset'))
stopwatch_reset.pack()


# Timer functions
tmr_hr, tmr_min, tmr_sec = 0, 0, 0

def timer_update():
    global tmr_hr, tmr_min, tmr_sec
    tmr_sec -= 1
    if tmr_sec == -1:
            tmr_min -= 1
            tmr_sec = 59
    if tmr_min == -1:
        tmr_hr -= 1
        tmr_min = 59

    hours_string = f'{tmr_hr}' if tmr_hr > 9 else f'0{tmr_hr}'
    minutes_string = f'{tmr_min}' if tmr_min > 9 else f'0{tmr_min}'
    seconds_string = f'{tmr_sec}' if tmr_sec > 9 else f'0{tmr_sec}'

    timer_label.config(text = hours_string + ':' + minutes_string + ':' + seconds_string)
    if running:
        global timer_after
        timer_after = timer_label.after(1000, timer_update)
        if tmr_hr == 0 and tmr_min == 0 and tmr_sec == 0:
            stop()
            timer_label.config(text = "Time's up")
            timer_label.after_cancel(timer_after)
            timer_entry.config(state='normal')
            timer_start.config(state='normal')

def timer_func(command):
    global tmr_hr, tmr_min, tmr_sec
    if command == 'start':      
        time = timer_entry.get()
        tmr_hr, tmr_min, tmr_sec = map(int, time.split(':'))
        start()
        timer_update()
        timer_start.config(state='disabled')
        timer_stop.config(state='normal')
        timer_reset.config(state='normal')
        timer_entry.config(state='disabled')
        
    if command == 'continue':
        start()
        timer_update()
        timer_start.config(state='disabled')
        timer_stop.config(state='normal')
        timer_reset.config(state='normal')
        timer_continue.config(state='disabled')
        
    if command == 'stop':
        stop()
        timer_start.config(state='disabled')
        timer_stop.config(state='disabled')
        timer_continue.config(state='normal')
        timer_label.after_cancel(timer_after)
        
    if command == 'reset':
        stop()
        timer_label.after_cancel(timer_after)
        timer_start.config(state='normal')
        timer_stop.config(state='disabled')
        timer_continue.config(state='disabled')
        timer_reset.config(state='disabled')
        tmr_hr, tmr_min, tmr_sec = 0, 0, 0
        timer_label.config(text='00:00:00')
        timer_entry.config(state='normal')

# Timer components
timer_label = Label(timer_tab, font = 'calibri 15', text = 'Enter time as HH:MM:SS')
timer_label.pack()
timer_entry = Entry(timer_tab, font = 'calibri 15')
timer_entry.pack()
timer_start = Button(timer_tab, text='start', state = 'normal', command = lambda: timer_func('start'))
timer_start.pack()
timer_continue = Button(timer_tab, text='continue', state = 'disabled', command = lambda: timer_func('continue'))
timer_continue.pack()
timer_stop = Button(timer_tab, text ='stop', state ='disabled', command = lambda: timer_func('stop'))
timer_stop.pack()
timer_reset = Button(timer_tab, text ='reset', state ='disabled', command = lambda: timer_func('reset'))
timer_reset.pack()


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

clock_func()
mainloop()