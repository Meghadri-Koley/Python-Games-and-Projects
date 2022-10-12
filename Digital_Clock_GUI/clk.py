from tkinter import *
from threading import *
import subprocess
import datetime
import time

screenWidth=520
screenHeight=300
canvasHeight=260

screenColour="#DA9F93"
textColour="#2C0703"

buttonColour="#720719"
buttonTextColour="#B6465F"

entryColour="#EBD4CB"
entryTextColour="#890620"

soundTrack="/Users/arghyabandyopadhyay/Desktop/Python - Projects/Clock/alarm.wav"


class MainFrame(object):
	_root=Tk()
	_frame=Frame(_root,bg=screenColour)
	_canvas=Canvas(_root,width=screenWidth,height=canvasHeight,bg=screenColour)

	_count=0

	def __init__(self):
		self._root.title("Digital Clock")
		self._root['background']=screenColour
		self._root.maxsize(screenWidth,screenHeight)
		self._root.minsize(screenWidth,screenHeight)
		self._frame.pack(pady=10,fill=X)
		self._canvas.pack(expand=YES,fill=BOTH)

		self.addElements()

	def addElements(self):
		button1=Button(self._frame, text="Alarm", fg=buttonTextColour, highlightthickness=2, highlightbackground=buttonColour, font="comicsansm 10 bold", padx=5, pady=5, relief="sunken")
		button1.grid(row=0, column=1, padx= 20)
		button1.bind("<Button-1>", self.clickAlarm)

		button2=Button(self._frame, text="Time Clock", fg=buttonTextColour, highlightthickness=2, highlightbackground=buttonColour, font="comicsansm 10 bold", padx=5, pady=5, relief="sunken")
		button2.grid(row=0, column=2, padx= 20)
		button2.bind("<Button-1>", self.clickClock)

		button3=Button(self._frame, text="Stopwatch", fg=buttonTextColour, highlightthickness=2, highlightbackground=buttonColour, font="comicsansm 10 bold", padx=5, pady=5, relief="sunken")
		button3.grid(row=0, column=3, padx= 20)
		button3.bind("<Button-1>", self.clickStopwatch)

		button4=Button(self._frame, text="Timer", fg=buttonTextColour, highlightthickness=2, highlightbackground=buttonColour, font="comicsansm 10 bold", padx=5, pady=5, relief="sunken")
		button4.grid(row=0, column=4, padx= 20)
		button4.bind("<Button-1>", self.clickTimer)

		self._canvas.create_text(screenWidth/2, 0.7*canvasHeight/2, text="Digital Clock", font="Times 60 bold", fill=buttonTextColour)		
		self._canvas.create_text(screenWidth/2, 1.3*canvasHeight/2, text="By Arghya Bandyopadhyay", font="Times 30 bold", fill=textColour)		

	def refeshCanvas(self):
		self._canvas.delete('all')

	def clickAlarm(self,event):
		self.refeshCanvas()
		Alarm()	

	def clickClock(self,event):
		self.refeshCanvas()
		Clock()

	def clickStopwatch(self,event):
		self.refeshCanvas()
		Stopwatch()

	def clickTimer(self,event):
		self.refeshCanvas()
		Timer()

	def mainloop(self):
		self._root.mainloop()


