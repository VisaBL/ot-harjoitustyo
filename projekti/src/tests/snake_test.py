import unittest
import pygame
from snake import Snake

class Tests(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(50, 120, 120, 4)
    def test_snake_will_update(self):
        for i in range(3):
            self.snake.update()
        self.assertEqual(1, self.snake.life)
        
