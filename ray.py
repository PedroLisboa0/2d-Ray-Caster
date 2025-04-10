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
        self.length = 1000
        self.collide_points = []

    def update_position(self, new_position, walls):
        self.position.update(new_position)
        self.length = 1000
        self.collide_points = []
        self.check_collision(walls)
        self.end_point = self.position + self.direction * self.length
    
    def draw(self, surface):
        pygame.draw.aaline(surface=surface, color=ray_color,start_pos=self.position, end_pos=self.end_point)

    def check_collision(self, walls):
        for wall in walls:
            x1 = wall.x1
            y1 = wall.y1
            x2 = wall.x2
            y2 = wall.y2
            x3 = self.position.x
            y3 = self.position.y
            x4 = self.position.x + self.direction.x
            y4 = self.position.y + self.direction.y
            
            # if the denominator of the formula is 0, it means the lines are parallel.
            den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
            if den == 0:
                continue

            t = ((x1-x3) * (y3-y4) - (y1-y3) * (x3-x4)) / den
            u = - ((x1-x2) * (y1-y3) - (y1-y2) * (x1-x3)) / den

            # this checks for collision.
            if 0 <= t <= 1 and 0 <= u:
                px = x1 + t * (x2 - x1)
                py = y1 + t * (y2 - y1) 
                self.collide_points.append((px, py))

                disance_to_collision = self.calculate_distance(px, py)
                self.length = disance_to_collision
            else:
                continue

    def calculate_distance(self, point_x, point_y): # calculates euclidian distance between ray origin and collision point
        base = self.position.x - point_x
        height = self.position.y - point_y
        distance = np.sqrt(np.square(base) + np.square(height))
        return distance