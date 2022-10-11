from tkinter import *
from PIL import ImageTk, Image
import random
import os

def result(comp, you):
	if you == comp:
		return -1

	elif you == "Stone":
		if comp == "Scissors":
			return 1
		else:
			return 0

	elif you == "Paper":
		if comp == "Stone":
			return 1
		else:
			return 0

	elif you == "Scissors":
		if comp == "Paper":
			return 1
		else:
			return 0

def democlick(event):
	pass

def startgame(event):
	global button1, button2, button3, button4, userScore, compScore

	button1.config(state="normal")
	button1.bind("<Button-1>",click)
	
	button2.config(state="normal")
	button2.bind("<Button-1>",click)
	
	button3.config(state="normal")
	button3.bind("<Button-1>",click)

	button4.config(state="disabled")
	button4.bind("<Button-1>",democlick)

	label6.config(text="Are You Ready?")
	image1=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/You.png")
	image1=image1.resize((200, 200), Image.ANTIALIAS)
	image1=ImageTk.PhotoImage(image1)
	imagelabel1.config(image=image1)
	imagelabel1.image = image1
	
	label7.config(text="Computer is Ready!!!")
	image2=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Computer.png")
	image2=image2.resize((200, 200), Image.ANTIALIAS)
	image2=ImageTk.PhotoImage(image2)
	imagelabel2.config(image=image2)
	imagelabel2.image = image2

	userScore, compScore = 0, 0
	screen1.config(text=str(userScore))
	screen2.config(text=str(compScore))
	resultScreen.config(text="Let's start the Game!!!")


def click(event):
	global screen1, screen2, userScore, compScore, label6, label7, resultScreen
	global imagelabel1, imagelabel2, button1, button2, button3, button4

	you = event.widget.cget("text")
	
	rand = (random.randint(5,10**5))%3
	comp = ""
	if rand==0:
		comp = "Stone"
		image2=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Stone.png")
	elif rand==1:
		comp = "Paper"
		image2=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Paper.png")
	else:
		comp = "Scissors"
		image2=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Scissors.png")
	
	if you=="Stone":
		image1=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Stone.png")
	elif you=="Paper":
		image1=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Paper.png")
	else:
		image1=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Scissors.png")

	label6.config(text="You played " + str(you))
	image1=image1.resize((200, 200), Image.ANTIALIAS)
	image1=ImageTk.PhotoImage(image1)
	imagelabel1.config(image=image1)
	imagelabel1.image = image1
	
	label7.config(text="Computer played " + str(comp))
	image2=image2.resize((200, 200), Image.ANTIALIAS)
	image2=ImageTk.PhotoImage(image2)
	imagelabel2.config(image=image2)
	imagelabel2.image = image2

	res = result(comp, you)

	if res==1:
		userScore += 1
		screen1.config(text=str(userScore))
		resultScreen.config(text="You win!!!")
	if res==0:
		compScore += 1
		screen2.config(text=str(compScore))
		resultScreen.config(text="Computer wins!!!")
	if res==-1:
		resultScreen.config(text="It's a Draw!!!")

	if userScore==10:
		resultScreen.config(text="You won over Computer by " + str(abs(userScore-compScore)) +"!!!")
		
		button1.config(state="disabled")
		button1.bind("<Button-1>",democlick)
		button2.config(state="disabled")
		button2.bind("<Button-1>",democlick)
		button3.config(state="disabled")
		button3.bind("<Button-1>",democlick)
		button4.config(state="normal")
		button4.bind("<Button-1>",startgame)

	if compScore==10:
		resultScreen.config(text="Computer won over You by " + str(abs(userScore-compScore)) +"!!!")
		
		button1.config(state="disabled")
		button1.bind("<Button-1>",democlick)
		button2.config(state="disabled")
		button2.bind("<Button-1>",democlick)
		button3.config(state="disabled")
		button3.bind("<Button-1>",democlick)
		button4.config(state="normal")
		button4.bind("<Button-1>",startgame)
	
#initialize
root = Tk()

#background colour
body="#95C5DA"
title="#172A3A"
score1="#058068"
score2="#004346"

#text colour
headText="#9EFAE0"
bodyText="#0C151D"
buttonText="#0E191A"
scoreText1="white"
scoreText2="white"

#title
root.title("Stone, Paper, Scissors")
#background
root['background']=body
#size
root.geometry("1200x585")
root.minsize(1200,585)
root.maxsize(1200,585)

