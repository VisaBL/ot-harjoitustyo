import pygame
import random
import os
import snake


dirname = os.path.dirname(__file__)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(dirname, "assets", "coin.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50,550), random.randint(50,500))


# Palauttaa Sprite-ryhmän: coin 

    def return_coin():
        coin = Coin()
        coin_group = pygame.sprite.GroupSingle()
        coin_group.add(coin)
        return coin_group
    