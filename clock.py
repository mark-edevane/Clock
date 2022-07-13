from tkinter import ttk
from tkinter import *
import time
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

tabs.add(timer_tab, text='Timer')
tabs.add(stopwatch_tab, text='Stopwatch')
tabs.add(alarm_tab, text='Alarm')
tabs.add(clock_tab, text='Clock')


# Clock components
time_label = Label(clock_tab, font = ('calibri', 20))
time_label.pack()
date_label = Label(clock_tab, font = ('calibri', 10))
date_label.pack()

# Clock function
def time_func():
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    time_label.config(text = time_str)
    date_label.config(text = date_str)
    root.after(1000, time_func)

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
alarm_instructions = Label(alarm_tab, font = 'calibri 10', text = 'Enter alarm time. For instance: 10:11:12')
alarm_instructions.pack()
set_alarm_button = Button(alarm_tab, text = 'Set alarm', command=lambda: [start(), alarm_func()])
set_alarm_button.pack()
alarm_status_label = Label(alarm_tab, font = 'calibri 10', text = '')
alarm_status_label.pack()




# Stopwatch variables
seconds = 0
minutes = 0
hours = 0

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

t_seconds = 0
t_minutes = 0
t_hours = 0

def timer_update():
    global t_hours, t_minutes, t_seconds
    t_seconds -= 1
    if t_seconds == -1:
            t_minutes -= 1
            t_seconds = 59
    if t_minutes == -1:
        t_hours -= 1
        t_minutes = 59

    hours_string = f'{t_hours}' if t_hours > 9 else f'0{t_hours}'
    minutes_string = f'{t_minutes}' if t_minutes > 9 else f'0{t_minutes}'
    seconds_string = f'{t_seconds}' if t_seconds > 9 else f'0{t_seconds}'

    timer_label.config(text = hours_string + ':' + minutes_string + ':' + seconds_string)
    if running:
        global timer_after
        timer_after = timer_label.after(1000, timer_update)
        if t_hours == 0 and t_minutes == 0 and t_seconds == 0:
            stop()
            timer_label.config(text = "Time's up")
            timer_label.after_cancel(timer_after)

def timer_func():
    # stop()
    global t_hours, t_minutes, t_seconds
    # t_hours, t_minutes, t_seconds =  0, 0, 0
    time = timer_entry.get()
    t_hours, t_minutes, t_seconds = map(int, time.split(':'))
    start()

    timer_update()


# Timer components
timer_label = Label(timer_tab, font = 'calibri 15', text = 'Enter time to count down in format 00:01:30')
timer_label.pack()
timer_entry = Entry(timer_tab, font = 'calibri 15')
timer_entry.pack()
timer_start = Button(timer_tab, text='Start', state = 'normal', command = timer_func)
timer_start.pack()
timer_stop = Button(timer_tab, text ='Stop', state ='disabled', command = lambda: timer_buttons_func('stop'))
timer_stop.pack()
timer_reset = Button(timer_tab, text ='Reset', state ='disabled', command = lambda: timer_buttons_func('reset'))
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

time_func()
mainloop()