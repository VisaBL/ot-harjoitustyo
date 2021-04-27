import pygame
from snake import Snake
from rewards import Coin, Apple, return_asset
from draw_window import DrawWindow
from event_queue import Eventqueue
from leaderboard_uploader import ScoreUploader


class Game():
    def __init__(self, resolution, bloc_size):
        self.display = DrawWindow(resolution)
        self.cordinates = [340, 340]
        self.direction_update = (0, 0)
        self.time_untill_speedup = 350
        self.window_size = resolution
        self.block_size = bloc_size
        self.points = 0

    def game_loop(self):
        snake_group = pygame.sprite.Group()
        rewards_group = pygame.sprite.Group(Coin())
        input_handler = Eventqueue(self.block_size)
        time = 0
        clock = pygame.time.Clock()
        prev_command = None
        running = True
        while True:
            clock.tick(60)
            if not input_handler.get_event(pygame.event.get()):
                DrawWindow.quit()
            time += clock.get_time()
            if time > self.time_untill_speedup:
                command = self.update_pos(input_handler.return_event())
                if not self.collisions(snake_group, rewards_group, (command, prev_command)):
                    running = False
                snake_group.draw(self.display.surface)
                rewards_group.draw(self.display.surface)
                if not running:
                    self.snake_dead_handler(input_handler)
                if command is not None:
                    prev_command = command
                time = 0
                pygame.display.update()
                self.display.surface.fill((0, 0, 0))

    def update_pos(self, position):
        if position:
            self.direction_update = (position[0], position[1])
        self.cordinates[0] += self.direction_update[0]
        self.cordinates[1] += self.direction_update[1]
        self.boarder_chekup()
        if position:
            return position[2]
        return None

    def collisions(self, snake_group, rewards_group, input_commands):
        runing = True
        new_bite = Snake(40, self.cordinates, self.points +
                         6, self.direction_update)
        if pygame.sprite.spritecollide(new_bite, rewards_group, True):
            if len(rewards_group) < 1:
                rewards_group.add(return_asset(
                    snake_group, Coin(), Apple(), 2))
            self.time_untill_speedup -= 4
            self.points += 1
        if pygame.sprite.spritecollide(new_bite, snake_group, True):
            runing = False
        if len(rewards_group) == 0:
            rewards_group.add(return_asset(snake_group, Coin(), Apple(), 0))
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

    def snake_dead_handler(self, eventq):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text1 = font.render('You Died :(', True, (255, 255, 255), (0, 0, 0))
        text2 = font.render("your points: "+str(self.points),
                            True, (255, 255, 255), (0, 0, 0))
        data = ScoreUploader().get_highscores()
        text3 = font.render(
            "Highscore: " + str(data[0]) + ", User: " + str(data[1]), True, (255, 255, 255), (0, 0, 0))
        texts = [text1, text2, text3]
        while True:
            offset = -50
            for text in texts:
                textRect = text.get_rect()
                textRect.center = (
                    self.window_size[0] // 2, (self.window_size[1] // 2) + offset)
                self.display.surface.blit(text, textRect)
                offset += 50
            pygame.display.update()
            if eventq.get_event(pygame.event.get()) == False:
                break
        ScoreUploader().upload_score(self.points, "TESTI-VISA")
        self.display.quit()

    def initializer(self):
        pass


if __name__ == "__main__":
    testi = Game((800, 600), 40)
    testi.game_loop()
