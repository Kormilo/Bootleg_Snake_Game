import pygame
import random


class Snake(pygame.sprite.Sprite):
    def __init__(self, player_width, player_height, pos_x, pos_y, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([player_width, player_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

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

    @staticmethod
    def move_snake():
        # Dictionary of snake's moves
        global running
        global currentmove
        snakes_moves = {
            pygame.K_w: (0, -20),
            pygame.K_s: (0, 20),
            pygame.K_a: (-20, 0),
            pygame.K_d: (20, 0)}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                currentmove = snakes_moves.get(event.key, currentmove)

    def food_collision(self, food_x, food_y):
        global is_food_not_spawned
        global score
        food_x = food_x
        food_y = food_y
        if self.rect.x == food_x and self.rect.y == food_y:
            is_food_not_spawned = True
            score += 1

    def update(self):
        self.rect.move_ip(currentmove)
        self.rect.clamp_ip(WIN_r)
        pygame.draw.rect(WIN, self.color, self.rect)


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, last_x, last_y, player_width, player_height, color, current_score):
        super().__init__()
        self.last_x = last_x
        self.last_y = last_y
        self.player_width = player_width
        self.player_height = player_height
        self.player_color = color
        self.snake_length = current_score
        self.image = pygame.Surface([player_width, player_height])
        self.image.fill(self.player_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.last_x, self.last_y)

    def spawn_body(self):
        pygame.draw.rect(WIN, self.player_color, self.rect)


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
        is_food_not_spawned = False
        self.food_coords_x, self.food_coords_y = random.randrange(20, 640, PLAYER_SPEED), random.randrange(20, 640,
                                                                                                           PLAYER_SPEED)
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
PLAYER_COLOR = (0, 149, 19)

# Creating player body color tuple
PLAYER_BODY_COLOR = (0, 255, 0)

# Coords where player spawns in at start of game
PLAYER_SPAWN_X, PLAYER_SPAWN_Y = 320, 320

# Player size in pixels
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20

# Player speed
PLAYER_SPEED = 20

# Player's moves
currentmove = (0, 0)

# Creating food generation
FOOD_COLOR = (255, 192, 203)
is_food_not_spawned = True
food = Food()
score = 0


snake = Snake(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPAWN_X, PLAYER_SPAWN_Y, PLAYER_COLOR)
snake_body = SnakeBody(snake.rect.x, snake.rect.y, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR, score)
snake_tail = SnakeBody(snake_body.rect.x, snake_body.rect.y, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR, score)
snake_group = pygame.sprite.Group()
snake_group.add(snake)
snake_group.add(snake_body)

food_group = pygame.sprite.Group()
food_group.add(food)
all_sprites = pygame.sprite.Group()
all_sprites.add(food)
all_sprites.add(snake)

snakes_past_moves = [(PLAYER_SPAWN_X - 20, PLAYER_SPAWN_Y), (PLAYER_SPAWN_X - 40, PLAYER_SPAWN_Y)]
running = True
while running:
    pygame.time.delay(150)
    pygame.Surface.blit(WIN, background, ORIGIN)
    snake.move_snake()
    # Believe it or not this tracks the past movements of the snake
    if currentmove == ORIGIN:
        snakes_past_moves = [(PLAYER_SPAWN_X - 20, PLAYER_SPAWN_Y), (PLAYER_SPAWN_X - 40, PLAYER_SPAWN_Y)]
    elif len(snakes_past_moves) > score + 2:
        snakes_past_moves.reverse()
        snakes_past_moves.pop(-1)
        snakes_past_moves.reverse()
    snakes_past_moves.append((snake.rect.x, snake.rect.y))

    snake.wall_collision()
    snake.food_collision(food.food_coords_x, food.food_coords_y)

    for x in range(len(snakes_past_moves)):
        snake_body = SnakeBody(snakes_past_moves[x][0], snakes_past_moves[x][1], PLAYER_WIDTH, PLAYER_HEIGHT,
                               PLAYER_BODY_COLOR, score)
        snake_body.spawn_body()
    if score > 0:
        for x in range(len(snakes_past_moves)-1):
            if (snake.rect.x, snake.rect.y) == snakes_past_moves[x]:
                running = False
                print("Congrats Doofas you ate yourself.")

    # Love yourself <3
    # Hi
    # Update
    all_sprites.update()

    # Draw
    pygame.display.update()

pygame.quit()
