import numpy as np

class Grid(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tbl = [[0] * width] * height

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getTbl(self):
		return self.tbl

	def clone(self):
		cpy = Grid(self.width, self.height)
		cpy.tbl = [row[:] for row in self.tbl]
		return cpy

	def transpose(self):
		tmp = self.width
		self.width = self.height
		self.height = tmp
		self.tbl = np.transpose(self.tbl)

	def flipHorizontal(self):
		self.tbl = np.fliplr(tbl)


	def nextVal(self, row, idx):
		i = idx
		while i < len(row):
			if row[i] != 0:
				return i
			i += 1
		return None


	def canSlideRow(self, row):
		i = self.nextVal(row, 0)
		if i == None:
			return False
		if i > 0:
			return True
		while i + 1 < len(row):
			nv = self.nextVal(row, i + 1)
			if nv != None and (nv > i + 1 or row[nv] == row[i]):
				return True
			i = nv
		return False


	def canSlide(self):
		return any(self.canSlideRow(row) for row in self.tbl)


	def slideRow(self, row):
		i = self.nextVal(row, 0)
		# print(str(i))
		if i == None:
			return
		if i > 0:
			row[0] = row[i]
			row[i] = 0
		idx = 0
		# print("idx: " + str(idx))
		# print("row: " + str(row) + "\n")

		while i != None and i + 1 < len(row):
			nv = self.nextVal(row, i + 1)
			# print("i: " + str(i))
			# print("nv: " + str(nv))
			# print("idx: " + str(idx))
			# print("row: " + str(row) + "\n")
			if nv != None:
				if row[nv] == row[idx]:
					row[idx] *= 2
					row[nv] = 0
					# idx -= 1
				elif nv > idx:
					row[idx] = row[nv]
					row[nv] = 0
			i = nv
			idx += 1


	# def slideRow(self, row):

	# 	# Handle empty spaces
	# 	emptySpaces = 0
	# 	i = len(row) - 1
	# 	while i >= 0:
	# 		if row[i] == 0:
	# 			row[i:len(row) - 1] = row[i + 1:len(row)]
	# 			row[len(row) - 1] = 0
	# 			emptySpaces += 1
	# 		i -= 1

	# 	# Test for success
	# 	if emptySpaces == len(row):
	# 		return False
		
	# 	# Handle Combinations
	# 	filledSpaces = len(row) - emptySpaces
	# 	combos = 0
	# 	pair = 0
	# 	while pair < filledSpaces - 1:
	# 		if row[pair] == row[pair + 1]:
	# 			row[pair] *= 2
	# 			row[pair + 1:filledSpaces] = row[pair + 2:filledSpaces] + [0]
	# 			filledSpaces -= 1
	# 			emptySpaces += 1
	# 			combos += 1
	# 		pair += 1

	# 	# Test for success
	# 	return (emptySpaces != 0 or combos != 0)


	def slide(self):
		return any(self.slideRow(row) for row in self.tbl)
