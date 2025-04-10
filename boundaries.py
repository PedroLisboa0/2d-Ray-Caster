import pygame
from random import randint

def create_walls(num, screen_walls, width, height):
    walls = []
    if screen_walls:
        walls = create_screen_walls(width, height)
    for i in range(num):
        new_wall = Boundary(x1=randint(0, width), y1=randint(0, height), x2=randint(0, width), y2=randint(0, height))
        walls.append(new_wall)
    return walls

class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.origin = pygame.Vector2(x1,y1)
        self.end = pygame.Vector2(x2,y2)
    
def create_screen_walls(width, height):
    screen_walls = [[(0,0),(width,0)], [(0,0),(0,height)], [(0,height),(width,height)], [(width,0),(width,height)]]
    walls = []
    for wall in screen_walls:
        boundary = Boundary(wall[0][0], wall[0][1], wall[1][0], wall[1][1])
        walls.append(boundary)
    return walls
        