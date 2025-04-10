import pygame
import numpy as np
from ray import Ray, create_rays
from boundaries import create_walls

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

walls = create_walls(num=3, screen_walls=True, width=WIDTH, height=HEIGHT)

# Create rays
number_of_rays = 100
rays = create_rays(number_of_rays)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                walls = create_walls(num=3, screen_walls=True, width=WIDTH, height=HEIGHT)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.mouse.set_visible(False)
    mouse_position = pygame.mouse.get_pos()
    
    for ray in rays:
        ray.update_position(mouse_position, walls)
        for point in ray.collide_points:
            pygame.draw.circle(surface=screen, color="red", radius=4, center=point)
        ray.draw(surface=screen)

    for wall in walls:
        pygame.draw.line(surface=screen, color="white",start_pos=wall.origin, end_pos=wall.end, width=3)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