class Alarm(MainFrame):
	__setAlarm=""
	
	def __init__(self):
		self.__screenHr=Entry(self._root,width=3,justify="center",font="Times 20 bold",bg=entryColour,fg=entryTextColour)
		self.__screenMin=Entry(self._root,width=3,justify="center",font="Times 20 bold",bg=entryColour,fg=entryTextColour)

		self._canvas.create_text(0.8*screenWidth/3, 0.5*canvasHeight/3, text="Set Time:", font="Times 20 bold",fill=textColour)

		self._canvas.create_window(1.4*screenWidth/3, 0.5*canvasHeight/3, window=self.__screenHr)
		self._canvas.create_text(1.7*screenWidth/3, 0.5*canvasHeight/3, text=":", font="Times 20 bold",fill=textColour)
		self._canvas.create_window(2*screenWidth/3, 0.5*canvasHeight/3, window=self.__screenMin)		
		
		ob1=self._canvas.create_text(2.5*screenWidth/3, 0.5*canvasHeight/3, text="+ Add", font="Times 20 bold",fill=buttonTextColour)
		self._canvas.tag_bind(ob1, '<Button-1>', self.addTime)

		self.ob2=self._canvas.create_text(screenWidth/2, 1.5*canvasHeight/3, text="No Current Alarm", font="Times 30 bold",fill=textColour)

	def addTime(self,event):
		self.hr=self.__screenHr.get().zfill(2)
		self.mn=self.__screenMin.get().zfill(2)

		if int(self.hr)>=0 and int(self.hr)<=23:
			if int(self.mn)>=0 and int(self.mn)<=59:
				Alarm.__setAlarm=self.hr+":"+self.mn+":00"

				displayAlarm="Alarm Set At : "+Alarm.__setAlarm
				super()._canvas.itemconfig(self.ob2,text=displayAlarm)

				timeLeft="Alarm Rings After : "
				self.ob3=self._canvas.create_text(screenWidth/2, 2*canvasHeight/3, text=timeLeft, font="Times 20 bold",fill=buttonTextColour)
				
				self.Threading()
		
		self.__screenHr.delete(0,"end")
		self.__screenMin.delete(0,"end")

	def Threading(self):
		self.t=Thread(target=self.checkTime)
		self.t.start()

	def checkTime(self):
		while True:
			now=time.strftime("%H:%M:%S")
			
			if now==Alarm.__setAlarm:
				Alarm.__setAlarm=""
				super()._canvas.itemconfig(self.ob2,text="It's the Time!!!")
				super()._canvas.itemconfig(self.ob3,text="")
				subprocess.call(["afplay",soundTrack])
				super()._canvas.itemconfig(self.ob2,text="No Current Alarm")
				break

			else:
				nowHr=int(time.strftime("%H"))
				nowMn=int(time.strftime("%M"))
				nowSec=int(time.strftime("%S"))
				curTimeSec=(nowHr*60*60)+(nowMn*60)+nowSec
				
				givenTimeSec=(int(self.hr)*60*60)+(int(self.mn)*60)
				diffTimeSec=(givenTimeSec-curTimeSec)

				secLeft=diffTimeSec%(24*3600)
				hourLeft=secLeft//3600
				secLeft%=3600
				minLeft=secLeft//60
				secLeft%=60

				timeLeft="Alarm Rings After : "
				if hourLeft:
					if hourLeft==1:
						timeLeft+=str(hourLeft)+" Hour "
					else:
						timeLeft+=str(hourLeft)+" Hours "
				if minLeft:
					if minLeft==1:
						timeLeft+=str(minLeft)+" Minute "
					else:
						timeLeft+=str(minLeft)+" Minutes "
				if secLeft:
					if secLeft==1:
						timeLeft+=str(secLeft)+" Second"
					else:
						timeLeft+=str(secLeft)+" Seconds"

				super()._canvas.itemconfig(self.ob3,text=timeLeft)



class Clock(MainFrame):
	def __init__(self):
		super()._canvas.create_text(screenWidth/2, 0.7*canvasHeight/3, text="Current Time", font="Times 30 bold", fill=buttonTextColour)
		self.curTime = time.strftime("%H:%M:%S")
		self.timeText=super()._canvas.create_text(screenWidth/2, canvasHeight/2, text="", font="Times 60 bold", fill=textColour)
		self.showTime()

	def showTime(self):
		self.curTime = time.strftime("%H:%M:%S")
		super()._canvas.itemconfig(self.timeText,text=self.curTime)
		super()._canvas.after(1000,self.showTime)


