from rewards import Coin
import unittest

import pygame
from gameloop import Game

# luodaan feikki luokat, jotta voidaan testata pelisilmukkaa
# ja jotka imitoivat pygamen toiminnallisuuksia


class Mocup_display():
    def __init__(self, mode):
        self.sprites = []

    def draw_to_screen(self, sprites: list):
        for sprite in sprites:
            self.sprites.append(sprite)
        return

    def return_sprites(self):
        return self.sprites


class Mocup_eventqueue():
    def __init__(self, blocksize: int, loops_untill_quitting: int, events: list):
        self.block_size = blocksize
        self.eventqueue = events
        self.loop_count = 0
        self.loops = loops_untill_quitting
    # event_getter_that will evetually return false and quit the game :)

    def get_event(self, events):
        self.loop_count += 1
        if self.loop_count is not None and self.loop_count > 200:
            return False
        return True

    # this funktion does nothing :(

    def init_queue(self):
        pass

    def return_event(self):
        command = None
        if len(self.eventqueue) > 0:
            command = self.eventqueue.pop()
        return command


class Fake_menu():
    def __init__(self):
        self.points = 0

    def snake_dead_handler(self, points):
        self.points = points

    def return_status(self):
        return self.points


class Fake_clock():
    def __init__(self):
        self.time = 0

    def get_time(self):
        return self.time

    def tick(self, n):
        self.time += n


class Tests(unittest.TestCase):
    def setUp(self):
        self.menu = Fake_menu()
        self.game = Game((800, 600), 40, self.menu)
        self.inputqueue = None
        self.display = Mocup_display(0)
        self.clock = Fake_clock()
        self.set_event([(0, -40, "D"), (40, 0, "R")], 200)

    def set_event(self, events, loops):
        self.inputqueue = Mocup_eventqueue(40, loops, events)

    def test_gameloop_runs_and_quits(self):
        self.game.game_loop(self.display, self.inputqueue, self.clock, None)

    def test_gameloop_runs_and_quits_if_snake_collides(self):
        event0 = (0, -40, "D")
        event1 = (-40, 0, "L")
        event2 = (0, 40, "U")
        event3 = (40, 0, "R")
        event4 = (0, -40, "D")
        events = [event0, event1, event2, event3, event4]
        self.set_event(events, None)
        self.game.game_loop(self.display, self.inputqueue, self.clock, None)
        game_state = self.menu.return_status()
        self.assertEqual(0, game_state)

    def test_game_loop_monitors_the_boarders_x_axis(self):
        test_status = True
        event0 = [(40, 0, "L")]
        self.set_event(event0, 1000)
        self.game.game_loop(self.display, self.inputqueue, self.clock, None)
        sprites = self.display.return_sprites()
        for group in sprites:
            for sprite in group:
                location = sprite.rect.center
                if location[0] not in range(20, 781):
                    test_status = False
        self.assertEqual(True, test_status)

    def test_game_loop_monitors_the_boarders_y_axis(self):
        test_status = True
        event0 = [(0, -40, "U")]
        self.set_event(event0, 1000)
        self.game.game_loop(self.display, self.inputqueue, self.clock, None)
        sprites = self.display.return_sprites()
        for group in sprites:
            for sprite in group:
                location = sprite.rect.center
                if location[1] not in range(20, 581):
                    test_status = False
        self.assertEqual(True, test_status)

    def test_game_loop_collisions_grow_points(self):
        test = False
        event0 = [(-40, 0, "L")]
        rewards_group = pygame.sprite.Group(Coin(), Coin(), Coin(), Coin())
        i = 20
        for sprite in rewards_group:
            sprite.rect.center = (i, 340)
            i += 40
        self.display = Mocup_display(1)
        self.set_event(event0, 500)
        self.game.game_loop(self.display, self.inputqueue,
                            self.clock, rewards_group)
        game_state = self.menu.return_status()
        if game_state in range(4, 6):
            test = True
        self.assertEqual(True, test)


if __name__ == "__main__":
    luokka = Mocup_eventqueue(40)
    for i in range(200):
        print(luokka.get_event(None))
