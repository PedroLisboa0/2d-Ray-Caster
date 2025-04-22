import pygame
import numpy as np
from ray import create_rays
from boundaries import create_walls
from render import Renderer

pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2d Raycaster by Pedro Lisboa")
clock = pygame.time.Clock()
running = True
pygame.mouse.set_visible(False)

movement_type = "keyboard" # Defines if moves the light source with mouse or wasd (keyboard)
is_screen_walls = True # Defines if there are wall objects at the borders of the screen
render3d = False 
number_of_walls = 4
number_of_rays = 100

field_of_view = np.deg2rad(45)

walls = create_walls(num=number_of_walls, screen_walls=is_screen_walls, width=WIDTH, height=HEIGHT)
rays = create_rays(num_of_rays=number_of_rays, FOV=field_of_view)
caster_position = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
caster_speed = 15
rotation_speed = 0 # initializes static

renderer = Renderer(surface=screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_r:
                    walls = create_walls(num=number_of_walls, screen_walls=is_screen_walls, width=WIDTH, height=HEIGHT)

                case pygame.K_w:
                    caster_position += direction * 15
                case pygame.K_s:
                    caster_position -= direction * 15
                case pygame.K_a:
                    right = direction.rotate(270)
                    caster_position += right * 15
                case pygame.K_d:
                    left = right = direction.rotate(90)
                    caster_position += left * 15

                case pygame.K_e:
                    rotation_speed = 0.005 if rotation_speed == 0 else 0
                case pygame.K_q:
                    rotation_speed = -0.005 if rotation_speed == 0 else 0

                case pygame.K_SPACE:
                    render3d = not render3d



    screen.fill("black")

    if not render3d:
        caster_position.update(pygame.mouse.get_pos())
    
    for ray in rays:
        ray.update_position(caster_position, walls)
        ray.angle += rotation_speed

        direction = np.mean([ray.angle for ray in rays])
        direction = pygame.Vector2(np.cos(direction), np.sin(direction))

        if not render3d:
            ray.draw(surface=screen)

    if not render3d:
        # Draws direction line (for debugging)
        pygame.draw.line(surface=screen, color="red",start_pos=caster_position, end_pos=caster_position+direction * 100 , width=3)
        for wall in walls:
            pygame.draw.line(surface=screen, color="white",start_pos=wall.origin, end_pos=wall.end, width=3)

    if render3d:
        renderer.create_scene(rays)
        renderer.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
