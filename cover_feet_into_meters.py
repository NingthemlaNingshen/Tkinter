# from tkinter import *
# from tkinter import ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()





###Basic example       ##since Tkinter is used in python 2 in latest version we won't get the module so there will be error
##Import the tkinter library
# from Tkinter import*
# ## Cereate an instance of tkinter frame
# win=Tk()
# ## Set the geometry
# win.geometry("650*200")
# win.mainloop()


##Example why we use from tkinter import* or import tkinter as tk

from tkinter import*
# import tkinter as tk
win= Tk()
win.geometry("750x250")
entry= Text(win, width= 24)
entry.insert(INSERT,"Hello World!")
entry.tag_add("start","1.0","end")
entry.tag_configure("start", background="blue", foreground= "white")
entry.pack()
win.mainloop()

