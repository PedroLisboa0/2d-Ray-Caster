import pygame
import numpy as np
ray_color = "white"

def create_rays(num_of_rays):
    angles = np.linspace(start=0, stop=360, num=num_of_rays, endpoint=False)
    rays = []
    for angle in angles:
        ray = Ray(angle=np.deg2rad(angle))
        rays.append(ray)
    return rays

class Ray:
    def __init__(self, x=0, y=0, angle=0):
        self.position = pygame.math.Vector2(x, y)
        self.direction = pygame.math.Vector2(np.cos(angle),np.sin(angle))

    def update_position(self, new_position):
        self.position.update(new_position)
        self.end_point = self.position + self.direction*1500
    
    def draw(self, surface):
        pygame.draw.aaline(surface=surface, color=ray_color,start_pos=self.position, end_pos=self.end_point)

    def collision(self, walls):
        for wall in walls:
            x1 = self.position.x
            y1 = self.position.y
            x2 = self.end_point.x
            y2 = self.end_point.y

            x3 = wall.x1
            y3 = wall.y1
            x4 = wall.x2
            y4 = wall.y2

            t = (x1-x3) * (y3-y4) - (y1-y3) * (x3-x4) / (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
            u = - (x1-x2) * (y1-y3) - (y1-y2) * (x1-x3) / (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
            if 0 <= t <= 1 and 0 <= u <= 1:
                px = x1 + t * (x2 - x1)
                py = y1 + t * (y2 - y1)
                return (px, py)
            else:
                return False
