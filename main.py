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

    # detect left and right key press and move the player
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < screen.get_width() - game.player.image.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # print(game.player.rect.x)

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
            # set true value for pressed key in game.pressed dictionary
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            # set false value for pressed key in game.pressed dictionary
            game.pressed[event.key] = False

