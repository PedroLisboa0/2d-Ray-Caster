import pygame
from ray import create_rays
from boundaries import create_walls

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2d Raycaster by Pedro Lisboa")
clock = pygame.time.Clock()
running = True
pygame.mouse.set_visible(False)

# Defines if moves the light source with mouse or wasd (keyboard)
movement_type = "mouse"
is_screen_walls = False

walls = create_walls(num=3, screen_walls=is_screen_walls, width=WIDTH, height=HEIGHT)
rays = create_rays(num_of_rays=36)
player_x = WIDTH/2
player_y = HEIGHT/2
player_speed = 15
vision_speed = 0 # == 0 when static

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_r:
                    walls = create_walls(num=3, screen_walls=is_screen_walls, width=WIDTH, height=HEIGHT)
                case pygame.K_w:
                    player_y -= player_speed
                case pygame.K_s:
                    player_y += player_speed
                case pygame.K_a:
                    player_x -= player_speed
                case pygame.K_d:
                    player_x += player_speed
                case pygame.K_e:
                    if vision_speed < 0:
                        vision_speed = 0
                    else:
                        vision_speed = 0.005
                case pygame.K_q:
                    if vision_speed > 0:
                        vision_speed = 0
                    else:
                        vision_speed = - 0.005



    screen.fill("black")

    if movement_type == "mouse":
        player_position = pygame.mouse.get_pos()
    elif movement_type == "keyboard":
        player_position = (player_x, player_y)
    
    for ray in rays:
        ray.update_position(player_position, walls)
        ray.angle += vision_speed
        ray.draw(surface=screen)

    for wall in walls:
        pygame.draw.line(surface=screen, color="white",start_pos=wall.origin, end_pos=wall.end, width=3)
   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
