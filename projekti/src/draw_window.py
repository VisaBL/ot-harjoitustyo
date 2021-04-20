import pygame


class DrawWindow():
    def __init__(self, resolution):
        pygame.init()
        self.surface = pygame.display.set_mode(resolution)
