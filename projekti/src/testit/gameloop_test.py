import unittest
f  # rom gameloop import Game

# luodaan feikki display-luokka, jotta voidaan testata pelisilmukkaa


class Mocup_display():
    def draw_to_screen(sprites: list):
        for sprite in sprites:
            sprites.append(sprite)
        return sprites


class Mocup_eventqueue():
    def __init__(self, blocksize):
        self.block_size = blocksize
        self.eventqueue = []
        self.loop_count = 0

    # event_getter_that will evetually return false and quit the game :)
    def get_event(self, events):
        self.loop_count += 1
        if self.loop_count < 100:
            return True
        return False
    # this funktion does nothing :(

    def init_queue(self):
        pass

    def return_event(self):
        command = None
        if len(self.eventqueue) > 0:
            command = self.eventqueue.pop()
        return command


class Fake_menu():
    def snake_dead_handler(self, points):
        return points


class Tests(unittest.TestCase):
    def setUp(self):
        self.game = Game((800, 600), 40, Fake_menu())
        self.inputqueue = Mocup_eventqueue(40)
        self.display = Mocup_display

    def test_gameloop_runs_and_quits(self):
        self.game.game_loop(self.display, self.inputqueue)


if __name__ == "__main__":
    luokka = Mocup_eventqueue(40)
    for i in range(200):
        print(luokka.get_event(None))
