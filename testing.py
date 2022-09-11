from tkinter import *
root =Tk()
e= Entry(root,width=50,bg="purple",fg="white")
e.pack()
def click():
    mylabel=Label(root,text="Look I click the button")
    mylabel.pack()
mybutton=Button(root,text="Click me",command=click())
mybutton.pack()
root.mainloop()