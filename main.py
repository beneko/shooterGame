import pygame

from game import Game


pygame.init()

# generate first window
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 720))

# import background image
background = pygame.image.load('assets/bg.jpg')

# create a game object
game = Game()

running = True

# run program while running is ture
while running:

    # set background image to the window
    screen.blit(background, (0, -200))

    # charge the player Image
    screen.blit(game.player.image, game.player.rect)

    # update screen
    pygame.display.flip()

    # see if player close the window
    for event in pygame.event.get():
        # verify if event is closing the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # verify if player press a key
        elif event.type == pygame.KEYDOWN:
            # verify which key is pressed
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            if event.key == pygame.K_LEFT:
                game.player.move_left()

