import pygame
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

movement_type = "mouse" # Defines if moves the light source with mouse or wasd (keyboard)
is_screen_walls = False # Defines if there are wall objects at the borders of the screen
render3d = False
number_of_walls = 4
number_of_rays = 60

walls = create_walls(num=number_of_walls, screen_walls=is_screen_walls, width=WIDTH, height=HEIGHT)
rays = create_rays(num_of_rays=number_of_rays)
caster_x = WIDTH/2
caster_y = HEIGHT/2
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
                    caster_y -= caster_speed
                case pygame.K_s:
                    caster_y += caster_speed
                case pygame.K_a:
                    caster_x -= caster_speed
                case pygame.K_d:
                    caster_x += caster_speed

                case pygame.K_e:
                    if rotation_speed < 0:
                        rotation_speed = 0
                    else:
                        rotation_speed = 0.005
                case pygame.K_q:

                    if rotation_speed > 0:
                        rotation_speed = 0
                    else:
                        rotation_speed = - 0.005
                case pygame.K_SPACE:
                    render3d = not render3d


    screen.fill("black")

    if movement_type == "mouse":
        caster_position = pygame.mouse.get_pos()
    elif movement_type == "keyboard":
        caster_position = (caster_x, caster_y)
    
    for ray in rays:
        ray.update_position(caster_position, walls)
        ray.angle += rotation_speed
        if not render3d:
            ray.draw(surface=screen)

    if not render3d:
        for wall in walls:
            pygame.draw.line(surface=screen, color="white",start_pos=wall.origin, end_pos=wall.end, width=3)

    if render3d:
        renderer.draw(rays=rays, walls=walls)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
