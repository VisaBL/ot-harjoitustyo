from random import randint
import pygame
from image_loader import image_load


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load("coin")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, 200), randint(50, 200))


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_load("apple")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, 200), randint(50, 200))
        self._life = (randint(9, 17))
        self._life_in_start = self._life

    def update(self):
        self._life -= 1
        if self._life < 1:
            self.kill()

    def return_life(self):
        return self._life, self._life_in_start

# Palauttaa Sprite-ryhmän: rewards ja tarkistaa törmäykset madon sekä muiden palkintojen kanssa
# Funktio kaipaa jatkokehitystä


def return_asset(snake_group, asset, asset2, asset2_spawn_prob):
    probability = randint(0, asset2_spawn_prob)
    while True:
        if pygame.sprite.spritecollide(asset, snake_group, False):
            asset.rect.center = (randint(0, 400), randint(0, 400))
        else:
            group = pygame.sprite.Group()
            group.add(asset)
            break
    if probability == asset2_spawn_prob:
        while True:
            if pygame.sprite.spritecollideany(asset2, group, False):
                asset2.rect.center = (randint(0, 400), randint(0, 400))
            if pygame.sprite.spritecollide(asset2, snake_group, False):
                asset2.rect.center = (randint(0, 400), randint(0, 400))
            else:
                group.add(asset2)
                break
    return group


if __name__ == "__main__":
    pass
