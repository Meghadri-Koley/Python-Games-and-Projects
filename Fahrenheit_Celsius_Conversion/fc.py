from tkinter import *

def cal(event):
	global swap, label1, label2, label3, label4, label5
	global string1, string2, screen1, screen2

	if(swap%2==0):
		temp=float(screen1.get())
		ans=round((temp-32)*5/9, 5)
		string2.set(ans)
		screen2.update()

	else:
		temp=float(screen1.get())
		ans=round((temp*9/5)+32, 5)
		string2.set(ans)
		screen2.update()

def swp(event):
	global swap, label1, label2, label3, label4, label5
	swap+=1

	string1.set("")
	string2.set("")
	screen1.update()
	screen2.update()


	if(swap%2==0):
		label1.config(text="Fahrenheit to Celsius Conversion")
		label2.config(text="Fahrenheit: ")
		label3.config(text=" °F")
		label4.config(text="Celsius: ")
		label5.config(text=" °C")
	else:
		label1.config(text="Celsius to Fahrenheit Conversion")
		label2.config(text="Celsius: ")
		label3.config(text=" °C")
		label4.config(text="Fahrenheit: ")
		label5.config(text=" °F")
	
#initialize
root=Tk()

#background colour
body="#9EC5AB"
button="#493E31"
text="#255651"

#text colour
headText="#022704"
titleText="#023B1C"
buttonText="#023B1C"
entryText="#BFD9C8"

#title
root.title("Fahrenheit - Celsius Conversion")

#background
root['background']=body

#size
root.geometry("600x470")
root.maxsize(600, 470)
root.minsize(600, 470)

#frame1
frame1=Frame(root, bg=body)
frame1.pack(fill="x", padx=50, pady=30)

label1=Label(frame1, text="Fahrenheit to Celsius Conversion", bg=body, fg=headText, justify=CENTER, font="comicsansm 32 bold")
label1.pack()

#frame2
frame2=Frame(root, bg=body)
frame2.pack(fill="x", padx=50, pady=30)

label2=Label(frame2, text="Fahrenheit: ", bg=body, fg=titleText, justify=CENTER, font="comicsansm 26 bold")
label2.pack(side=LEFT)

string1=StringVar()
string1.set("")
screen1=Entry(frame2, textvar=string1, width=10, font="comicsansm 35 bold", bg=text, borderwidth=2, fg=entryText)
screen1.pack(side=LEFT, fill="x")

label3=Label(frame2, text=" °F", bg=body, fg=titleText, justify=CENTER, font="comicsansm 26 bold")
label3.pack(side=LEFT)

#frame3
frame3=Frame(root, bg=body)
frame3.pack(fill="x", padx=50, pady=30)

label4=Label(frame3, text="Celsius: ", bg=body, fg=titleText, justify=CENTER, font="comicsansm 26 bold")
label4.pack(side=LEFT)

string2=StringVar()
string2.set("")
screen2=Entry(frame3, textvar=string2, width=10, font="comicsansm 35 bold", bg=text, borderwidth=2, fg=entryText)
screen2.pack(side=LEFT, fill="x")

label5=Label(frame3, text=" °C", bg=body, fg=titleText, justify=CENTER, font="comicsansm 26 bold")
label5.pack(side=LEFT)

#frame4
frame4=Frame(root, bg=body)
frame4.pack(fill="x", pady=30)

swap=0

button1=Button(frame4, text="Calculate", fg=buttonText, highlightthickness=6, highlightbackground=button, font="comicsansm 30 bold", padx=14, pady=10, relief="groove")
button1.grid(row=0, column=3, padx= 50)
button1.bind("<Button-1>",cal)

button2=Button(frame4, text="Swap", fg=buttonText, highlightthickness=6, highlightbackground=button, font="comicsansm 30 bold", padx=14, pady=10, relief="groove")
button2.grid(row=0, column=5, padx= 50)
button2.bind("<Button-1>",swp)

root.mainloop()