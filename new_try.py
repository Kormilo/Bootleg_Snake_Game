import pygame
import random


class Snake(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def collision(self):
        global running
        if self.rect.clipline(top_Line):
            running = False
            print("You hit the TOP Doofas")
        elif self.rect.clipline(left_Line):
            running = False
            print("You hit the LEFT Doofas")
        elif self.rect.clipline(right_Line):
            running = False
            print("You hit the RIGHT Doofas")
        elif self.rect.clipline(bottom_Line):
            running = False
            print("You hit the BOTTOM Doofas")

    def move_snake(self, lastmove):
        # Dictionary of snake's moves
        snakes_moves = {
            pygame.K_w: (0, -20),
            pygame.K_s: (0, 20),
            pygame.K_a: (-20, 0),
            pygame.K_d: (20, 0)}
        if event.type == pygame.KEYDOWN:
            currentmove = snakes_moves.get(event.key, lastmove)
            self.rect.topleft = currentmove
            print(event.type)

    def update(self):
        pygame.draw.rect(WIN, PLAYER_COLOR, self.rect)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global is_food_spawned
        global food
        if is_food_spawned:
            pass
        else:
            is_food_spawned = True
            self.food_coords_x, self.food_coords_y = random.randrange(20, 640, 20), random.randrange(20, 640, 20)

    def update(self):
        pygame.draw.rect(WIN, FOOD_COLOR, (self.food_coords_x, self.food_coords_y, 20, 20))


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



# Tuple of snakes move
move = (0, 0)

# Creating out of bonds lines
top_Line = ((0, 0), (640, 0))
left_Line = ((0, 0), (0, 640))
bottom_Line = ((0, 640), (640, 640))
right_Line = ((640, 640), (640, 0))


# Creating food generation
FOOD_COLOR = (255, 192, 203)
is_food_spawned = False
food = Food()

all_sprites = pygame.sprite.Group()
snake = Snake(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPAWN_X, PLAYER_SPAWN_Y, PLAYER_COLOR)
all_sprites.add(food)
all_sprites.add(snake)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        move = snake.move_snake(move)



    #update
    all_sprites.update()


    #Draw
    pygame.display.update()

pygame.quit()
