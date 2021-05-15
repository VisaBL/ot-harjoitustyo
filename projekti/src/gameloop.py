import pygame
from rewards import Coin, Apple, return_asset
from snake import Snake


class Game():
    def __init__(self, window_size, block_size, menu):
        """[Parameters for the main game]

        Args:
            window_size ([type]): [description]
            block_size ([type]): [description]
            menu ([type]): [description]
        """
        self.cordinates = [340, 340]
        self.direction_update = (0, 0)
        self.window_size = window_size
        self.block_size = block_size
        self.menu = menu
        self.time_untill_speedup = None
        self._points = None

    def game_loop(self, display, input_handler):
        """[The main event loop for the game]

        Args:
            display (Pygame.display object): [The display object, where to draw]
            input_handler (Eventqueue object): [Object that will monitor user input]
        """
        self._set_game_parameters()
        input_handler.init_queue()
        snake_group = pygame.sprite.Group()
        rewards_group = pygame.sprite.Group()
        time = 0
        clock = pygame.time.Clock()
        prev_command = None
        running = True
        while True:
            print(running)
            clock.tick(30)
            if input_handler.get_event(None) == False:
                running = False
                break
            time += clock.get_time()
            if time > self.time_untill_speedup:
                event = self.update_pos(input_handler.return_event())
                command = event[2] if event else None
                running = self.collisions(
                    snake_group, rewards_group, (command, prev_command))
                display.draw_to_screen([snake_group, rewards_group])
                if command is not None:
                    prev_command = command
                time = 0
            if not running:
                self.menu.snake_dead_handler(self._points)
                break

    def update_pos(self, position):
        if position:
            self.direction_update = (position[0], position[1])
        self.cordinates[0] += self.direction_update[0]
        self.cordinates[1] += self.direction_update[1]
        self.boarder_chekup()
        if position:
            return position
        return None

    def collisions(self, snake_group, rewards_group, input_commands):
        runing = True
        new_bite = Snake(self.block_size, self.cordinates, self._points +
                         6, self.direction_update)
        if pygame.sprite.spritecollide(new_bite, rewards_group, True):
            if len(rewards_group) < 1:
                rewards_group.add(return_asset(
                    snake_group, Coin(), Apple(), self.block_size, self.window_size))
            self.time_untill_speedup -= 4
            self._points += 1
        if pygame.sprite.spritecollide(new_bite, snake_group, True):
            runing = False
        if len(rewards_group) == 0:
            rewards_group.add(return_asset(
                snake_group, Coin(), None, self.block_size, self.window_size))
        rewards_group.update()
        snake_group.update(input_commands)
        snake_group.add(new_bite)

        return runing

    def boarder_chekup(self):
        margin = self.block_size/2
        if self.cordinates[0] > self.window_size[0]:
            self.cordinates[0] = margin
        elif self.cordinates[0] < 0:
            self.cordinates[0] = self.window_size[0]-margin

        elif self.cordinates[1] > self.window_size[1]:
            self.cordinates[1] = margin
        elif self.cordinates[1] < 0:
            self.cordinates[1] = self.window_size[1]-margin

    def _set_game_parameters(self):
        self.cordinates = [340, 340]
        self.time_untill_speedup = 300
        self._points = 0
        self.direction_update = (40, 0)


if __name__ == "__main__":
    clas = Game((600, 600), 40, None)
