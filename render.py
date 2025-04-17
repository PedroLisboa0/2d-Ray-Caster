import pygame
import numpy as np

class Renderer:
    def __init__(self, surface):
        self.surface = surface
        self.scene_width, self.scene_height = pygame.display.get_window_size()
        self.rect_width = 10

    def create_scene(self, rays):
        self.rects = []
        x_axis = np.linspace(0, self.scene_width, len(rays))
        for ray, x in zip(rays, x_axis):
            if ray.collide_point:
                
                projection_distance = ray.distance_to_collision * np.cos(np.rad2deg(ray.angle))
                rect_height = self.scene_height / projection_distance
                rect = pygame.Rect(0,0,self.rect_width+10, rect_height)
                rect.center = (x, self.scene_height/2)
                self.rects.append(rect)


    def draw(self):
        for rect in self.rects:
            rect_color = self.map_value(rect.height, 1,self.scene_height, 0, 255)
            pygame.draw.rect(surface=self.surface, color="white", rect=rect)

    def map_value(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min