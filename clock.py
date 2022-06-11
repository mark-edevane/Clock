from tkinter import *

# ttk module stands for "Themed Tkinter". Designed to give widgets  a better and more modern look
from tkinter import ttk
from time import strftime

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


# A way to create a menu
'''
menubar  = Menu(root)
root.config(menu=menubar)
menubar.add_command(label='Timer', command=lambda: print("Your time's up"))
menubar.add_command(label='Stopwatch', command=lambda: print("The clock's ticking"))
'''
def time():
    string = strftime('%H:%M:%S')
    clock.config(text = string)
    clock.after(1000, time)

clock = Label(root,font = ('calibri', 40))
clock.pack()

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
