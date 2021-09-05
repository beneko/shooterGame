import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 20
        self.max_health = 20
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

    def forward(self):
        # verify if player isn't in collision with the monsters
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity



