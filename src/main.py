from os import walk
from os.path import join

import pygame
from pygame.sprite import Group


# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, player, *groups: Group) -> None:
        super().__init__(*groups)
        self.image = player
        self.rect = self.image.get_frect(center= ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2)))
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt #type: ignore

# PyGame Init
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TILE_SIZE = 64
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

# Import Images
player_surface = pygame.image.load(join("..", 'images', 'player','down', '0.png')).convert_alpha()

#Sprite Groups
all_sprites = pygame.sprite.Group()

# Call Sprites
player = Player(player_surface, all_sprites)

# Main Loop
while running:
    # Frame Control
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Refresh
    all_sprites.update(dt)

    # Game
    display_surface.fill("#3a2e3f")
    all_sprites.draw(display_surface)

    pygame.display.update()