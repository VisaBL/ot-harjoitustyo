import pygame


class DrawWindow():
    def __init__(self, resolution):
        pygame.init()
        self.surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption('Snake Game')

    def refresh(self):
        pygame.display.update()
        self.surface.fill((0, 0, 0))

    def quit(self):
        try:
            pygame.quit()
        except pygame.error:
            print("Bye Bye!")
