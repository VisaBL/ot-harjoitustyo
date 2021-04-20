import pygame
from snake import Snake
from rewards import Coin, Apple, return_asset
from draw_window import DrawWindow
from event_queue import Eventqueue


class Game():
    def __init__(self, resolution):
        self.display = DrawWindow(resolution)
        self.len = 6
        self.points = 0
        self.cordinates = [340, 260]
        self.direction_update = (0, 0)
        self.time_untill_speedup = 350
        self.edellinen = self.direction_update
        self.window_size = resolution

    def game_loop(self):
        snake_group = pygame.sprite.Group()
        rewards_group = pygame.sprite.Group(Coin())
        input_handler = Eventqueue(40)
        time = 0
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if not input_handler.get_event(pygame.event.get()):
                pygame.quit()
            self.display.surface.fill((0, 0, 0))
            time += clock.get_time()
            if time > self.time_untill_speedup:
                self.update_pos(input_handler.return_event())
                self.collisions(snake_group, rewards_group)
                time = 0
            snake_group.draw(self.display.surface)
            rewards_group.draw(self.display.surface)
            pygame.display.flip()

    def update_pos(self, position):
        if position:
            self.direction_update = (position[0], position[1])
        self.cordinates[0] += self.direction_update[0]
        self.cordinates[1] += self.direction_update[1]
        self.boarder_chekup()

    def collisions(self, snake_group, rewards_group):
        new_bite = Snake(40, self.cordinates, self.len, self.direction_update)
        if pygame.sprite.spritecollide(new_bite, rewards_group, True):
            if len(rewards_group) < 1:
                rewards_group.add(return_asset(
                    snake_group, Coin(), Apple(), 2))
            self.time_untill_speedup -= 4
            self.len += 1
            self.points += 1
        if pygame.sprite.spritecollide(new_bite, snake_group, True):
            print("You Died :( ... Your points are", self.points)
            pygame.quit()
        rewards_group.update()
        snake_group.update()
        snake_group.add(new_bite)

    def does_rotate(self):
        change = None
        if self.direction_update != self.edellinen:
            change = self.edellinen[0] - \
                self.direction_update[0], self.edellinen[1] - \
                self.direction_update[1]
            self.edellinen = (self.cordinates)
            print(change)
        return change

    def boarder_chekup(self):
        if self.cordinates[0] > self.window_size[0]:
            self.cordinates[0] = 0
        elif self.cordinates[0] < 0:
            self.cordinates[0] = self.window_size[0]

        elif self.cordinates[1] > self.window_size[1]:
            self.cordinates[1] = 0
        elif self.cordinates[1] < 0:
            self.cordinates[1] = self.window_size[1]


if __name__ == "__main__":
    testi = Game((800, 600))
    testi.game_loop()
