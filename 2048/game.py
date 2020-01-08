import math
import pygame
import sys

from board import Board

'''
A class to represent a Game of 2048.
'''
class Game(object):

	def __init__(self, width=4, height=4):
  
		# Create the board
		self.board = Board(width, height)
  
		# Initialize Pygame
		pygame.init()
  
		# Create the display and clock
		self.display = pygame.display.set_mode((500, 500))
		pygame.display.set_caption("2048")
		self.clock = pygame.time.Clock()

		# Create the fonts
		sizes = [(2 ** n, max(40, math.floor(40 / math.ceil(math.log10(2 ** n))))) for n in range(1, 50)]
		fonts = [(n, pygame.font.SysFont("Impact", size)) for n,size in sizes]
		self.texts = {n:font.render(str(n), True, (255, 255, 255)) for n,font in fonts}
  
		# Since the game has not started yet, set running to False
		self.running = False

	def getBoard(self):
		return self.board


	def initBoard(self):
		self.board.toStartingState()


	def start(self):
		print("Starting 2048...")
		self.initBoard()
		print(str(self.board))
		self.running = True

		print("Successfully Started 2048.")
		self.run()


	def run(self):
		print("Running 2048...")

		while True:
			
			self.clock.tick(60)
   
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("Quitting 2048...")
					pygame.quit()
					sys.exit()

			self.processUI()
			self.update(1.0 / 60.0)
			self.render()

		self.end()
  
  
	def processUI(self):
		keys = pygame.key.get_pressed()
  
		left = keys[pygame.K_LEFT]
		right = keys[pygame.K_RIGHT]
		up = keys[pygame.K_UP]
		down = keys[pygame.K_DOWN]

		self.board.resetLastSlide((left, right, up, down))

		if left ^ right ^ up ^ down:
			if left:
				self.board.slideLeft()
			if right:
				self.board.slideRight()
			if up:
				self.board.slideUp()
			if down:
				self.board.slideDown()


	def update(self, dt):
		pass


	def render(self):
		self.display.fill(-1)
		self.drawBoard()
		pygame.display.update()
  

	def drawBoard(self):
		self.board.draw(self.display, self.texts)
			

	def end(self):
		print("Successfully Quit 2048.")
