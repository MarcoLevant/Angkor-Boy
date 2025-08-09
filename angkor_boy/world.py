import pygame
from player import Player

class World:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(100, 100)
        self.all_sprites.add(self.player)

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)
