import math
import pygame
import random

from grid import Grid

SLIDE_UP = 1 << 0
SLIDE_DOWN = 1 << 1
SLIDE_LEFT = 1 << 2
SLIDE_RIGHT = 1 << 3


class Board(object):

	def __init__(self, width=4, height=4):
		self.grid = [[Tile(r, c) for c in range(width)] for r in range(height)]
		self.width = width
		self.height = height
		self.lastSlide = 0

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getGrid(self):
		return self.grid

	def placeTile(self, row, col, tile):
		self.grid[row][col] = tile

	def removeTile(self, row, col, tile):
		self.grid[row][col] = tile

	def randomAvailableSpace(self):
		return random.choice(self.allAvailableSpaces())

	def allAvailableSpaces(self):
		return [tile.getPos() for row in self.grid for tile in row if tile.isEmpty()]

	def placeRandomTile(self):
		val = (2, 4)[random.random() > 0.9]
		pos = self.randomAvailableSpace()
		self.placeTile(*pos, Tile(*pos, val))

	def toStartingState(self):
		for i in range(2):
			self.placeRandomTile()

	def transpose(self):
		tmp = self.width
		self.width = self.height
		self.height = tmp
		self.grid = list(map(list, zip(*self.grid)))

	def flipRows(self):
		self.grid = [row[::-1] for row in self.grid]

	def nextNum(self, nums, i):
		n = i + 1
		while n < self.width:
			if nums[n] != 0:
				return n
			n += 1
		return None

	# def slideRaw(self, nums):
	# 	moved = False
	# 	i = self.nextNum(nums, -1)
	#
	# 	if i is None:
	# 		return False
	# 	if i > 0:
	# 		nums[0] = nums[i]
	# 		nums[i] = 0
	# 		moved = True
	# 	i = 0
	#
	# 	while i < self.width:
	# 		nv = self.nextNum(nums, i)
	# 		if nv is None:
	# 			return moved
	# 		if nums[nv] == nums[i]:
	# 			nums[i] *= 2
	# 			nums[nv] = 0
	# 			moved = True
	# 		elif nv > i + 1:
	# 			nums[i + 1] = nums[nv]
	# 			nums[nv] = 0
	# 			i += 1
	# 			moved = True
	# 	return moved
 
 
	def slideRaw(self, nums):
		i = self.nextNum(nums, -1)

		if i is None:
			return

		if i > 0:
			nums[0] = nums[i]
			nums[i] = 0
			i = 0

		while i < self.width:
			nv = self.nextNum(nums, i)
			if nv is None:
				return
			if nums[nv] == nums[i]:
				nums[i] *= 2
				nums[nv] = 0
			elif nv > i + 1:
				nums[i + 1] = nums[nv]
				nums[nv] = 0
				i += 1
			else:
	   			i += 1


	def slideRow(self, row):
		nums = [tile.getVal() for tile in row]
		print("Attempting to slide " + str(nums))
		self.slideRaw(nums)
		print("Did it!")
		for i in range(len(nums)):
			row[i].setVal(nums[i])


	def slide(self):
		for row in self.grid:
			self.slideRow(row)
	

	def canSlideRaw(self, nums):
		i = self.nextNum(nums, -1)

		if i is None:
			return False

		if i > 0:
			return True

		while i < self.width:
			nv = self.nextNum(nums, i)
			if nv is None:
				return False
			if nums[nv] == nums[i] or nv > i + 1:
				return True
			else:
	   			i += 1


	def canSlideRow(self, row):
		nums = [tile.getVal() for tile in row]
		print("Attempting to slide " + str(nums))
		print("Did it!")
		return self.canSlideRaw(nums)


	def canSlide(self):
		return any(self.canSlideRow(row) for row in self.grid)


	def gameOver(self):
		return not (self.canSlideLeft() or self.canSlideRight() or self.canSlideUp() or self.canSlideDown())

		
	def __str__(self):
		return '\n'.join(' '.join(str(tile.getVal()).ljust(4) for tile in row) for row in self.grid)

	def __repr__(self):
		return str(self)

	def clone(self):
		pass

	def resetLastSlide(self, kps):
		if self.lastSlide != 0 and not kps[self.lastSlide - 1]:
			self.lastSlide = 0

	def slideLeft(self):
		if self.lastSlide != 1 and self.canSlideLeft():
			print("Sliding left...")
			res = self.slide()
			self.lastSlide = 1
			self.placeRandomTile()

	def slideRight(self):
		if self.lastSlide != 2 and self.canSlideRight():
			print("Sliding right...")
			self.flipRows()
			res = self.slide()
			self.flipRows()
			self.lastSlide = 2
			self.placeRandomTile()

	def slideUp(self):
		if self.lastSlide != 3 and self.canSlideUp():
			print("Sliding up...")
			self.transpose()
			res = self.slide()
			self.transpose()
			self.lastSlide = 3
			self.placeRandomTile()

	def slideDown(self):
		if self.lastSlide != 4 and self.canSlideDown():
			print("Sliding down...")
			self.transpose()
			self.flipRows()
			res = self.slide()
			self.flipRows()
			self.transpose()
			self.lastSlide = 4
			self.placeRandomTile()

	def canSlideLeft(self):
		return self.canSlide()

	def canSlideRight(self):
		self.flipRows()
		res = self.canSlide()
		self.flipRows()
		return res

	def canSlideUp(self):
		self.transpose()
		res = self.canSlide()
		self.transpose()
		return res

	def canSlideDown(self):
		self.transpose()
		self.flipRows()
		res = self.canSlide()
		self.flipRows()
		self.transpose()
		return res

	def getMoves(self):
		return 0

	def draw(self, display, texts):
		for row in self.grid:
			for tile in row:
				tile.draw(display, texts)


from AAfilledRoundedRect import AAfilledRoundedRect

class Tile(object):

	def __init__(self, row, col=None, val=None):
		if type(row) in [list, tuple]:
			self.row, self.col = row
			self.val = col
		else:
			self.row = row
			self.col = col
			self.val = val if val != None else 0
		self.lastPos = None

	def getRow(self):
		return self.row

	def setRow(self, row):
		self.row = row

	def getCol(self):
		return self.col

	def setCol(self, col):
		self.col = col

	def getVal(self):
		return self.val

	def setVal(self, val):
		self.val = val

	def getPos(self):
		return (self.row, self.col)

	def setPos(self, pos):
		self.row, self.col = pos

	def savePos(self):
		self.lastPos = self.getPos

	def isEmpty(self):
		return self.val == 0

	def moveTo(self, row, col):
		if type(row) in [list, tuple]:
			self.row, self.col = row
		else:
			self.row = row
			self.col = col

	def draw(self, display, texts):
		if self.isEmpty():
			AAfilledRoundedRect(display, (self.col * 60 + 5, self.row * 60 + 5, 50, 50), (200, 195, 190), 0.1)
		else:
			ts = AAfilledRoundedRect(display, (self.col * 60 + 5, self.row * 60 + 5, 50, 50), (200, 160, 120), 0.1)
			text = texts[self.val]
			tr = text.get_rect()
			display.blit(text, (ts[0] - tr[0] + ts[2] // 2 - tr[2] // 2, ts[1] - tr[1] + ts[3] // 2 - tr[3] // 2))