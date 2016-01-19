# This file provides a class constructor for a chess game in pgn (portable game notation) format
#
# class pgnRecord: import pgn data
# class board: process a game

import re
import sys
import numpy as np

recordEnd = ('1-0', '0-1', '1/2-1/2')
rows = [1, 2, 3, 4, 5, 6, 7, 8]
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
castle = ('O-O-O', 'O-O')

class pgnRecord():

	def __init__(self):
	#constructor
		self.tagRoster = {}
		self.moves = ''
		self.game = {}

		return;

	def finishRec(self):
		self.gameList(self.moves)
		return;

	def addField(self, fName, fValue):
		self.tagRoster.update({fName: fValue})
		return;

	def gameList(self, moves):
		moveCount = 1
		moveList = re.split('[ ]*[0-9]+\.', moves)
		for i in range(0, len(moveList)):
			if moveList[i] <> '':
				self.game.update({moveCount: moveList[i].split(' ')})
				moveCount += 1

		return;

	def getECO(self):
		return self.tagRoster['ECO']

	def getGame(self):
		return self.game

	def addLine(self, newLine):
		if('[' in newLine):
			fieldName = newLine[newLine.find('[')+1:newLine.find(' "')]
			fieldValue = newLine[newLine.find('"')+1:newLine.rfind('"')]
			self.addField(fieldName, fieldValue)
		else:
			self.moves = self.moves + newLine + ' '

		return;

	def copy(self):

		theCopy = pgnRecord();
		for k, v in self.tagRoster.iteritems():
			theCopy.addField(k, v)
		theCopy.moves = self.moves
		theCopy.finishRec()
		return theCopy;

	def pgnGamePrint(self):
		for k, v in self.game.iteritems():
			print str(k)+':'+v[0]+' '+v[1]

	def pgnPrint(self):
		for k, v in self.tagRoster.iteritems():
			print k+':'+v
		for k, v in self.game.iteritems():
			print str(k)+':'+v[0]+' '+v[1]
		
		return;

