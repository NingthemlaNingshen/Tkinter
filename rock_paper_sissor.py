from tkinter import *
from PIL import Image,ImageTk
from random import randint
window = Tk()
window.title("Rock_Paper_Sissor_Game!")
window.configure(bg="pink")

Image_rock1=ImageTk.PhotoImage(Image.open("rock2.png"))   ##PhotoImage is a function
Image_paper1=ImageTk.PhotoImage(Image.open("paper.jpg"))
Image_scissor1=ImageTk.PhotoImage(Image.open("scissor.jpg"))
Image_rock2=ImageTk.PhotoImage(Image.open("rock.jpg"))
Image_paper2=ImageTk.PhotoImage(Image.open("paper2.jpg"))
Image_scissor2=ImageTk.PhotoImage(Image.open("scissor2.jpg"))

label_player = Label(window,image=Image_scissor1)     
label_player.image=Image_scissor1
label_computer=Label(window,image=Image_scissor2)
label_computer.image=Image_scissor2

label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=4)

computer_score = Label(window,text = 0,font=('arial',20,'bold'),fg="blue")
player_score = Label(window,text = 0,font=('arial',20,'bold'),fg="blue")

computer_score.grid(row = 1,column = 1)
player_score.grid(row = 1,column = 3)

player_indicator=Label(window,font=("arial",30,"bold"),text="PLAYER",bg="orange",fg="white")
computer_indicator=Label(window,font=("arial",30,"bold"),text="COMPUTER",bg="orange",fg="white")

computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

def updateMessage(a):   
    final_msg["text"] = a
def computer_update():
    final=int(computer_score["text"])
    final=final+1
    computer_score["text"]=str(final)
def player_update():
    final=int(player_score["text"])
    final=final+1
    player_score["text"]=str(final)
def winner_check(p,c):
    if p==c:
        updateMessage("it's a tie")
    elif p=="rock":
        if c=="paper":
            updateMessage("compueter wins!!")
            computer_update()
        else:
            updateMessage("players wins!!!")
            player_update()
    elif p=="paper":
        if c=="scissor":
            updateMessage("computer wins")
            computer_update()
        else:
            updateMessage("players wins")
            player_update()
    elif p=="scissor":
        if c=="rock":
            updateMessage("computer wins")
            computer_update()
        else:
            updateMessage("players wins")
            player_update()
    else:
        pass
to_select=["rock","paper","scissor"]

def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_comp.configure(image=Image_rock2)
    elif choice_computer == "paper":
        label_comp.configure(image=Image_paper2)
    else:
        label_comp.configure(image=Image_scissor2)
    if a == "rock":
        label_player.configure(image=Image_rock1)
    elif a == "paper":
        label_player.configure(image=Image_paper1)
    else:
        label_player.configure(image=Image_scissor1)
    winner_check(a, choice_computer)



final_msg=Label(window,font=("arial",30,"bold"),bg="red",fg="white")
final_msg.grid(row=3,column=2)

##creating buttons

button_rock=Button(window,width=5,height=5,text="ROCK",font=("arial",10,"bold"),bg="white",fg="black",command=lambda:choice_update("rock")).grid(row=2,column=1)
button_paper=Button(window,width=5,height=5,text="PAPER",font=("arial",10,"bold"),bg="white",fg="black",command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor=Button(window,width=5,height=5,text="SCISSOR",font=("arial",10,"bold"),bg="white",fg="black",command=lambda:choice_update("scissor")).grid(row=2,column=3)


window. mainloop()
