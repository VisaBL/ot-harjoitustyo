import unittest
import pygame
from snake import Snake


class Tests(unittest.TestCase):
    def setUp(self):
        self.snake_group = pygame.sprite.Group(
            Snake(40, (120, 120), 5, (0, 40)))
        self.snake_bit = Snake(40, (120, 120), 2, (0, 40))

    def test_snake_will_update(self):
        for _ in range(3):
            for snake in self.snake_group:
                tulos = snake.update(None)
        self.assertEqual(2, tulos)

    def test_snake_bit_is_still_alive(self):
        snake = Snake(40, (30, 30), 4, (40, 0))
        group = pygame.sprite.Group(snake)
        group.update(None)
        is_alive = pygame.sprite.Sprite.alive(snake)
        self.assertEqual(True, is_alive)

    def test_snake_bit_is_dead(self):
        snake = Snake(40, (30, 30), 4, (40, 0))
        group = pygame.sprite.Group(snake)
        for i in range(6):
            group.update(None)
        is_alive = pygame.sprite.Sprite.alive(snake)
        self.assertEqual(False, is_alive)
