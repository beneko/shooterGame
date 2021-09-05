import pygame

import game
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def move_right(self):
        # verify if player isn't in collision with the monsters
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        # verify if player isn't in collision with the monsters
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity

    def launch_projectile(self):
        # create a new projectile object and add it to the group
        self.all_projectiles.add(Projectile(self))
