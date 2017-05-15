#!/usr/bin/python
import pygame
import os
import random
import sys
import codecs
from Photo import Photo
#from gi.repository import Gtk

class FlagGame:

	def __init__(self):
		self.restart = True
		self.backgroundimg = "resources/background.png"
		self.screen = pygame.display.get_surface()
		self.font1 = pygame.font.Font(None,150)
		self.font2 = pygame.font.Font(None,75)
		self.font3 = pygame.font.Font(None,40)
		self.flaghistory = []

	def startScreen(self):
		#pygame.font.SysFont() #This can be used to add special fonts
		file = open("highscore.txt", "r")
		self.highscore = file.read()
		file.close()
		wait = True
		while wait:
			self.screen.fill((255,255,255))
			self.screen.blit(pygame.image.load(self.backgroundimg), (0,150))
			self.screen.blit(self.font1.render("FLAG MATCHING GAME", True, (0, 0, 0)),(150,50))
			self.screen.blit(self.font2.render("Press 'S' to start", True, (0, 0, 0)),(150,150))
			self.screen.blit(self.font2.render("Press 'Q' to quit", True, (0, 0, 0)),(150,250))
			self.screen.blit(self.font2.render("Highscore: " + self.highscore, True, (0,0,0)), (1000,150))
			self.screen.blit(self.font3.render("By: Michael Bateman and Troy Boydell", True, (0, 0, 0)), (150,850))
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
			self.screen.fill((255,255,255))
			self.screen.blit(pygame.image.load(self.backgroundimg), (0,150))
			self.screen.blit(self.font1.render("Level Selector", True, (0, 0, 0)),(150,50))
			self.screen.blit(self.font2.render("Type the level you would like using number keys (1-4)", True, (0, 0, 0)),(150,150))
			leveltext = ["Level 1 - (Easy) - 2 flags", "Level 2 (Medium) - 3 flags", "Level 3 (Hard) - 4 flags", "Level 4 (Very Hard) - 5 flags"]
			textlocation = 200
			for i in range(len(leveltext)):
				textlocation += 50
				self.screen.blit(self.font3.render(leveltext[i], True, (0, 0, 0)), (150,textlocation))
			if invalid == True:
				self.screen.blit(self.font2.render("Invalid selection", True, (255, 0, 0)), (400,600))
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

	def instructionScreen(self):
		wait = True
		while wait:
			self.screen.fill((255, 255, 255))
			self.screen.blit(pygame.image.load(self.backgroundimg), (0,150))
			self.screen.blit(self.font1.render("Instructions - Level " + str(self.level), True, (0, 0, 0)),(150, 50))
			instructiontext = ["You will be presented with " + str(self.level + 1) + " flags to choose from", "There will be 20 rounds", "Choose the correct flag by clicking the flag image with your mouse", "There will be a map with the location highlighted", "Don't cheat and lookup the location", "At any time during the game, press the 'Q' on your keyboard to quit the game", "At any time during the game, press 'I' to see the instructions again", "Are you ready? Press any key to continue"]
			location = 150
			for i in range(len(instructiontext)):
				location += 50
				self.screen.blit(self.font3.render(instructiontext[i], True, (0, 0, 0)),(150, location))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
					else:
						wait = False

	def getRandomHand(self):
		keeptrying = True
		while keeptrying:
			disklocation = "flags"
			if self.level == 1 or 2 or 3 or 4:
				first = random.choice(os.listdir(disklocation))
				second = random.choice(os.listdir(disklocation))
				flag1 = Photo(os.path.abspath(disklocation + "/" + first),first[:-4],True)
				flag2 = Photo(os.path.abspath(disklocation + "/" + second),first[:-4],False)
			if self.level == 2 or 3 or 4:
				third = random.choice(os.listdir(disklocation))
				flag3 = Photo(os.path.abspath(disklocation + "/" + third),first[:-4],False)
			if self.level == 3 or 4:
				fourth = random.choice(os.listdir(disklocation))
				flag4 = Photo(os.path.abspath(disklocation + "/" + fourth),first[:-4],False)
			if self.level == 4:
				fifth = random.choice(os.listdir(disklocation))
				flag5 = Photo(os.path.abspath(disklocation + "/" + fifth),first[:-4],False)

			try:
				self.countryimg = pygame.image.load("countryimg/" + first)
			except:
				print("Could not find " + first)
			
			if self.level == 1:
				if first == ".DS_Store" or second == ".DS_Store" or first == second:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2]
			elif self.level == 2:
				if first == ".DS_Store" or second == ".DS_Store" or third == ".DS_Store" or first == second or first == third or second == third:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2,flag3]
			elif self.level == 3:
				if first == ".DS_Store" or second == ".DS_Store" or third == ".DS_Store" or fourth == ".DS_Store" or first == second or first == third or first == fourth or second == third or second == fourth or third == fourth:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2,flag3,flag4]
			elif self.level == 4:
				if first == ".DS_Store" or second == ".DS_Store" or third == ".DS_Store" or fourth == ".DS_Store" or fifth == ".DS_Store" or first == second or first == third or first == fourth or first == fifth or second == third or second == fourth or second == fifth or third == fourth or third == fifth or fourth == fifth:
					pass
				else:
					keeptrying = False
					returnlist = [flag1,flag2,flag3,flag4,flag5]

			for i in range(len(self.flaghistory)):
				if first == self.flaghistory[i]:
					keeptrying = True
					break
			self.flaghistory.append(first)
		shuffledList = sorted(returnlist, key=lambda k: random.random())
		return shuffledList

	def run(self):
		msg = ""
		text = self.font2.render(msg, True, (250, 250, 250))
		textRect = text.get_rect()
		textRect.x = 150 
		textRect.y = 50
		self.score = 0
		gmround = 1
		noofrounds = 20 #the number is the amount of flags to guess
		self.highscore = int(self.highscore)
		soundcorrect = pygame.mixer.Sound("sounds/chime.wav")
		soundwrong = pygame.mixer.Sound("sounds/buzzer.wav")
		while gmround <= noofrounds:able to guess flags
			gmround += 1

			#while Gtk.events_pending():
			#	Gtk.main_iteration()

			self.screen.fill((255,255,255))
			self.screen.blit(pygame.image.load(self.backgroundimg), (0,150))
			widthofphoto = 125
			photoX = 50
			photoY = 200
			photos = self.getRandomHand()
			clickRect = [50,250]
			for photo in photos:
				if (photo.answer == True):
					msgencoded = photo.photoname
					#msg = msgencoded.decode('string-escape').decode("utf-8") #uncomment this when running on the OLPC
					msg = msgencoded
					clickRect = [photoX,photoX+widthofphoto]
					answerX = clickRect[0]
					self.screen.blit(self.countryimg,(50,400))
				try:
					newimg = pygame.image.load(photo.imgname)
					self.screen.blit(newimg,(photoX,photoY))
					photoX = photoX + 200
				except:
					print("Can not find image " + photo.imgname)
			if len(msg) <= 20:
				text = self.font2.render(msg, True, (0, 0, 0))
			else:
				text = self.font3.render(msg, True, (0, 0, 0))
			self.screen.blit(text,(textRect.x,textRect.y))
			scoretext = self.font2.render("Score: " + str(self.score), True, (0, 0, 0))
			self.screen.blit(scoretext,(800,50))
			pygame.display.flip()

			keepwaiting = True
			while keepwaiting:

				#while Gtk.events_pending():
				#	Gtk.main_iteration()

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						if score >= self.highscore:
							file = open("highscore.txt", "w")
							file.write(str(score))
							file.close()
						sys.exit()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							sys.exit()
						elif event.key == pygame.K_i:
							self.instructionScreen()
							keepwaiting = False
							gmround -= 1
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if 0 <= pygame.mouse.get_pos()[0] <= 50 or 175 <= pygame.mouse.get_pos()[0] <= 250 or 375 <= pygame.mouse.get_pos()[0] <= 450 or 575 <= pygame.mouse.get_pos()[0] <= 650 or 775 <= pygame.mouse.get_pos()[0] <= 850 or 975 <= pygame.mouse.get_pos()[0]:
							break
						elif 175 >= pygame.mouse.get_pos()[1] or 300 <= pygame.mouse.get_pos()[1]:
							break
						elif pygame.mouse.get_pos()[0] >= clickRect[0] and pygame.mouse.get_pos()[0] < clickRect[1] and 145 <= pygame.mouse.get_pos()[1] <= 245:
							keepwaiting = False
							self.screen.blit(self.font2.render("Correct", True, (0,250,0)),(300,600))
							soundcorrect.play()
							self.score += 1
						else:
							keepwaiting = False
							soundwrong.play()
							if 50 <= pygame.mouse.get_pos()[0] <= 175:
								selectionX = 50
							elif 250 <= pygame.mouse.get_pos()[0] <= 375:
								selectionX = 250
							elif 450 <= pygame.mouse.get_pos()[0] <= 575:
								selectionX = 450
							elif 650 <= pygame.mouse.get_pos()[0] <= 775:
								selectionX = 650
							elif 850 <= pygame.mouse.get_pos()[0] <= 975:
								selectionX = 850
							self.screen.blit(self.font2.render("Incorrect", True, (250,0,0)),(300,600))
							pygame.draw.rect(self.screen, (255, 0, 0), (selectionX, 200, 125, 100), 5)
						self.screen.blit(self.font2.render("Press any key to continue", True, (0,0,0)),(20,700))
						pygame.draw.rect(self.screen, (0, 255, 0), (answerX, 200, 125, 100), 5)
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

		if self.score >= self.highscore:
			file = open("highscore.txt", "w")
			file.write(str(self.score))
			file.close()
			self.highScoreMessage()
		self.finishScreen()
						
	def highScoreMessage(self):
		file = open("highscore.txt", "r")
		highscore = file.read()
		file.close()
		self.screen.fill((255,255,255))
		self.screen.blit(pygame.image.load(self.backgroundimg), (0,150))
		self.screen.blit(self.font1.render("NEW HIGH SCORE!", True, (0, 0, 0)),(150,50))
		self.screen.blit(self.font1.render("Your new high score is " + highscore, True, (0, 0, 0)),(150,200))
		self.screen.blit(self.font2.render("Press any key to continue", True, (0, 0, 0)),(150,300))
		pygame.display.flip()
		keepwaiting = True
		while keepwaiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					keepwaiting = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					keepwaiting = False

	def finishScreen(self):
		self.screen.fill((255,255,255))
		self.screen.blit(pygame.image.load(self.backgroundimg), (0,150))
		self.screen.blit(self.font2.render("Score: " + str(self.score), True, (0,0,0)),(150,50))
		self.screen.blit(self.font2.render("Press 'Q' to quit and any key to play again", True, (0, 0, 0)),(150,150))
		pygame.display.flip()
		keepwaiting = True
		while keepwaiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
					else:
						keepwaiting = False
						self.restart = True
						# Why does this need 2 keydowns for both variables to be set???
						

def main():
	pygame.init()
	pygame.display.set_mode((0,0),pygame.FULLSCREEN)
	game = FlagGame()
	while game.restart:
		game.restart = False
		game.startScreen()
		game.instructionScreen()
		game.run()
		game.finishScreen()

if __name__ == "__main__":
	main()