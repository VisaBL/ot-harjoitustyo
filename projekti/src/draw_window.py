import pygame

class Draw_window():
    def __init__(self, size_x, size_y):
        pygame.init()
        self.surface = pygame.display.set_mode([size_x, size_y])
    def flip(self):
        pygame.display.flip() 


if __name__ == "__main__":
    pass 
