import pygame
import random


class Snake(pygame.sprite.Sprite):
    def __init__(self, player_width, player_height, pos_x, pos_y, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([player_width, player_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        print(pos_x, pos_y)
        self.rect.topleft = [pos_x, pos_y]
        self.currentmove = (0, 0)

    def wall_collision(self):
        global running
        # Creating out of bonds lines
        top_line = ((0, 0), (640, 0))
        left_line = ((0, 0), (0, 640))
        bottom_line = ((0, 640), (640, 640))
        right_line = ((640, 640), (640, 0))
        if self.rect.clipline(top_line):
            running = False
            print("You hit the TOP Doofas")
        elif self.rect.clipline(left_line):
            running = False
            print("You hit the LEFT Doofas")
        elif self.rect.clipline(right_line):
            running = False
            print("You hit the RIGHT Doofas")
        elif self.rect.clipline(bottom_line):
            running = False
            print("You hit the BOTTOM Doofas")

    def move_snake(self):
        # Dictionary of snake's moves
        global running
        snakes_moves = {
            pygame.K_w: (0, -20),
            pygame.K_s: (0, 20),
            pygame.K_a: (-20, 0),
            pygame.K_d: (20, 0)}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                self.currentmove = snakes_moves.get(event.key, self.currentmove)

    def update(self):
        self.rect.move_ip(self.currentmove)
        self.rect.clamp_ip(WIN_r)
        pygame.draw.rect(WIN, self.color, self.rect)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.food_coords_x, self.food_coords_y = random.randrange(20, 640, PLAYER_SPEED), random.randrange(20, 640,
                                                                                                           PLAYER_SPEED)

    def update(self):
        global is_food_not_spawned
        if is_food_not_spawned:
            self.spawn_food()
        else:
            pygame.draw.rect(WIN, FOOD_COLOR, (self.food_coords_x, self.food_coords_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    def spawn_food(self):
        global is_food_not_spawned
        print(is_food_not_spawned)
        is_food_not_spawned = False
        self.food_coords_x, self.food_coords_y = random.randrange(20, 640, PLAYER_SPEED), random.randrange(20, 640,
                                                                                                           PLAYER_SPEED)
        print(self.food_coords_x, self.food_coords_y)
        pygame.draw.rect(WIN, FOOD_COLOR, (self.food_coords_x, self.food_coords_y, PLAYER_WIDTH, PLAYER_HEIGHT))


# Initializing pygame modules
pygame.init()

# Music
pygame.mixer.music.load("epic_music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.05)

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
PLAYER_COLOR = (0, 255, 0)

# Coords where player spawns in at start of game
PLAYER_SPAWN_X, PLAYER_SPAWN_Y = 320, 320

# Player size in pixels
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20

# Player speed
PLAYER_SPEED = 20

# Creating food generation
FOOD_COLOR = (255, 192, 203)
is_food_not_spawned = True
food = Food()

all_sprites = pygame.sprite.Group()
snake = Snake(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPAWN_X, PLAYER_SPAWN_Y, PLAYER_COLOR)
all_sprites.add(food)
all_sprites.add(snake)
snake_group = pygame.sprite.Group()
snake_group.add(snake)
food_group = pygame.sprite.Group()
food_group.add(food)
running = True
while running:
    pygame.time.delay(150)
    pygame.Surface.blit(WIN, background, ORIGIN)
    snake.move_snake()
    snake.wall_collision()

    # Update
    all_sprites.update()

    # Draw
    pygame.display.update()

pygame.quit()
