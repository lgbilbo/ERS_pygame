import pygame
import random

# Import card image and define card sizes

# Scale refers to how much we enlarge the card
# from the original image
SCALE = 3

cards_image = pygame.image.load("cards.png")


# Dimensions of the original image
CARDS_HEIGHT = cards_image.get_height()
CARDS_WIDTH = cards_image.get_width()

# Scale image
cards_image = pygame.transform.scale(cards_image, (CARDS_WIDTH*SCALE, CARDS_HEIGHT*SCALE))

# Height and width of an individual card
CARD_HEIGHT = CARDS_HEIGHT/4.0*SCALE
CARD_WIDTH = CARDS_WIDTH/13.0*SCALE


# BLANK is used for dummy cards at start up
BLANK = 100

# SUIT variables
HEARTS = 0
DIAMONDS = 1
SPADES = 2
CLUBS = 3

# FACE/NUMBER variables
ACE = 0
TWO = 1
THREE = 2
FOUR = 3
FIVE = 4
SIX = 5
SEVEN = 6
EIGHT = 7
NINE = 8
TEN = 9
JACK = 10
QUEEN = 11
KING = 12



class Card:
	def __init__(self, dummy = False):
		# Dummy cards are used only at start up
		if dummy:
			self.suit = BLANK
			self.face = BLANK
		else:
			self.suit = random.randint(0,3)
			self.face = random.randint(0,12)

	def flip_card(self, display):
		# card_x_pos and card_y_pos are where the card
		# will appear on the screen
		card_x_pos = (display.get_width()-CARD_WIDTH)/2
		card_y_pos = (display.get_height()-CARD_HEIGHT)/2
		# Display card to screen
		display.blit(cards_image,(card_x_pos, card_y_pos), pygame.Rect(self.face*CARD_WIDTH, self.suit*CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))
		pygame.display.update()











	
