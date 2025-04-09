import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.mouse.set_visible(False)
    mouse_position = pygame.mouse.get_pos()

    # RENDER YOUR GAME HERE
    pygame.draw.circle(surface=screen, color="red", center=mouse_position, radius=10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