class Stopwatch(MainFrame):
	__hr=__mn=__sec="00"
	__timeText=__hr+":"+__mn+":"+__sec
	__count=0
	__running=False

	def __init__(self):
		self.__curTime=super()._canvas.create_text(screenWidth/2, 1*canvasHeight/3, text=self.__timeText, font="Times 60 bold", fill=textColour)

		ob1=super()._canvas.create_text(1*screenWidth/4, 2.3*canvasHeight/3, text="Start", font="Times 30 bold", fill=buttonTextColour)
		ob2=super()._canvas.create_text(2*screenWidth/4, 2.3*canvasHeight/3, text="Pause", font="Times 30 bold", fill=buttonTextColour)
		ob3=super()._canvas.create_text(3*screenWidth/4, 2.3*canvasHeight/3, text="Reset", font="Times 30 bold", fill=buttonTextColour)
		
		self._canvas.tag_bind(ob1, '<Button-1>', self.clickStart)
		self._canvas.tag_bind(ob2, '<Button-1>', self.clickPause)
		self._canvas.tag_bind(ob3, '<Button-1>', self.clickReset)

	def startTime(self):
		if self.__running:
			self.__count+=1
		
			self.__sec=str(self.__count%60).zfill(2)
			self.__mn=str(self.__count//60).zfill(2)
			self.__hr=str(self.__count//(60*60)).zfill(2)
		
			self.__timeText=self.__hr+":"+self.__mn+":"+self.__sec
			super()._canvas.itemconfig(self.__curTime,text=self.__timeText)
			super()._canvas.after(1000,self.startTime)
		
	def clickStart(self,event):
		self.__running=True
		self.startTime()

	def clickPause(self,event):
		self.__running=False
		self.startTime()

	def clickReset(self,event):
		self.__hr=self.__mn=self.__sec="00"
		self.__timeText=self.__hr+":"+self.__mn+":"+self.__sec
		self.__count=0
		self.__running=False
		super()._canvas.itemconfig(self.__curTime,text=self.__timeText)


class Timer(MainFrame):
	__running=False
	__timeSet=0

	def __init__(self):
		self.__screenHr=Entry(self._root,width=3,justify="center",font="Times 30 bold",bg=entryColour,fg=entryTextColour)
		self.__screenMin=Entry(self._root,width=3,justify="center",font="Times 30 bold",bg=entryColour,fg=entryTextColour)
		self.__screenSec=Entry(self._root,width=3,justify="center",font="Times 30 bold",bg=entryColour,fg=entryTextColour)

		self._canvas.create_text(1*screenWidth/4, canvasHeight/3, text="Set Timer:", font="Times 30 bold",fill=textColour)

		self._canvas.create_text(1*screenWidth/4, canvasHeight/3, text="Set Timer:", font="Times 30 bold",fill=textColour)
		self._canvas.create_window(2*screenWidth/4, canvasHeight/3, window=self.__screenHr)
		
		self._canvas.create_text(2.3*screenWidth/4, canvasHeight/3, text=":", font="Times 30 bold",fill=textColour)
		self._canvas.create_window(2.6*screenWidth/4, canvasHeight/3, window=self.__screenMin)
		
		self._canvas.create_text(2.9*screenWidth/4, canvasHeight/3, text=":", font="Times 30 bold",fill=textColour)		
		self._canvas.create_window(3.2*screenWidth/4, canvasHeight/3, window=self.__screenSec)
		
		ob1=self._canvas.create_text(screenWidth/2, 2.1*canvasHeight/3, text="Start", font="Times 30 bold",fill=buttonTextColour)
		self._canvas.tag_bind(ob1, '<Button-1>', self.addTime)

	def addTime(self,event):
		super().refeshCanvas()

		if self.__screenHr.get()=="":
			self.hr=0
		else:
			self.hr=int(self.__screenHr.get())

		if self.__screenMin.get()=="":
			self.mn=0
		else:
			self.mn=int(self.__screenMin.get())

		if self.__screenSec.get()=="":
			self.sc=0
		else:
			self.sc=int(self.__screenSec.get())

		if int(self.hr)>=0 and int(self.hr)<=99:
			if int(self.mn)>=0 and int(self.mn)<=59:
				if int(self.sc)>=0 and int(self.sc)<=59:  
					Timer.__timeSet=(self.hr*60*60)+(self.mn*60)+(self.sc)+1

					self.countTime=str(self.hr).zfill(2)+":"+str(self.mn).zfill(2)+":"+str(self.sc).zfill(2)
					self.ob2=self._canvas.create_text(screenWidth/2, canvasHeight/3, text=self.countTime, font="Times 60 bold",fill=textColour)
					self.startTimmer()

					self.ob3=self._canvas.create_text(1*screenWidth/3, 2.3*canvasHeight/3, text="Cancel", font="Times 30 bold",fill=buttonTextColour)
					self._canvas.tag_bind(self.ob3, '<Button-1>', self.resetTimmer)
					
					self.ob4=self._canvas.create_text(2*screenWidth/3, 2.3*canvasHeight/3, text="Pause", font="Times 30 bold",fill=buttonTextColour)
					self._canvas.tag_bind(self.ob4, '<Button-1>', self.pauseTimmer)

	def decTime(self):
		if self.__running:
			Timer.__timeSet-=1

			temp=Timer.__timeSet
			self.hr=temp//3600
			temp%=3600
			self.mn=temp//60
			temp%=60
			self.sc=temp

			self.countTime=str(self.hr).zfill(2)+":"+str(self.mn).zfill(2)+":"+str(self.sc).zfill(2)
			super()._canvas.itemconfig(self.ob2,text=self.countTime)
			if self.countTime=="00:00:00":
				self.__running=False
				return
			super()._canvas.after(1000,self.decTime)

	def startTimmer(self):
		self.__running=True
		self.decTime()

	def pauseTimmer(self,event):
		self.__running=not self.__running
		
		if not(self.countTime=="00:00:00"):
			if self.__running:
				super()._canvas.itemconfig(self.ob4,text="Pause")
			else:
				super()._canvas.itemconfig(self.ob4,text="Resume")
			self.decTime()

	def resetTimmer(self,event):
		super().refeshCanvas()
		Timer()


clock=MainFrame()
clock.mainloop()


