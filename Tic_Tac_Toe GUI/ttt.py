from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import random

boardSize=600
symbolSize=(boardSize / 3 - boardSize / 8) / 2
symbolThickness = 50
boardColour="#D9B8C4"
titleColour="#1E000E"
subTitleColour="#501823"
buttonText="#953740"
xColor = "#1E2749"
oColor = "#046E8F"


#main page - Player vs Player or Player vs Computer
class mainPage(object):
	_root=Tk()
	_canvas=Canvas(_root, width=boardSize, height=boardSize, bg=boardColour)

	_xScore,_oScore,_tieScore=0,0,0
	_xWin,_oWin,_tieWin=False,False,False
	
	_board=np.zeros(shape=(3,3))
	_xTurn=True
	_playerGame=False

	def __init__(self):		
		self._root.title("Tic-Tac-Toe")
		self._root.maxsize(boardSize,boardSize)
		self._root.minsize(boardSize,boardSize)
		self._canvas.pack(expand=YES,fill=BOTH)

		self._canvas.create_text(boardSize/2, (1.3)*boardSize/6, text="Tic-Tac-Toe", font="Times 60 bold", fill=titleColour)
		self._canvas.create_text(boardSize/2, (2.4)*boardSize/6, text="Which one would you choose?", font="Times 40 bold", fill=subTitleColour)

		ob1=self._canvas.create_text(boardSize/2, (3.5)*boardSize/6, text="Player vs Player", font="Times 50 bold", fill=buttonText)
		ob2=self._canvas.create_text(boardSize/2, (4.5)*boardSize/6, text="Player vs Computer", font="Times 50 bold", fill=buttonText)
		self._canvas.tag_bind(ob1, '<Button-1>', self.clickPlayer)
		self._canvas.tag_bind(ob2, '<Button-1>', self.clickComputer)

	def mainloop(self):
		self._root.mainloop()

	def initialize(self):
		for i in range(2):
			self._canvas.create_line((i+1)*boardSize/3, 0, (i+1)*boardSize/3, boardSize, width=symbolThickness/10, fill=titleColour)
		for i in range(2):
			self._canvas.create_line(0, (i+1)*boardSize/3, boardSize, (i+1)*boardSize/3, width=symbolThickness/10, fill=titleColour)

	def setTurn(self):
		mainPage._xTurn=not mainPage._xTurn

	def available(self,x,y):
		if self._board[x][y]==0:
			return True
		else:
			return False

	def gridToPos(self, pos):
		return np.array(pos//(boardSize/3),dtype=int)

	def posToGrid(self,x,y):
		pos = np.array([x,y], dtype=int)
		return (boardSize/3)*pos+boardSize/6

	def drawX(self,x,y):
		pos=self.posToGrid(x,y)
		self._canvas.create_line(pos[1]-symbolSize, pos[0]-symbolSize, pos[1]+symbolSize, pos[0]+symbolSize, width=symbolThickness,fill=xColor)
		self._canvas.create_line(pos[1]-symbolSize, pos[0]+symbolSize, pos[1]+symbolSize, pos[0]-symbolSize, width=symbolThickness,fill=xColor)

	def drawO(self,x,y):
		pos=self.posToGrid(x,y)
		self._canvas.create_oval(pos[1]-symbolSize, pos[0]-symbolSize, pos[1]+symbolSize, pos[0]+symbolSize, width=symbolThickness,outline=oColor)

	def isWinner(self,player):
		for i in range(3):
			#row
			if(self._board[i][0]==self._board[i][1]==self._board[i][2]==player):
				return True
			#column
			if(self._board[0][i]==self._board[1][i]==self._board[2][i]==player):
				return True

		#diagonal
		if(self._board[0][0]==self._board[1][1]==self._board[2][2]==player):
			return True
		if(self._board[0][2]==self._board[1][1]==self._board[2][0]==player):
			return True

		return False

	def isTie(self):
		x,y=np.where(self._board==0)
		tie=False
		if len(x)==0:
			tie=True
		return tie

	def isGameOver(self):
		self._xWin=self.isWinner(-1)
		if not self._xWin:
			self._oWin=self.isWinner(1)
			if not self._oWin:
				self._tieWin=self.isTie()
		
		gameOver=self._xWin+self._oWin+self._tieWin

		if self._xWin:
			mainPage._xScore+=1
		if self._oWin:
			mainPage._oScore+=1
		if self._tieWin:
			mainPage._tieScore+=1

		return gameOver

	def displayBoard(self, player2):
		self._canvas.delete('all')
		self._canvas.unbind('<Button-1>')

		self._canvas.create_text(boardSize/2, (1.3)*boardSize/6, text="Tic-Tac-Toe", font="Times 50 bold", fill=titleColour)
		self._canvas.create_text(boardSize/2, (2.0)*boardSize/6, text="Score Board", font="Times 30 bold", fill=subTitleColour)

		text="Player 1 (X): "+str(self._xScore)+"\n"+str(player2)+" (O): "+str(self._oScore)+"\n"+"Tie\t: "+str(self._tieScore)+"\n"
		self._canvas.create_text(boardSize/2, (3.0)*boardSize/6, text=text, font="Times 30 bold", fill=subTitleColour)

		ob1=self._canvas.create_text(boardSize/2, (4.0)*boardSize/6, text="Play Again", font="Times 40 bold", fill=buttonText)
		ob2=self._canvas.create_text(boardSize/2, (4.8)*boardSize/6, text="Main Menu", font="Times 40 bold", fill=buttonText)
		self._canvas.tag_bind(ob1, '<Button-1>', self.clickPlayAgain)
		self._canvas.tag_bind(ob2, '<Button-1>', self.clickMainMenu)

	def clickPlayer(self, event):
		self._root.title("Player vs Player")
		self._canvas.delete('all')
		mainPage._playerGame=True

		self.initialize()
		playerVsPlayer()

	def clickComputer(self, event):
		self._root.title("Player vs Computer")
		self._canvas.delete('all')
		mainPage._playerGame=False

		self.initialize()
		playerVsComputer()

	def clickPlayAgain(self,event):
		mainPage._board=np.zeros(shape=(3,3))
		mainPage._xWin,mainPage._oWin,mainPage._tieWin=False,False,False
		mainPage._xTurn=True
		
		self._canvas.delete('all')
		self.initialize()
		if mainPage._playerGame:
			playerVsPlayer()
		else:
			playerVsComputer()

	def clickMainMenu(self,event):	
		mainPage._xScore,mainPage._oScore,mainPage._tieScore=0,0,0
		mainPage._xWin,mainPage._oWin,mainPage._tieWin=False,False,False
		mainPage._board=np.zeros(shape=(3,3))
		mainPage._xTurn=True
		
		self._canvas.delete('all')
		mainPage()


#player vs player
class playerVsPlayer(mainPage):
	__count=0
	def __init__(self):
		super()._canvas.bind('<Button-1>', self.click)

	def click(self, event):
		if self.__count==0:
			self.__count+=1
			return
		
		pos=np.array([event.x,event.y])
		pos=super().gridToPos(pos)
		x,y=pos[1],pos[0]

		if super()._xTurn:
			if super().available(x,y):
				super().drawX(x,y)
				super()._board[x][y]=-1
				super().setTurn()
		else:
			if super().available(x,y):
				super().drawO(x,y)
				super()._board[x][y]=1
				super().setTurn()

		if super().isGameOver():
			super().displayBoard("Player 2")


#player vs computer
class playerVsComputer(mainPage):
	__count=0
	def __init__(self):
		super()._canvas.bind('<Button-1>', self.click)

	def place(self):
		find=False
		while not find:
			x,y=random.randint(0,boardSize),random.randint(0,boardSize)
			pos=np.array([x,y])
			pos=super().gridToPos(pos)
			x,y=pos[1],pos[0]
			if super().available(x,y):
				find=True

		if not super()._xTurn:
			super().drawO(x,y)
			super()._board[x][y]=1
			super().setTurn()

		if super().isGameOver():
			super().displayBoard("Computer")

	def click(self, event):
		if self.__count==0:
			self.__count+=1
			return
		
		pos=np.array([event.x,event.y])
		pos=super().gridToPos(pos)
		x,y=pos[1],pos[0]

		if super()._xTurn:
			if super().available(x,y):
				super().drawX(x,y)
				super()._board[x][y]=-1
				super().setTurn()

		if super().isGameOver():
			super().displayBoard("Computer")
		else:
			self.place()
		

screen=mainPage()
screen.mainloop()