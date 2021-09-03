import pygame
pygame.init()

# generate first window
pygame.display.set_caption("Shooter Game")
pygame.display.set_mode((1080, 720))

running = True

# run program while running is ture
while running:
    # see if player close the window
    for event in pygame.event.get():
        # verify if event is closing the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

