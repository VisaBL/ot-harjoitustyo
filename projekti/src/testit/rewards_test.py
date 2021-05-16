import unittest
import pygame
from rewards import Coin, Apple, return_asset
from snake import Snake


class Tests(unittest.TestCase):
    def setUp(self):
        self.cordinates = (0, 40)
        self.rewards_group = pygame.sprite.Group()
        self.snake_group = pygame.sprite.Group(
            Snake(40, self.cordinates, 10, (0, 40)))

    def test_return_asset_function_returns_asset_that_does_not_collide_with_snake(self):
        for i in range(10):
            group = return_asset(self.snake_group, Coin(),
                                 None, 40, (120, 120))
            for asset in group:
                location = asset.rect.center
            self.assertNotEqual(self.cordinates, location)

    def test_return_asset_will_return_varying_reward_sprites(self):
        test = True
        for _ in range(100):
            group = return_asset(self.snake_group, Coin(),
                                 Apple(), 40, (200, 200))
            lista = []
            for asset in group:
                lista.append(asset.rect.center)
            if len(lista) > 1:
                if lista[0] == lista[1]:
                    test = False
                    print(lista)
        self.assertEqual(True, test)
