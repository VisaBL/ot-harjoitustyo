import pygame


class DrawWindow():
    def __init__(self, resolution):
        pygame.init()
        self._surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption('Snake Game')

    def refresh(self):
        pygame.display.update()
        self._surface.fill((0, 0, 0))

    def draw_to_screen(self, items_to_draw: list):
        for sprite in items_to_draw:
            sprite.draw(self._surface)
        self.refresh()

    def blit_to_screen(self, item, center):
        self._surface.blit(item, center)

    def text_to_screen(self, text: str, location: tuple, size):
        white = (0, 255, 0)
        font = pygame.font.SysFont(None, size)
        text = font.render(text, True, white, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = location
        self._surface.blit(text, text_rect)
        pygame.display.update()

    def draw_gui(self, gui, time):
        gui.draw_ui(self._surface)
        gui.update(time)
        pygame.display.update()

    def quit(self):
        pygame.quit()
