import pygame
import numpy as np
ray_color = "white"
max_ray_length = 2500 # this just has to be bigger than the screen's diagonal size, so it can traverse the whole window.
# However, it will never get to the max length since they collide with the screen walls.

start_angle = 60
FOV = 90

def create_rays(num_of_rays):
    angles = np.linspace(start=start_angle, stop=start_angle+FOV, num=num_of_rays, endpoint=False)
    rays = []
    for angle in angles:
        ray = Ray(angle=np.deg2rad(angle))
        rays.append(ray)
    return rays


class Ray:


    def __init__(self, angle, x=0, y=0):
        self.position = pygame.math.Vector2(x, y)
        self.angle = angle
        self.direction = pygame.math.Vector2(np.cos(self.angle),np.sin(self.angle))
        self.length = max_ray_length
        self.collide_points = []


    def update_position(self, new_position, walls):
        self.position.update(new_position)
        self.direction.update((np.cos(self.angle),np.sin(self.angle)))
        self.length = max_ray_length
        self.collide_points = []
        self.collide_point = None
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
            else:
                continue

            distances = [self.calculate_distance(*point) for point in self.collide_points]
            self.distance_to_collision = min(distances)

            point_index = distances.index(self.distance_to_collision)
            self.collide_point = self.collide_points[point_index]

            self.length = self.distance_to_collision


    def calculate_distance(self, point_x, point_y): # calculates euclidian distance between ray origin and collision point
        base = self.position.x - point_x
        height = self.position.y - point_y
        distance = np.sqrt(np.square(base) + np.square(height))
        return distance
    