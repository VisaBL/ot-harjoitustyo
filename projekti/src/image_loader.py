import os
import pygame

dirname = os.path.dirname(__file__)


def image_load(asset):
    return pygame.image.load(os.path.join(dirname, "assets", asset+".png"))
