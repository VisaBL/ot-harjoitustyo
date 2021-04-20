import pygame
from image_loader import image_load as im


class Snake(pygame.sprite.Sprite):
    def __init__(self, size, cordinates, life, direciton):
        pygame.sprite.Sprite.__init__(self)
        self.dir = direciton
        self._life = life
        self.size = size
        self.image = self._image_setter()
        self.rect = self.image.get_rect()
        self.rect.center = cordinates

    def update(self):
        self._life -= 1
        if self._life < 1:
            self.kill()
        return self._life

    def _image_setter(self):
        texture = im("snake")
        if self.dir[0] == -self.size:
            deg = 90
        elif self.dir[0] == self.size:
            deg = 270
        elif self.dir[1] == -self.size:
            deg = 0
        elif self.dir[1] == self.size:
            deg = 180
        return pygame.transform.rotate(texture, deg)


if __name__ == "__main__":
    pass
