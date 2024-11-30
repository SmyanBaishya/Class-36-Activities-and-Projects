import pygame
import random

# Initialise Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Change Sprite Colours")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Custom event for changing colours
CHANGE_COLOUR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOUR_EVENT, 2000)  # Trigger every 2 seconds

# Sprite class
class ColourSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, size, colour):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center=(x, y))
        self.colour = colour

    def change_colour(self):
        # Change to a random colour
        new_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_colour)

# Create sprites
sprite1 = ColourSprite(200, 300, 100, (255, 0, 0))  # Red square
sprite2 = ColourSprite(600, 300, 100, (0, 0, 255))  # Blue square

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == CHANGE_COLOUR_EVENT:
            sprite1.change_colour()
            sprite2.change_colour()

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()

