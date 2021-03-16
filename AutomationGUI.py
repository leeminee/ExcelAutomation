from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Automation GUI Test")

startDate, endDate = StringVar(), StringVar()

ttk.Label(window, text="startDate : ").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(window, text="endDate : ").grid(row=1, column=0, padx=10, pady=10)
ttk.Entry(window, textvariable=startDate).grid(row=0, column=1, padx=10, pady=10)
ttk.Entry(window, textvariable=endDate).grid(row=1, column=1, padx=10, pady=10)
ttk.Button(window, text="Excel Download").grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
