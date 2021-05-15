from collections import deque
from random import choice
import pygame


class Eventqueue():
    def __init__(self, block_size):
        self._events = deque(choice(["L", "R", "D", "U"]))
        self._size = block_size
        self._previous_command = None
        self._previously_executed = None

# event list välitetään funktiolle testejä varten. Jos

    def get_event(self, event_list):
        """[this funktion will check and queue user input, also will register quits]

        Args:
            event_list (list): [ongoinm events, if none will get events from pygame video system]

        Returns:
            [Bool]: [Will return true if running, and false if there has been a quit input]
        """
        if pygame.get_init():
            event_list = pygame.event.get()
        running = True
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                keypress = None
                if event.key == pygame.K_LEFT:
                    keypress = "L"
                elif event.key == pygame.K_RIGHT:
                    keypress = "R"
                elif event.key == pygame.K_UP:
                    keypress = "U"
                elif event.key == pygame.K_DOWN:
                    keypress = "D"
                elif event.key == pygame.K_ESCAPE:
                    running = False
                if keypress and keypress != self._previous_command:
                    self._events.append(keypress)
                    self._previous_command = keypress
            if event.type == pygame.QUIT:
                running = False
        return running

    def return_event(self):
        """Will return event, position update and keypress

        Returns:
            [Tuple]: [X-update, Y-update, Keypress ]
        """
        not_allowed = [("L", "R"), ("R", "L"), ("U", "D"), ("D", "U")]
        command = None
        if len(self._events) > 0:
            keypress = self._events.popleft()
            if (keypress, self._previously_executed) in not_allowed:
                command = None
            elif keypress == "L":
                command = (-self._size, 0, keypress)
            elif keypress == "R":
                command = (self._size, 0, keypress)
            elif keypress == "U":
                command = (0, -self._size, keypress)
            elif keypress == "D":
                command = (0, self._size, keypress)
            if command == self._previous_command:
                command = None
            self._previously_executed = keypress
        return command

    def init_queue(self):
        """[To reset the queue ready for the new game after old game]
        """
        self._events = deque(choice(["L", "R", "D", "U"]))
        self._previous_command = None
        self._previously_executed = None

# Fuktioita testejä varten

    def previous_command(self):
        return self._previously_executed

    def reset_queue(self):
        self._previous_command = None
        self._previously_executed = None
