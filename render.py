import pygame

class Renderer:
    def __init__(self, surface):
        self.scene = surface
        self.scene_width, self.scene_height = pygame.display.get_window_size()

    def create_scene(self, rays, walls):
        pass