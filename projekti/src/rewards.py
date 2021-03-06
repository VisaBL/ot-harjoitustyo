from random import randint
import pygame
from file_loader import image_load


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load("coin")
        self.rect = self.image.get_rect()
        self.rect.center = (10, 10)


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load("apple")
        self.rect = self.image.get_rect()
        self.rect.center = 10, 10
        self._life = (randint(9, 17))
        self._life_in_start = self._life

    def update(self):
        self._life -= 1
        if self._life < 1:
            self.kill()

    def return_life(self):
        return self._life, self._life_in_start

# Palauttaa Sprite-ryhmän: rewards ja tarkistaa törmäykset madon sekä muiden palkintojen kanssa


def return_asset(snake_group, asset, asset2, block_size, resolution):
    """Will check collisions with the snake and return the sprites,
        also monitos that the spawned sprites wont collide 
    Args:
        snake_group (Pygame.sprite.Group): [The group for snake blocks to check collisions ]
        asset (Sprite): [The main reward for the snake]
        asset2 (Additional_sprite): [Additional bonus reward, won't be dispatched if none ]
        block_size (int): [size of the single block]
        resolution (tuple): [Size of the window]
    Returns:
        pygame.sprite.Group: Returns the group containing sprites 
    """
    group = pygame.sprite.Group()
    group.add(asset)
    if _randomaattor(2) and asset2 is not None:
        group.add(asset2)
    while True:
        if pygame.sprite.groupcollide(group, snake_group, False, False) or asset.rect.center == (10, 10):
            lista = []
            for item in group:
                _asset_placer(item, resolution, block_size)
                while True:
                    if item.rect.center in lista:
                        _asset_placer(item, resolution, block_size)
                    if item.rect.center not in lista:
                        break
                lista.append(asset.rect.center)
        else:
            break
    return group


def _asset_placer(asset, resolution, block_size):
    margin = block_size/2
    x_axis = resolution[0] // block_size
    y_axis = resolution[1] // block_size
    asset.rect.center = (randint(1, x_axis-1)*block_size+margin,
                         randint(1, y_axis-1)*block_size+margin)


def _randomaattor(probability):
    value = randint(1, probability)
    if value == 1:
        return True
    return False
