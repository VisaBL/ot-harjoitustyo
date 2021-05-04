import pygame
import pygame_gui
from draw_window import DrawWindow
from leaderboard_uploader import ScoreUploader


class Menu():
    def __init__(self, resolution, game):
        self.resolution = resolution
        self.display = DrawWindow(resolution)
        self.clock = pygame.time.Clock()
        self.gui = pygame_gui.UIManager(resolution)
        self.game = game
        self.gui.set_visual_debug_mode(False)

    def main_menu(self):
        hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 180), (150, 50)),
                                                    text='START THE GAME',
                                                    manager=self.gui)

        scores_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (150, 50)),
                                                     text='LOAD HIGHSCORES',
                                                     manager=self.gui)

        settigns_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 320), (150, 50)),
                                                       text='OPTIONS',
                                                       manager=self.gui)

        exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 390), (150, 50)),
                                                   text='QUIT',
                                                   manager=self.gui)

        while True:
            time_delta = self.clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.display.quit()

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == hello_button:
                            print('Here we go!')
                            self.game.game_loop()
                        elif event.ui_element == exit_button:
                            print('Adios!!')
                            self.display.quit()
                        elif event.ui_element == scores_button:
                            self.highscore_display(time_delta)
                self.gui.process_events(event)
            self.refresh(time_delta)

    def highscore_display(self, time_delta):
        datasource = ScoreUploader()
        local_data = datasource.get_highscores(5)
        cloud_data = datasource.get_highscores_from_drive(5)
        self.refresh(time_delta)
        h_margin = 130
        for alkio in local_data:
            info = f'{alkio[0]}; {alkio[1]}; {alkio[2][0:10]}'
            textbox = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((40, h_margin), (200, 50)),
                                                           text=info,
                                                           manager=self.gui)
            self.refresh(time_delta)
            h_margin += 70
        h_margin = 130
        for alkio in cloud_data:
            info = f'{alkio[1]}; {alkio[0]}; {alkio[2][0:10]}'
            textbox = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((570, h_margin), (200, 50)),
                                                           text=info,
                                                           manager=self.gui)
            self.refresh(time_delta)
            h_margin += 70

    def refresh(self, time):
        self.gui.update(time)
        self.gui.draw_ui(self.display.surface)
        self.display.refresh()


if __name__ == "__main__":
    luokka = Menu((800, 600))
    luokka.main_menu()
