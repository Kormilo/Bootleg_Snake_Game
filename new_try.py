import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, pos_x, pos_y):
        self.rect.topleft = [pos_x, pos_y]

    def move(self, snake_move, is_game_running):




# General setup
pygame.init()
Clock = pygame.time.Clock()

# Game Screen
SCREEN_SIZE = width, height = 660, 660
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.mouse.set_visible(False)


# Loading in icon and caption
ICON = pygame.image.load("hellfrog.png")
pygame.display.set_caption("Worm Game!")
pygame.display.set_icon(ICON)

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

# Dictionary of snake's moves
snakes_Moves = {
    pygame.K_w: (0, -20),
    pygame.K_s: (0, 20),
    pygame.K_a: (-20, 0),
    pygame.K_d: (20, 0)}

# Tuple of snakes move
move = (0, 0)

snake = Snake(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPAWN_X, PLAYER_SPAWN_Y, PLAYER_COLOR)

snake_group = pygame.sprite.Group()
snake_group.add(snake)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            move = snakes_Move.get(event.key, move)
    pygame.display.flip()
    snake_group.draw(WIN)
    Clock.tick(60)


pygame.quit()
