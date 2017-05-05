#!/usr/bin/python
import pygame
import os
import random
import sys
import time #only for testing
from Photo import Photo
#from gi.repository import Gtk

class MatchGame:

	def startScreen(self):
		startmsg = "FLAG MATCHING GAME"
		self.backgroundimg = "resources/background.png"
		screen = pygame.display.get_surface()
		font1 = pygame.font.Font(None,150)
		font2 = pygame.font.Font(None,75)
		font3 = pygame.font.Font(None,40)
		# Can be added on OLPC to load other fonts
		#pygame.font.SysFont()
		file = open("highscore.txt", "r")
		self.highscore = file.read()
		file.close()
		wait = True
		while wait:
			screen.fill((255,255,255))
			screen.blit(pygame.image.load(self.backgroundimg), (0,150))
			screen.blit(font1.render(startmsg, True, (0, 0, 0)),(150,50))
			screen.blit(font2.render("Press 's' to start", True, (0, 0, 0)),(150,150))
			screen.blit(font2.render("Press 'q' to quit", True, (0, 0, 0)),(150,250))
			screen.blit(font2.render("Highscore: " + self.highscore, True, (0,0,0)), (1000,150))
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
		wait = True
		invalid = False
		while wait:
			screen.fill((255,255,255))
			screen.blit(pygame.image.load(self.backgroundimg), (0,150))
			screen.blit(font1.render("Level Selector", True, (0, 0, 0)),(150,50))
			screen.blit(font2.render("Type the level you would like (1-4)", True, (0, 0, 0)),(150,150))
			screen.blit(font3.render("Level 1 (Easy) - 3 flags", True, (0, 0, 0)), (150,250))
			screen.blit(font3.render("Level 2 (Medium) - 4 flags", True, (0, 0, 0)), (150,300))
			screen.blit(font3.render("Level 3 (Hard) - 5 flags", True, (0, 0, 0)), (150,350))
			screen.blit(font3.render("Level 4 (Very Hard) - 7 flags", True, (0, 0, 0)), (150,400))
			if invalid == True:
				screen.blit(font2.render("Invalid selection", True, (255, 0, 0)), (400,600))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						self.level = 1
						wait = False
					elif event.key == pygame.K_2:
						self.level = 2
						wait = False
					elif event.key == pygame.K_3:
						self.level = 3
						wait = False
					elif event.key == pygame.K_4:
						self.level = 4
						wait = False
					elif event.key == pygame.K_q:
						sys.exit()
					else:
						invalid = True

	def getRandomHand(self):
		keeptrying = True
		while keeptrying:
			disklocation = "flags"
			if self.level == 1 or 2 or 3 or 4:
				first = random.choice(os.listdir(disklocation))
				second = random.choice(os.listdir(disklocation))
				third = random.choice(os.listdir(disklocation))
				flag1 = Photo(os.path.abspath(disklocation + "/" + first),first[:-4],True)
				flag2 = Photo(os.path.abspath(disklocation + "/" + second),first[:-4],False)
				flag3 = Photo(os.path.abspath(disklocation + "/" + third),first[:-4],False)
			if self.level == 2 or 3 or 4:
				fourth = random.choice(os.listdir(disklocation))
				flag4 = Photo(os.path.abspath(disklocation + "/" + fourth),first[:-4],False)
			if self.level == 3 or 4:
				fifth = random.choice(os.listdir(disklocation))
				flag5 = Photo(os.path.abspath(disklocation + "/" + fifth),first[:-4],False)
			if self.level == 4:
				sixth = random.choice(os.listdir(disklocation))
				flag6 = Photo(os.path.abspath(disklocation + "/" + sixth),first[:-4],False)
				seventh = random.choice(os.listdir(disklocation))
				flag7 = Photo(os.path.abspath(disklocation + "/" + seventh),first[:-4],False)
			
			if self.level == 1:
				if first == ".DS_Store" or second == ".DS_Store" or third == ".DS_Store" or first == second or first == third or second == third:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2,flag3]
			elif self.level == 2:
				if first == ".DS_Store" or second == ".DS_Store" or third == ".DS_Store" or fourth == ".DS_Store" or first == second or first == third or first == fourth or second == third or second == fourth or third == fourth:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2,flag3,flag4]
			elif self.level == 3:
				if first == ".DS_Store" or second == ".DS_Store" or third == ".DS_Store" or fourth == ".DS_Store" or fifth == ".DS_Store" or first == second or first == third or first == fourth or first == fifth or second == third or second == fourth or second == fifth or third == fourth or third == fifth or fourth == fifth:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2,flag3,flag4,flag5]
			elif self.level == 4:
				if first == ".DS_Store" or second == ".DS_Store" or third == ".DS_Store" or fourth == ".DS_Store" or fifth == ".DS_Store" or sixth == ".DS_Store" or first == second or first == third or first == fourth or first == fifth or first == sixth or first == seventh or second == third or second == fourth or second == fifth or second == sixth or second == seventh or third == fourth or third == fifth or third == sixth or third == seventh or fourth == fifth or fourth == sixth or fourth == seventh or fifth == sixth or fifth == seventh or sixth == seventh:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2,flag3,flag4,flag5,flag6,flag7]
		shuffledList = sorted(returnlist, key=lambda k: random.random())
		return shuffledList
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
		self.highscore = int(self.highscore)
		while gmround <= 10: #the "10" is the amount of tries you want the user to be able to guess differtnt flags
			gmround += 1

			#while Gtk.events_pending():
			#	Gtk.main_iteration()

			screen.fill((255,255,255))
			screen.blit(pygame.image.load(self.backgroundimg), (0,150))
			widthofphoto = 125
			photoX = 50
			photoY = 200
			photos = self.getRandomHand()
			clickRect = [50,250]
			for photo in photos:
				if (photo.answer == True):
					msg = photo.photoname
					clickRect = [photoX,photoX+widthofphoto]
					answerX = clickRect[0]
				try:
					newimg = pygame.image.load(photo.imgname)
					screen.blit(newimg,(photoX,photoY))
					photoX = photoX + 200
				except:
					print("Can not find image " + photo.imgname)

			text = font.render(msg, True, (0, 0, 0))
			screen.blit(text,(textRect.x,textRect.y))
			scoretext = font.render("Score: " + str(score), True, (0, 0, 0))
			screen.blit(scoretext,(800,50))
			pygame.display.flip()

			keepwaiting = True
			while (keepwaiting):

				#while Gtk.events_pending():
				#	Gtk.main_iteration()

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						if score >= self.highscore:
							file = open("highscore.txt", "w")
							file.write(str(score))
							file.close()
						return
					elif (event.type == pygame.MOUSEBUTTONDOWN):
						if pygame.mouse.get_pos()[0] >= clickRect[0] and pygame.mouse.get_pos()[0] < clickRect[1] and 145 <= pygame.mouse.get_pos()[1] <= 245:
							keepwaiting = False
							screen.blit(font.render("Correct", True, (0,250,0)),(300,600))
							score += 1
						else:
							keepwaiting = False
							screen.blit(font.render("Incorrect", True, (250,0,0)),(300,600))
						screen.blit(font.render("Press any key to continue", True, (0,0,0)),(20,700))
						pygame.draw.rect(screen, (0, 255, 0), (answerX, 200, 125, 100), 5)
						pygame.display.flip()
						wait = True
						while wait:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									sys.exit()
								elif event.type == pygame.MOUSEBUTTONDOWN:
									wait = False
								elif event.type == pygame.KEYDOWN:
									wait = False

		if score >= self.highscore:
			file = open("highscore.txt", "w")
			file.write(str(score))
			file.close()
			self.highScoreMessage()
						
	def highScoreMessage(self):
		file = open("highscore.txt", "r")
		highscore = file.read()
		file.close()
		screen = pygame.display.get_surface()
		screen.fill((255,255,255))
		font1 = pygame.font.Font(None,150)
		font2 = pygame.font.Font(None,75)
		screen.blit(font1.render("NEW HIGH SCORE!", True, (0, 0, 0)),(150,50))
		screen.blit(font1.render("Your new high score is " + highscore, True, (0, 0, 0)),(150,200))
		pygame.display.flip()
		time.sleep(10) #for testing only

	def finishScreen(self):
		screen = pygame.display.get_surface()
		font = pygame.font.Font(None, 75)
		screen.fill((255,255,255))
		screen.blit(pygame.image.load(self.backgroundimg), (0,150))
		screen.blit(font.render("Press 'Q' to quit and any key to play agian", True, (0, 0, 0)),(150,50))
		keepwaiting = True
		while keepwaiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
					else:
						#where will have a screeen variable to go agian.
						# Ends the for loop
				elif event.type == pygame.MOUSEBUTTONDOWN:
					#same as the above if statement

def main():
	pygame.init()
	pygame.display.set_mode((0,0),pygame.RESIZABLE)
	pygame.display.set_caption("Flag Game")
	game = MatchGame()
	game.startScreen()
	game.run()
	#game.finishScreen()

if __name__ == "__main__":
	main()