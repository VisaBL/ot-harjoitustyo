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
                lives = snake.update(None)
        self.assertEqual(2, lives[0])

    def test_snake_bit_is_still_alive(self):
        snake = Snake(50, (30, 30), 4, (40, 0))
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

    def test_snake_turn_setter_works_if_turn(self):
        snake = Snake(40, (30, 30), 10, (-40, 0))
        result = snake.update(("U", "R"))
        self.assertEqual(("U", "R"), result[1])

    def test_snake_turn_setter_returns_none_if_not_turn(self):
        snake = Snake(40, (30, 30), 10, (-40, 0))
        result = snake.update(("L", None))
        self.assertEqual(None, result[1])