class board():

	def __init__(self, ECO):
		self.openingCode = ECO
		self.game = {}
		self.board = {}
		self.initialBoard()
	
		return;

	def initialBoard(self):
		self.currentMove = 1
		self.sideToMove = 'W'
		
		for row in rows:
			for col in cols:
				self.board.update({col+str(row): '  '})

		for col in cols:
			self.board.update({col+'2': 'WP'})
			self.board.update({col+'7': 'BP'})

		self.board.update({'a1': 'WR', 'b1': 'WN', 'c1': 'WB', 'd1': 'WQ'})
		self.board.update({'h1': 'WR', 'g1': 'WN', 'f1': 'WB', 'e1': 'WK'})
		self.board.update({'a8': 'BR', 'b8': 'BN', 'c8': 'BB', 'd8': 'BQ'})
		self.board.update({'h8': 'BR', 'g8': 'BN', 'f8': 'BB', 'e8': 'BK'})

		return;

	def resetToBeg(self):
		self.initialBoard()

	def moveList(self, nums, moves):
		self.game = dict(zip(nums, moves))
		return;

	def printMoveList(self):
		for k,v in self.game.iteritems():
			print str(k) + ': ' + v[0] +' '+ v[1]

		return;

	def printBoard(self):
		breakLine = '---------------------------------------------------------'
		spaceLine = '|      |      |      |      |      |      |      |      |'
		
		print breakLine
		print spaceLine
		print '|  '+self.board['a8']+'  |  '+self.board['b8']+'  |  '+self.board['c8']+'  |  '+self.board['d8']+'  |  '+self.board['e8']+'  |  '+self.board['f8']+'  |  '+self.board['g8']+'  |  '+self.board['h8']+'  |'
		print spaceLine
		print breakLine
		print spaceLine
		print '|  '+self.board['a7']+'  |  '+self.board['b7']+'  |  '+self.board['c7']+'  |  '+self.board['d7']+'  |  '+self.board['e7']+'  |  '+self.board['f7']+'  |  '+self.board['g7']+'  |  '+self.board['h7']+'  |'
		print spaceLine
		print breakLine
		print spaceLine
		print '|  '+self.board['a6']+'  |  '+self.board['b6']+'  |  '+self.board['c6']+'  |  '+self.board['d6']+'  |  '+self.board['e6']+'  |  '+self.board['f6']+'  |  '+self.board['g6']+'  |  '+self.board['h6']+'  |'
		print spaceLine
		print breakLine
		print spaceLine
		print '|  '+self.board['a5']+'  |  '+self.board['b5']+'  |  '+self.board['c5']+'  |  '+self.board['d5']+'  |  '+self.board['e5']+'  |  '+self.board['f5']+'  |  '+self.board['g5']+'  |  '+self.board['h5']+'  |'
		print spaceLine
		print breakLine
		print spaceLine
		print '|  '+self.board['a4']+'  |  '+self.board['b4']+'  |  '+self.board['c4']+'  |  '+self.board['d4']+'  |  '+self.board['e4']+'  |  '+self.board['f4']+'  |  '+self.board['g4']+'  |  '+self.board['h4']+'  |'
		print spaceLine
		print breakLine
		print spaceLine
		print '|  '+self.board['a3']+'  |  '+self.board['b3']+'  |  '+self.board['c3']+'  |  '+self.board['d3']+'  |  '+self.board['e3']+'  |  '+self.board['f3']+'  |  '+self.board['g3']+'  |  '+self.board['h3']+'  |'
		print spaceLine
		print breakLine
		print spaceLine
		print '|  '+self.board['a2']+'  |  '+self.board['b2']+'  |  '+self.board['c2']+'  |  '+self.board['d2']+'  |  '+self.board['e2']+'  |  '+self.board['f2']+'  |  '+self.board['g2']+'  |  '+self.board['h2']+'  |'
		print spaceLine
		print breakLine
		print spaceLine
		print '|  '+self.board['a1']+'  |  '+self.board['b1']+'  |  '+self.board['c1']+'  |  '+self.board['d1']+'  |  '+self.board['e1']+'  |  '+self.board['f1']+'  |  '+self.board['g1']+'  |  '+self.board['h1']+'  |'
		print spaceLine
		print breakLine
		return;		

	def moveIsCapture(self, moveText):
		if 'x' in moveText:
			return 1
		else:
			return 0

	def filePlus(self, theFile, theAmt):
		fileMap = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
		result = fileMap[theFile] + theAmt
		if (result < 1 or result > 8):
			return 'pastEdge'
		else:
			return fileMap[result]

	def rankPlus(self, theRank, theAmt):
		result = int(theRank) + theAmt
		if (result < 1 or result > 8):
			return 'pastEdge'
		else:
			return str(result)

	def rookMovesPoss(self, square, side, piece):
		squareRank = square[1]
		squareFile = square[0]
		
		poss = []
		checkRanks = [0, 0, 1, -1]
		checkFiles = [1, -1, 0, 0]
		# check the four directions - stop when a piece is your color or opponent's
		for i in range(0, 4):
			num = 1
			blockPosition = 'null'
			testFile = self.filePlus(squareFile, checkFiles[i]*num)
			testRank = self.rankPlus(squareRank, checkRanks[i]*num)
			while (testFile!= 'pastEdge' and testRank != 'pastEdge' and blockPosition == 'null'):
			# rook can only come from a square occupied by a rook of his own color
				if self.board[testFile+testRank] == '  ':
					poss.append(testFile+testRank)
					num += 1
				elif self.board[testFile+testRank] == side+piece:
					poss.append(testFile+testRank)
					blockPosition = testFile+testRank
				else:
					blockPosition = testFile+testRank
				testFile = self.filePlus(squareFile, checkFiles[i]*num)
				testRank = self.rankPlus(squareRank, checkRanks[i]*num)
		return poss			 

	def knightMovesPoss(self, square):
		squareRank = square[1]
		squareFile = square[0]

		poss = []
		# first add moves where rank dist == 2 and file dist == 1
		rankDifs = [ -2, -2, 2, 2, -1, -1, 1, 1]
		fileDifs = [ -1, 1, -1, 1, -2, 2, -2, 2]
		for i in range(0, 8):
			testFile = self.filePlus(squareFile, fileDifs[i])
			testRank = self.rankPlus(squareRank, rankDifs[i])
			if (testFile!= 'pastEdge' and testRank!= 'pastEdge'):
				poss.append(testFile+testRank)
			else:
				next

		return poss

	def bishopMovesPoss(self, square, side, piece):
		squareRank = square[1]
		squareFile = square[0]
		
		poss = []
		checkRanks = [1, 1, -1, -1]
		checkFiles = [1, -1, 1, -1]
		# check the four quadrants - stop when a piece is your color or opponent's
		for i in range(0, 4):
			num = 1
			blockPosition = 'null'
			testFile = self.filePlus(squareFile, checkFiles[i]*num)
			testRank = self.rankPlus(squareRank, checkRanks[i]*num)
			while (testFile!= 'pastEdge' and testRank != 'pastEdge' and blockPosition == 'null'):
			# bishop can only come from a square occupied by a bishop of his own color
				if self.board[testFile+testRank] == '  ':
					poss.append(testFile+testRank)
					num += 1
				elif self.board[testFile+testRank] == side+piece:
					poss.append(testFile+testRank)
					blockPosition = testFile+testRank
				else:
					blockPosition = testFile+testRank
				testFile = self.filePlus(squareFile, checkFiles[i]*num)
				testRank = self.rankPlus(squareRank, checkRanks[i]*num)
		return poss			 

	def kingMovesPoss(self, square, side):
		squareRank = square[1]
		squareFile = square[0]
	
		poss = []
		checkRanks = [-1, -1, -1, 0, 0, 1, 1, 1]
		checkFiles = [-1, 0, 1, -1, 1, -1, 0, 1]

		for i in range(0,8):
			testFile = self.filePlus(squareFile, checkFiles[i])
			testRank = self.rankPlus(squareRank, checkRanks[i])
			if(testFile != 'pastEdge' and testRank != 'pastEdge'):
				poss.append(testFile+testRank)
		return poss
	
	def movePawn(self, moveText, side):
		
		if self.moveIsCapture(moveText)==1:
			destRank = moveText[moveText.find('x')+2:moveText.find('x')+3]
			destFile = moveText[moveText.find('x')+1:moveText.find('x')+2]
			sourceFile = moveText[0]
			if side == 'W':
				sourceRank = str(int(destRank)-1)
			else:
				sourceRank = str(int(destRank)+1)
		else:
			destRank = moveText[1]
			destFile = moveText[0]

		self.board.update({destFile+destRank: side+'P'})

		if self.moveIsCapture(moveText)==1:
			self.board.update({sourceFile+sourceRank : '  '})
		else:
			if side == 'W':
				if self.board[destFile+str(int(destRank)-1)] == 'WP':
				# pawn moved one square
					self.board.update({destFile+str(int(destRank)-1): '  '})
				else:
				# pawn moved two squares - only from the second row
					self.board.update({destFile+'2': '  '})
			else:
				if self.board[destFile+str(int(destRank)+1)] == 'BP':
					self.board.update({destFile+str(int(destRank)+1): '  '})
				else:
					self.board.update({destFile+'7': '  '})
		return;

	def nonPawnDestSq(self, moveText, piece):
		if self.moveIsCapture(moveText)==1:
			return moveText[moveText.find('x')+1:]
		else:
			return moveText[moveText.find(piece)+1:]
		return;

	def moveRook(self, moveText, side):
		destSquare = self.nonPawnDestSq(moveText, 'R')
		if len(destSquare) == 3:
			ambiguous = 1
		else:
			ambiguous = 0
		if ambiguous == 1:
			disambiguate = destSquare[0]
			destSquare = destSquare[1:]

		possSources = self.rookMovesPoss(destSquare, side, 'R')

		for source in possSources:
			if( self.board[source] == side + 'R' and ambiguous == 0):
				sourceSquare = source
			elif( self.board[source] == side + 'R' and ambiguous == 1):
				if disambiguate == source[0] or disambiguate == source[1]:
					sourceSquare = source
			else:
				next

		self.board.update({sourceSquare: '  ', destSquare: side+'R'})

	def removePinnedPiece(self, pieceList):
	# returns the pieceList with the pinned piece removed
	
		# make a copy for each piece possible
		# make each theoretical move
		# check if the king could be taken - if so not possible
			
		print "currently a bug that needs to be fixed:"
		print "move appears ambiguous because check rules not programmed"

		return 

	def moveKnight(self, moveText, side):
		destSquare = self.nonPawnDestSq(moveText, 'N')
		if len(destSquare) == 3:
			ambiguous = 1
		else:
			ambiguous = 0
		if ambiguous == 1:
			disambiguate = destSquare[0]
			destSquare = destSquare[1:]

		possSources = self.knightMovesPoss(destSquare)
		multPossSources = []

		for source in possSources:
		# need to add a check for if the source will endanger the king
		# i.e. is the piece pinned
			if( self.board[source] == side+'N' and ambiguous == 0):
				sourceSquare = source
				multPossSources.append(sourceSquare)
			elif( self.board[source] == side+'N' and ambiguous == 1):
				if disambiguate == source[0] or disambiguate == source[1]:
					sourceSquare = source
			else:
				next
	
		if len(multPossSources) > 1:
			self.removePinnedPiece(multPossSources)
			sourceSquare = multPossSources[0]


		self.board.update({sourceSquare: '  ', destSquare: side+'N'})
		return;


	def moveBishop(self, moveText, side):
		# don't have to disambiguate bishops because opposite color squares
		destSquare = self.nonPawnDestSq(moveText, 'B')
		possSources = self.bishopMovesPoss(destSquare, side, 'B')

		for source in possSources:
			if( self.board[source] == side+'B' ):
				sourceSquare = source
			else:
				next
		self.board.update({sourceSquare: '  ', destSquare: side+'B'})
		return;

	def moveQueen(self, moveText, side):
		destSquare = self.nonPawnDestSq(moveText, 'Q')
		possSources = self.bishopMovesPoss(destSquare, side, 'Q')
		possSources.extend(self.rookMovesPoss(destSquare, side, 'Q'))

		for source in possSources:
			if( self.board[source] == side + 'Q'):
				sourceSquare = source
			else:
				next
		self.board.update({sourceSquare: '  ', destSquare: side+'Q'})
		return;


	def moveKing(self, moveText, side):
		destSquare = self.nonPawnDestSq(moveText, 'K')
		possSources = self.kingMovesPoss(destSquare, side)
		for source in possSources:
			if( self.board[source] == side+'K'):
				sourceSquare = source
			else:
				next
		self.board.update({sourceSquare: '  ', destSquare: side+'K'})
		return;


	def moveIsCastle(self, moveText):
		# 0 = false, 1 = true	
		if 'O-O' in moveText:
		# also works for queenside castle because 'O-O' is substring of 'O-O-O'
			return 1
		else:	
			return 0 

	def moveCastle(self, moveText, side):
		if 'O-O-O' in moveText:
		# Queenside
			if side == 'W':
				self.board.update({'a1': '  ', 'd1': 'WR', 'e1': '  ', 'c1': 'WK'})
			else:
				self.board.update({'a8': '  ', 'd8': 'BR', 'e8': '  ', 'c8': 'BK'})		
		else:
		# Kingside
			if side == 'W':
				self.board.update({'h1': '  ', 'f1': 'WR', 'e1': '  ', 'g1': 'WK'})
			else:
				self.board.update({'h8': '  ', 'f8': 'BR', 'e8': '  ', 'g8': 'BK'})			
		return;

	def move(self, moveText, side):
		if '+' in moveText:
			moveText=moveText[:moveText.find('+')]
		if self.moveIsCastle(moveText)==1:
			self.moveCastle(moveText, side)
		elif 'R' in moveText:
			self.moveRook(moveText, side)
		elif 'N' in moveText:
			self.moveKnight(moveText, side)
		elif 'B' in moveText:
			self.moveBishop(moveText, side)
		elif 'Q' in moveText:
			self.moveQueen(moveText, side)
		elif 'K' in moveText:		
			self.moveKing(moveText, side)
		else:
			self.movePawn(moveText, side)

		if side == 'B':
			self.sideToMove = 'W'
			self.currentMove += 1
		else:
			self.sideToMove = 'B'

		return;

	def processMove(self, number, side):
	# reflect board immediately after move NUMBER for SIDE
		if number < self.currentMove:
			print 'Cannot go back'
		elif number > self.currentMove:
		# process all the moves up until this move
			while( number > self.currentMove ):
				if self.sideToMove == 'W':
					self.move(self.game[self.currentMove][0], 'W')
				else:
					self.move(self.game[self.currentMove][1], 'B')
			self.processMove(number, side)
		elif number == self.currentMove and side == self.sideToMove:
			if side == 'W':
				self.move(self.game[number][0], 'W')
			else:
				self.move(self.game[number][1], 'B')
		elif number == self.currentMove and side != self.sideToMove:
			# case where white has to move and then black
			if self.sideToMove == 'W':
				self.move(self.game[self.currentMove][0], 'W')
			else:
				self.move(self.game[self.currentMove][1], 'B')
			self.processMove(number, side)
		else:
			print 'something wrong in processMove method!'

		return;

# input 1: pgn file name
# input 2: game number
# input 3: move number
# input 4: side
fileName = sys.argv[1]
fp = open(fileName)

currentRec = pgnRecord();
rawData = []
for line in fp:
	cleanedLine = line.replace('\n', '').replace('\r', '')
	if cleanedLine <> '':
		if cleanedLine.endswith(recordEnd):
			currentRec.addLine(cleanedLine)
			currentRec.finishRec()
			rawData.append(currentRec.copy())
			currentRec = pgnRecord()
		else:
			currentRec.addLine(cleanedLine)

def gameProc(gameIndex, moveNum, side):
	thisGame = board(rawData[gameIndex].getECO())
	moveNums = [k for k in rawData[gameIndex].getGame().iterkeys()]
	moveTexts = [v for v in rawData[gameIndex].getGame().itervalues()]
	thisGame.moveList(moveNums, moveTexts)
	thisGame.processMove(moveNum, side)
	thisGame.printBoard()

gameProc(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])

