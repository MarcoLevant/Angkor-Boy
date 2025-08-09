import pygame
import sys
from settings import *
from world import World

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Angkor Boy")
        self.clock = pygame.time.Clock()
        self.running = True
        self.world = World()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.world.update()

    def draw(self):
        self.screen.fill((0, 0, 0)) # Black background
        self.world.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
    game.quit()
