from tkinter import *
from tkinter import ttk

window = Tk()
window.title('The progressbar')
window.geometry('300x300')

pro = DoubleVar(value=0)

progress = ttk.Progressbar(
    master=window,
    variable=pro,
    maximum=30,
    orient='horizontal',
    mode='determinate',
    length=300
)
progress.pack(pady=120)
progress.start(70)

window.mainloop()