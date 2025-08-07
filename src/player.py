from settings import WINDOW_HEIGHT, WINDOW_WIDTH, Group, join, pygame


# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: Group) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load(join("..", "images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_frect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt  # type: ignore
