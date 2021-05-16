from event_queue import Eventqueue
from gameloop import Game
from ui.draw_window import DrawWindow
from ui.menu import Menu


class Main():
    def __init__(self, resolution, block_size):
        self.window_size = resolution
        self.block_size = block_size
        self.display = DrawWindow(self.window_size)
        self.menu = Menu((self.window_size), Eventqueue(
            self.block_size), self.display)
        self.game = Game(self.window_size, self.block_size, self.menu)

    def init_game(self):
        self.menu.main_menu(self.game)


if __name__ == "__main__":
    luokka = Main((800, 600), 40)
    luokka.init_game()
