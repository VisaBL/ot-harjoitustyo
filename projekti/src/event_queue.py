from collections import deque
from random import choice
import pygame


class Eventqueue():
    def __init__(self, block_size):
        self._events = deque(choice(["L", "R", "D", "U"]))
        self._size = block_size
        self._previous_command = None
        self._previously_executed = None

# pygame get_event välitetään funktiolle koska automaattiset testit

    def get_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                print(event)
                keypress = None
                if event.key == pygame.K_LEFT:
                    keypress = "L"
                elif event.key == pygame.K_RIGHT:
                    keypress = "R"
                elif event.key == pygame.K_UP:
                    keypress = "U"
                elif event.key == pygame.K_DOWN:
                    keypress = "D"
                if keypress is not None and keypress != self._previous_command:
                    self._events.append(keypress)
                    self._previous_command = keypress
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                return False
        return True

    def return_event(self):
        not_allowed = [("L", "R"), ("R", "L"), ("U", "D"), ("D", "U")]
        command = None
        if len(self._events) > 0:
            keypress = self._events.popleft()
            if (keypress, self._previously_executed) in not_allowed:
                pass
            elif keypress == "L":
                command = (-self._size, 0)
            elif keypress == "R":
                command = (self._size, 0)
            elif keypress == "U":
                command = (0, -self._size)
            elif keypress == "D":
                command = (0, self._size)
            if command == self._previous_command:
                return None
            self._previously_executed = keypress
        return command
