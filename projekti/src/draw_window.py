import pygame


class DrawWindow():
    def __init__(self, resolution):
        pygame.init()
        self.surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption('Snake Game')

    def quit(self):
        pygame.quit()
