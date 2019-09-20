
import pygame

pygame.init()
pygame.mixer.init()

FPS_TARGET = 60
BLACK = (0, 0, 0)


class Viewer(object):
    def __init__(self, game):
        self.game = game
        self.running = False
        self.clock = pygame.time.Clock()
        self.window_settings = pygame.HWSURFACE | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode((self.game.width, self.game.height), self.window_settings)
        pygame.display.set_caption('Game Viewer')

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS_TARGET)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.draw()
        pygame.quit()

    def draw(self):
        self.screen.fill(BLACK)
        # TODO: do drawing here
        pygame.display.flip()
