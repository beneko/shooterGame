import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 3
        self.image = pygame.image.load('assets/projectile.png')
        # resize image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 100
        self.origin_image = self.image
        self.angle = 0

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # delete projectile when it is out of screen
        if self.rect.x > 1080:
            self.remove()

    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        self.angle += 8
        # rotate image by angle
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        # rotation by center of image
        self.rect = self.image.get_rect(center=self.rect.center)
