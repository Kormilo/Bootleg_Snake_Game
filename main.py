import pygame
import random

# Initializing pygame modules
pygame.init()

# Music
pygame.mixer.music.load("epic_music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.10)

# Initializing display settings
flags = pygame.SCALED
SCREEN_SIZE = width, height = 660, 660

# Loading in icon and caption
ICON = pygame.image.load("hellfrog.png")
pygame.display.set_caption("Worm Game!")

# Setting icon
pygame.display.set_icon(ICON)

# Creating display
WIN = pygame.display.set_mode(SCREEN_SIZE, flags=flags)

# Creating rect display
WIN_r = WIN.get_rect()

# loading background image
background = pygame.image.load("new_Background.png").convert()

# 0, 0 Constant created
ORIGIN = (0, 0)

# Setting background image to cover window display
pygame.Surface.blit(WIN, background, ORIGIN)
pygame.display.update()

# Created player color tuple
PLAYER_COLOR = (255, 255, 255)

# Coords where player spawns in at start of game
PLAYER_SPAWN_X, PLAYER_SPAWN_Y = 320, 320

# Player size in pixels
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20

# Player speed
PLAYER_SPEED = 20

# Snake Rect
snake = pygame.draw.rect(WIN, PLAYER_COLOR, (PLAYER_SPAWN_X, PLAYER_SPAWN_Y, PLAYER_WIDTH, PLAYER_HEIGHT))

# Dictionary of snake's moves
snakes_Moves = {
    pygame.K_w: (0, -20),
    pygame.K_s: (0, 20),
    pygame.K_a: (-20, 0),
    pygame.K_d: (20, 0)}

# Tuple of snakes move
move = (0, 0)

# Creating out of bonds lines
top_Line = ((0, 0), (640, 0))
left_Line = ((0, 0), (0, 640))
bottom_Line = ((0, 640), (640, 640))
right_Line = ((640, 640), (640, 0))


# Creating food generation
FOOD_COLOR = (255, 192, 203)
is_food_spawned = True
food = pygame.draw.rect(WIN, FOOD_COLOR, (120, 120, 20, 20))


def food_generator(is_food):
    global is_food_spawned
    global food
    if is_food:
        pass
    else:
        is_food_spawned = True
        food_coords_x, food_coords_y = random.randrange(20, 640, 20), random.randrange(20, 640, 20)
        food = pygame.draw.rect(WIN, FOOD_COLOR, (food_coords_x, food_coords_y, 20, 20))


# Game loop
running = True
moving = True
lastKey = None
score = 0

while running:
    pygame.time.delay(150)
    # Checks events/ if QUIT was called. Stops loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Congrats you quit loser!")
        if event.type == pygame.KEYDOWN:
            move = snakes_Moves.get(event.key, move)
    if snake.clipline(top_Line):
        running = False
        print("You hit the TOP Doofas")
    elif snake.clipline(left_Line):
        running = False
        print("You hit the LEFT Doofas")
    elif snake.clipline(right_Line):
        running = False
        print("You hit the RIGHT Doofas")
    elif snake.clipline(bottom_Line):
        running = False
        print("You hit the BOTTOM Doofas")
    if snake.contains(food):
        snake.union(food)
        is_food_spawned = False
        score += 1
        print(f"the score is {score}")

    food_generator(is_food_spawned)
    snake.move_ip(move)
    snake.clamp_ip(WIN_r)
    pygame.Surface.blit(WIN, background, ORIGIN)
    pygame.draw.rect(WIN, PLAYER_COLOR, snake)
    pygame.draw.rect(WIN, FOOD_COLOR, food)
    pygame.display.update()

pygame.mixer.music.unload()
pygame.quit()
# I LEFT OFF JUST FINISHING UP THE FOOD SPAWNING
# BEST OF LUCK FIGURING OUT HOW TO MAKE THE SNAKE ADD TO ITSELF
# WATCH OUT FOR COLLISION WITH ITSELF
# AND NOT FUCKING MOVE BACK INTO ITSELF
# :'^ ) <3
