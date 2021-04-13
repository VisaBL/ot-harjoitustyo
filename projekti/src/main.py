import pygame
from snake import Snake
from coin import Coin
from draw_window import Draw_window
from event_queue import Eventqueue

class Game():
    def __init__(self):
        self.display = Draw_window(600,600)
        self.clock = pygame.time.Clock()
        self.eventq = Eventqueue()
        self.len = 8
        self.points = 0 
        self.x = 120
        self.y = 120
        self.x_dir = 30
        self.y_dir = 0 
        self.snake_group = pygame.sprite.Group()
        self.coin_group = Coin.return_coin()

    def game_loop(self):
        time = 0 
        while True:
            self.clock.tick(60)
            self.display.surface.fill((0,0,0))
            self.eventq.get_event() 
            time += (self.clock.get_time())
            if time > 300:
                self.update()
                time = 0 
            self.snake_group.draw(self.display.surface)
            self.coin_group.draw(self.display.surface)
            pygame.display.flip()

    def update(self):
        position = self.eventq.return_event()
        if position != None:
            self.x_dir = position[0]
            self.y_dir = position[1]
        self.x += self.x_dir
        self.y += self.y_dir
        new_bite = Snake(30,self.x,self.y, self.len)
        for snake in self.snake_group:
            if pygame.sprite.spritecollideany(snake, self.coin_group):
                for koin in self.coin_group:
                    koin.kill() 
                    self.coin_group = Coin.return_coin()
                self.len += 1 
                self.points += 1
            if pygame.sprite.spritecollide(new_bite, self.snake_group, True):
                print("You Died :( ... Your points are", self.points)
                pygame.quit()
            snake.update()
        self.snake_group.add(new_bite)

if __name__ == "__main__":
    testi = Game()
    testi.game_loop()
