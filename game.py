import pygame.sprite

from player import Player
from monster import Monster


class Game:

    def __init__(self):
        # generate a player object
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        # generate a group of monster object
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()

    def spawn_monster(self):
        # generate a monster object
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


