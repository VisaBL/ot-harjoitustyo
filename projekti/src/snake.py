import pygame
from file_loader import image_load as im


class Snake(pygame.sprite.Sprite):
    def __init__(self, size, cordinates, life, direciton):
        """Sprite class, that will create new snake bite

        Args:
            size (int): [Size for the snake-block]
            cordinates (tuple): [Block location for display]
            life (int): [How many update cycles the block will live]
            direciton (tuple): [Ongoing direction to set the resolution]
        """
        pygame.sprite.Sprite.__init__(self)
        self._dir = direciton
        self._life = life
        self._updates = 0
        self._size = size
        self.image = self._image_setter(im("head"))
        self.rect = self.image.get_rect()
        self.rect.center = cordinates

    def _image_setter(self, texture):
        if self._dir[0] == -self._size:
            deg = 90
        elif self._dir[0] == self._size:
            deg = 270
        elif self._dir[1] == -self._size:
            deg = 0
        elif self._dir[1] == self._size:
            deg = 180
        else:
            deg = 0
        return pygame.transform.rotate(texture, deg)

    def _set_second_block(self, commands):
        turn = None
        command_list = {("U", "L"): 90, ("L", "D"): 180,
                        ("D", "R"): 270, ("R", "U"): 0}
        command_list_flip = {("U", "R"): 90, ("R", "D"): 0,
                             ("D", "L"): 270, ("L", "U"): 180}
        if commands in command_list:
            self.image = pygame.transform.rotate(
                im("turn"), command_list[commands])
        elif commands in command_list_flip:
            image = pygame.transform.flip(im("turn"), False, True)
            self.image = pygame.transform.rotate(
                image, command_list_flip[commands])
            turn = commands
        else:
            self.image = self._image_setter(im("snake"))
        return turn

    def update(self, commands):
        """[will update the snake block life and kill the sprite if no life left]

        Args:
            command (tuple): [previously executed command, adńd current commant]

        Returns:
            [tuole]: [returns sprite snake remaining lives, and if turn has occoured or not]
        """
        event = None
        self._updates += 1
        if self._updates == 1:
            event = self._set_second_block(commands)
        self._life -= 1
        if self._life < 1:
            self.kill()
        return self._life, event


if __name__ == "__main__":
    käärme = Snake(40, (120, 120), 5, (40, 0))
