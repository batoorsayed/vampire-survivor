from player import Player
from settings import WINDOW_HEIGHT, WINDOW_WIDTH, join, pygame


# PyGame Init
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Survivor")
        self.clock = pygame.time.Clock()
        self.running = True

        # Sprite Groups
        self.all_sprites = pygame.sprite.Group()

        # Call Sprites
        self.player = Player(self.all_sprites)

    # Main Loop
    def run(self):
        while self.running:
            # Frame Control
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Refresh
            self.all_sprites.update(dt)

            # Game
            self.display_surface.fill("#3a2e3f")
            self.all_sprites.draw(self.display_surface)

            # Draw
            pygame.display.update()

        # Quit Game
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()