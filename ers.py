# Written by Lauren Bilbo, June 2017

import pygame
import card

# Display width and height
DISP_WIDTH = 800
DISP_HEIGHT = 600

# Determines frames per second
FRAME_RATE = 30

WHITE = (255,255,255)
LIGHT_GREEN = (60,200,0)
BLACK = (0,0,0)
BLUE = (0,0,155)
GREEN = (0,155,0)

# Render message at location x, y on screen
def render_text(screen, font_size, message, x, y, color):
	disp_width = screen.get_width();
	disp_height = screen.get_height();

	font = pygame.font.SysFont('Arial', font_size)
	text = font.render(message, False, color)
	screen.blit(text, (x, y))

# Render/update score box
def disp_score(screen, score):
	disp_width = screen.get_width();
	disp_height = screen.get_height();

	pygame.draw.rect(screen, BLUE, [disp_width*0.66, disp_height*0.10, 260, 90])
	render_text(screen, 70, "Score: %d" % score, disp_width*0.66+10, disp_height*0.10+20, WHITE)

# Create background for gameplay
def render_game_background(screen, score):
	screen.fill(LIGHT_GREEN)
	disp_score(screen, score)
	pygame.display.update()

# Flip the next card and clear past events
def flip_card(index, used, screen):
	# Create a new card
	next_card = card.Card()
	index = (index + 1) % 3
	used[(index)] = next_card
	next_card.flip_card(screen)

	# Clear past KEYDOWN events
	pygame.event.clear(pygame.KEYDOWN)

	return index

# Return true if a double pattern has occurred
def double(used, index):
	other_index = (index+2)%3 
	return used[index].face == used[other_index].face

# Return true if a sandwich pattern has occurred
def sandwich(used, index):
	other_index = (index+1)%3
	return used[index].face == used[other_index].face

# Return true if the prior cards sum to 10
def sum10(used, index):
	other_index = (index+2)%3 
	return used[index].face + used[other_index].face + 2 == 10

# Return true if any of the patterns have occurred
def pattern(used, index):
	if double(used, index) or sandwich(used, index) or sum10(used, index):
		return True
	else:
		return False

# Checks for a quit event
def check_quit():
	quit_event = pygame.event.get(pygame.QUIT)
	if len(quit_event):
		pygame.quit()
		quit()

# Generate gave over message
def game_over(screen):
	disp_width = screen.get_width();
	disp_height = screen.get_height();

	screen.fill(WHITE)
	render_text(screen, 80, "GAME OVER", \
		disp_width*0.31, disp_height*0.4, BLACK)
	pygame.display.update()
	for i in range(100):
		pygame.time.wait(FRAME_RATE)
		check_quit()

# Generate welcome screen
def generate_welcome(screen):
	disp_width = screen.get_width()
	disp_height = screen.get_height()

	screen.fill(WHITE)
	"""Instructions: This is a variation on the card game, Egyption Rat Screw. The object of the game is to identify patterns in cards. A series of cards will appear in front of you. You must watch for three patterns: 1. Double cards, i.e. King, King, 2. Sandwiches, i.e. King, Queen, King, and 3. Sums of 10, i.e. 4 then 6. Suit does not matter. When you see a pattern press the space bar. You will receive points for identifying correct patterns, and will be penalized for irroneously pressing the space bar and for missing a pattern. Good luck!"""
	
	render_text(screen, 55, "Welcome to Virtual Egyption Rat Screw!", \
		disp_width*0.05, disp_height*0.1, BLACK)
	render_text(screen, 30, "Instructions: This is a variation on the card game, Egyption Rat Screw.", \
		disp_width*0.05, disp_height*0.25, BLACK)
	render_text(screen, 30, "The object of the game is to identify patterns in cards. A series of cards ", \
		disp_width*0.05, disp_height*0.30, BLACK)
	render_text(screen, 30, "will appear in front of you. You must watch for three patterns:", \
		disp_width*0.05, disp_height*0.35, BLACK)
	render_text(screen, 30, "1. Double cards, i.e. King, King", \
		disp_width*0.05, disp_height*0.40, BLACK)
	render_text(screen, 30, "2. Sandwiches, i.e. King, Queen, King", \
		disp_width*0.05, disp_height*0.45, BLACK)
	render_text(screen, 30, "3. Sums of 10, i.e. 4 then 6", \
		disp_width*0.05, disp_height*0.50, BLACK)
	render_text(screen, 30, "Suit does not matter. When you see a pattern press the space bar. You will", \
		disp_width*0.05, disp_height*0.55, BLACK)
	render_text(screen, 30, "receive points for identifying correct patterns, and will be penalized for", \
		disp_width*0.05, disp_height*0.60, BLACK)
	render_text(screen, 30, "for irroneously pressing the space bar and for missing a pattern. Good luck!", \
		disp_width*0.05, disp_height*0.65, BLACK)

	w, h = 130, 75
	pygame.draw.rect(screen, GREEN, [(disp_width-w)/2, disp_height*0.8, w, h])
	render_text(screen, 50, "START", disp_width*0.43, disp_height*0.84, WHITE)
	pygame.display.update()

	# Wait for user to press start button
	waiting = True
	while waiting:
		check_quit()
		pygame.time.wait(FRAME_RATE)
		if pygame.mouse.get_pos()[0] > (disp_width-w)/2 and pygame.mouse.get_pos()[0] < (disp_width+w)/2 and \
			pygame.mouse.get_pos()[1] > disp_height*0.8 and pygame.mouse.get_pos()[1] < disp_height*0.8+h and \
			pygame.mouse.get_pressed()[0]:
			waiting = False



# Control for game play
def play_game(screen):
	wait_time = 2500	# Time between card flips
	score = 50			# Player's score

	# Keep track of last 3 cards
	used = [card.Card(True), card.Card(True), card.Card(True)]
	index = 0

	# Only allow keydown and quit events to be logged
	pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

	# Render background
	render_game_background(screen, score)


	while score > 0:
		index = flip_card(index, used, screen)

		# Wait for wait_time ms
		for i in range(wait_time/FRAME_RATE):
			pygame.time.wait(FRAME_RATE)
			check_quit()

		# Check if user has pressed a key and update
		# score and speed accordingly
		if pygame.event.peek(pygame.KEYDOWN):
			if pattern(used, index):
				score += 10
				wait_time -= 210
			else:
				score -= 15
				if wait_time < 4000:
					wait_time += 250
		else:
			if pattern(used, index):
				score -= 10
				if wait_time < 4000:
					wait_time += 200

		# Update score on screen
		disp_score(screen, score)


	# Print game over message
	game_over(screen)

	# Allow all events
	pygame.event.set_blocked(None)


def main():

	# Initialize pygame
	pygame.init()
	pygame.font.init()

	# Display initialization
	display = pygame.display.set_mode((DISP_WIDTH, DISP_HEIGHT))
	pygame.display.set_caption("Practice Egyption Rat Screw!")
	pygame.display.update()

	while True:
		# Intro screen
		generate_welcome(display)

		# Play the game!
		play_game(display)


	pygame.quit()
	quit()

if __name__ == "__main__":
	main()


