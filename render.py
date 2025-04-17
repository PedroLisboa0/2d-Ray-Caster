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
            rect = pygame.Rect(0,0,self.rect_width, ray.distance_to_collision)
            rect.center = (x, self.scene_height/2)
            self.rects.append(rect)


    def draw(self):
        for rect in self.rects:
            pygame.draw.rect(surface=self.surface, color="white", rect=rect)