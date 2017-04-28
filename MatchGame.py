#!/usr/bin/python
import pygame
import os
import random
import sys
from Photo import Photo
#from gi.repository import Gtk

class MatchGame:

	def getRandomHand(self):
		keeptrying = True
		while keeptrying:
			disklocation = "students"
			answer = random.choice(os.listdir(disklocation))
			other = random.choice(os.listdir(disklocation))
			another = random.choice(os.listdir(disklocation))
			flag1 = Photo(os.path.abspath(disklocation + "/" + answer),answer[:-4],True)
			flag2 = Photo(os.path.abspath(disklocation + "/" + other),answer[:-4],False)
			flag3 = Photo(os.path.abspath(disklocation + "/" + another),answer[:-4],False)
			if answer == ".DS_Store" or other == ".DS_Store" or another == ".DS_Store" or answer == other or answer == another or other == another:
				pass
			else:
				keeptrying = False
		returnlist = [flag1,flag2,flag3]
		shuffledList = sorted(returnlist, key=lambda k: random.random())
		return shuffledList

	def startScreen(self):
		startmsg = "FLAG MATCHING GAME"
		screen = pygame.display.get_surface()
		font1 = pygame.font.Font(None,150)
		font2 = pygame.font.Font(None,75)
		font3 = pygame.font.Font(None,40)
		# Can be added on OLPC to load other fonts
		#pygame.font.SysFont()
		wait = True
		while wait:
			screen.fill((255,255,255))
			screen.blit(pygame.image.load("resources/background.png"), (0,150))
			screen.blit(font1.render(startmsg, True, (0, 0, 0)),(150,50))
			screen.blit(font2.render("Press 's' to start", True, (0, 0, 0)),(150,150))
			screen.blit(font2.render("Press 'q' to quit", True, (0, 0, 0)),(150,250))
			screen.blit(font3.render("By: Michael Bateman and Troy Boydell", True, (0, 0, 0)), (150,850))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						wait = False
					elif event.key == pygame.K_q:
						sys.exit()


	def run(self):
		screen = pygame.display.get_surface()
		font = pygame.font.Font(None, 75)
		msg = ""
		text = font.render(msg, True, (250, 250, 250))
		textRect = text.get_rect()
		textRect.x = 150 
		textRect.y = 50
		score = 0
		gmround = 0
		while gmround <= 10:
			gmround += 1

			#while Gtk.events_pending():
			#	Gtk.main_iteration()

			screen.fill((0,0,0))

			photoX = 50
			photoY = 200
			photos = self.getRandomHand()
			clickRect = [50,250]
			for photo in photos:
				if (photo.answer == True):
					msg = photo.photoname
					clickRect = [photoX,photoX+250]
				try:
					newimg = pygame.image.load(photo.imgname)
					screen.blit(newimg,(photoX,photoY))
					photoX = photoX + 250
				except:
					print("Can not find image " + photo.imgname)

			text = font.render(msg, True, (250, 250, 250))
			screen.blit(text,(textRect.x,textRect.y))
			scoretext = font.render("Score: " + str(score), True, (250, 250, 250))
			screen.blit(scoretext,(600,50))
			pygame.display.flip()

			keepwaiting = True
			while (keepwaiting):

				#while Gtk.events_pending():
				#	Gtk.main_iteration()

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						return
					elif (event.type == pygame.MOUSEBUTTONDOWN):
						if pygame.mouse.get_pos()[0] >= clickRect[0] and pygame.mouse.get_pos()[0] < clickRect[1]:
							keepwaiting = False
							score += 1
						else:
							keepwaiting = False
						


def main():
	pygame.init()
	pygame.display.set_mode((0,0),pygame.RESIZABLE)
	pygame.display.set_caption("Flag Game")
	game = MatchGame()
	game.startScreen()
	game.run()

if __name__ == '__main__':
	main()