import pygame
import numpy as np
from ray import Ray, create_rays
from boundaries import Boundary, create_screen_walls

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

walls = []
#walls = create_screen_walls(WIDTH, HEIGHT)
walls.append(Boundary(200,200,200,400))

# Create rays
number_of_rays = 100
rays = create_rays(number_of_rays)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.mouse.set_visible(False)
    mouse_position = pygame.mouse.get_pos()
    
    for ray in rays:
        ray.update_position(mouse_position)
        collide_point = ray.collision(walls)
        if collide_point:
            pygame.draw.circle(surface=screen, color="red", radius=4, center=collide_point)
        ray.draw(surface=screen)
    
    for wall in walls:
        pygame.draw.line(surface=screen, color="white",start_pos=wall.origin, end_pos=wall.end, width=3)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
