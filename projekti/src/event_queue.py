import pygame
from collections import deque

class Eventqueue():
    def __init__(self):
        self.events = deque()
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.events.append("L")
                elif event.key == pygame.K_RIGHT:
                    self.events.append("R")
                elif event.key == pygame.K_UP:
                    self.events.append("U")
                elif event.key == pygame.K_DOWN:
                    self.events.append("D")
            elif event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()

    def return_event(self):
        if len(self.events) > 0:
            keypress = self.events.popleft()
            if keypress  == "L":
                return(-30,0)
            elif keypress == "R":
                return(30,0)
            elif keypress == "U":
                return(0,-30)
            elif keypress == "D":
                return(0,30)