#frame1
frame1=Frame(root, bg=title)
frame1.pack(fill="x")
label1=Label(frame1, text="Rock, Paper, Scissors", bg=title, fg=headText, justify=CENTER, font="comicsansm 26 bold")
label1.pack()
label2=Label(frame1, text="First to 10 is the champion", bg=title, fg=headText, justify=CENTER, font="comicsansm 20")
label2.pack(pady=3)

#frame2
userScore, compScore = 0, 0
frame2=Frame(root, bg=score1, bd=6, relief="sunken")
frame2.pack(fill="x")
#player_screen
screen1=Label(frame2, text="0", bg=score2, fg=scoreText2, font="comicsansm 35", width=3, bd=6, relief="sunken")
screen1.pack(side=LEFT)
label3=Label(frame2, text="You", bg=score1, fg=scoreText1, font="comicsansm 20 bold")
label3.pack(side=LEFT, padx=15)
#computer_screen
screen2=Label(frame2, text="0", bg=score2, fg=scoreText2, font="comicsansm 35", width=3, bd=6, relief="sunken")
screen2.pack(side=RIGHT)
label4=Label(frame2, text="Computer", bg=score1, fg=scoreText1, font="comicsansm 20 bold")
label4.pack(side=RIGHT, padx=15)

#frame3
frame3=Frame(root, bg=body)
frame3.pack(fill="x")
label5=Label(frame3, text="Stone, Paper, or Scissors?", bg=body, fg=bodyText, justify=CENTER, font="comicsansm 30 bold")
label5.pack(pady=20)

#frame4
frame4=Frame(root, bg=body)
frame4.pack()
#button1
button1=Button(frame4, text="Stone", state="disabled", fg=buttonText, highlightthickness=6, highlightbackground=title, font="comicsansm 30 bold", padx=14, pady=10, relief="groove")
button1.grid(row=0, column=1, padx= 50)
button1.bind("<Button-1>",democlick)
#button2
button2=Button(frame4, text="Paper", state="disabled", fg=buttonText, highlightthickness=6, highlightbackground=title, font="comicsansm 30 bold", padx=14, pady=10, relief="groove")
button2.grid(row=0, column=2, padx= 50)
button2.bind("<Button-1>",democlick)
#button3
button3=Button(frame4, text="Scissors", state="disabled", fg=buttonText, highlightthickness=6, highlightbackground=title, font="comicsansm 30 bold", padx=14, pady=10, relief="groove")
button3.grid(row=0, column=3, padx= 50)
button3.bind("<Button-1>",democlick)

#frame5
frame5=Frame(root, bg=body)
frame5.pack(fill="x")
label6=Label(frame5, text="Are You Ready?", bg=body, fg=bodyText, font="comicsansm 20 bold")
label6.pack(side=LEFT, padx=40, pady=20)
label7=Label(frame5, text="Computer is Ready!!!", bg=body, fg=bodyText, font="comicsansm 20 bold")
label7.pack(side=RIGHT, padx=40, pady=20)

#frame6
frame6=Frame(root, bg=body)
frame6.pack(fill="x")
#image1
image1=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/You.png")
image1=image1.resize((200, 200), Image.ANTIALIAS)
image1=ImageTk.PhotoImage(image1)
imagelabel1=Label(image=image1, bg=body)
imagelabel1.pack(side=LEFT, padx=40)
#image2 
image2=Image.open("/Users/arghyabandyopadhyay/Desktop/batcave/Python-Games-and-Projects/Stone_Paper_Scissors_GUI/Computer.png")
image2=image2.resize((200, 200), Image.ANTIALIAS)
image2=ImageTk.PhotoImage(image2)
imagelabel2=Label(image=image2, bg=body)
imagelabel2.pack(side=RIGHT, padx=40)

#frame
frame7=Frame(root, bg=body)
frame7.pack(fill="x")
resultScreen=Label(frame7, text="Let's start the Game!!!", bg=body, fg=bodyText, font="comicsansm 30 bold")
resultScreen.pack(fill="x", padx=40)

#frame8
frame8=Frame(root, bg=body)
frame8.pack(fill="x", side=BOTTOM)
#button4
button4=Button(frame8, text="Start Game", fg=buttonText, highlightthickness=6, highlightbackground=title, font="comicsansm 30 bold", padx=14, pady=10, relief="sunken")
button4.pack(pady=20)
button4.bind("<Button-1>",startgame)

root.mainloop()