import pygame
import numpy as np

class Renderer:
    def __init__(self, surface):
        self.surface = surface
        self.scene_width, self.scene_height = pygame.display.get_window_size()
        self.rect_width = 15

    def create_scene(self, rays):
        self.rects = []
        x_axis = np.linspace(0, self.scene_width, len(rays))
        for ray, x in zip(rays, x_axis):
            if ray.collide_point:
                epsilon = 0.0001
                self.scale = 80
                rect_height = min([self.scale * self.scene_height / (ray.distance_to_collision + epsilon), self.scene_height])
                rect = pygame.Rect(0,0,self.rect_width, rect_height)
                rect.center = (x, self.scene_height/2)
                self.rects.append(rect)


    def draw(self):
        for rect in self.rects:
            rect_color = max((self.map_value(rect.height, self.scale,self.scene_height, 0, 255), 0))
            color = (rect_color, rect_color, rect_color)

            pygame.draw.rect(surface=self.surface, color=color, rect=rect)

    def map_value(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min