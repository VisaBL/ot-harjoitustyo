import pygame
import pygame_gui
from ui.draw_window import DrawWindow
from services.leaderboard_uploader import ScoreUploader
from random import choice


class Menu():
    def __init__(self, resolution, eventqueue, display):
        self.resolution = resolution
        self.display = display
        self.clock = pygame.time.Clock()
        self.eventqueue = eventqueue

    def main_menu(self, game):
        self.display.refresh()
        gui = pygame_gui.UIManager(self.resolution)
        center = self.resolution[0] // 2 - 150//2
        hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center, 180), (150, 50)),
                                                    text='START THE GAME',
                                                    manager=gui)

        scores_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center, 250), (150, 50)),
                                                     text='LOAD HIGHSCORES',
                                                     manager=gui)

        settigns_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center, 320), (150, 50)),
                                                       text='OPTIONS',
                                                       manager=gui)

        exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center, 390), (150, 50)),
                                                   text='QUIT',
                                                   manager=gui)

        while True:
            self.display.text_to_screen(
                "The Snake Game", (self.resolution[0]//2, 80), 40)
            running = True
            time_delta = self.clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == hello_button:
                            print('Here we go!')
                            game.game_loop(self.display, self.eventqueue)

                        elif event.ui_element == exit_button:
                            print('Adios!!')
                            running = False
                        elif event.ui_element == scores_button:
                            self.display.text_to_screen(
                                "Loading Data", (self.resolution[0]//2, 120), 30)
                            self.highscore_display()
                        elif event.ui_element == settigns_button:
                            self.settings(center)
                gui.process_events(event)
                self.display.draw_gui(gui, time_delta)

            if not running:
                self.display.quit()
                break

    def highscore_display(self):
        running = True
        time_delta = self.clock.tick(60)/1000.0
        gui = pygame_gui.UIManager(self.resolution)
        datasource = ScoreUploader()
        local_data = datasource.get_highscores(5)
        cloud_data = datasource.get_highscores_from_drive(5)
        h_margin = 130
        exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 390), (150, 50)),
                                                   text='BACK TO MENU',
                                                   manager=gui)

        for alkio in local_data:
            info = f'{alkio[0]}; {alkio[1]}; {alkio[2][0:10]}'
            textbox = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((40, h_margin), (200, 50)),
                                                           text=info,
                                                           manager=gui)
            h_margin += 70
        h_margin = 130
        for alkio in cloud_data:
            info = f'{alkio[0]}; {alkio[1]}; {alkio[2][0:10]}'
            textbox = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((570, h_margin), (200, 50)),
                                                           text=info,
                                                           manager=gui)
            h_margin += 70
        self.display.refresh()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.display.quit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == exit_button:
                            running = False
                gui.process_events(event)
            if not running:
                break
            self.display.draw_gui(gui, time_delta)
            self.display.text_to_screen("local Highscores", (150, 80), 40)
            self.display.text_to_screen(
                "Online Leaderboards", (self.resolution[0]-150, 80), 40)
        self.display.refresh()

    def snake_dead_handler(self, points):
        center = self.resolution[0] // 2 - 150//2
        gui = pygame_gui.UIManager(self.resolution)
        end_texts = ["Don't try to eat your own tail",
                     "you have lost the game :(", "next time better luck", "oh, you died :(, try again!"]
        data = ScoreUploader().get_highscores(1)
        time_delta = self.clock.tick(60)/1000.0
        text2 = str("your points: "+str(points))
        text3 = str("Highscore: " + str(data[0][0]) + ", User: " + str(
            data[0][1]))
        texts = [text2, text3]
        back_to_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.resolution[0]/2 - 90, self.resolution[1]-100), (180, 50)),
                                                    text='RETURN TO MAIN MENU ',
                                                    manager=gui)
        end_text = choice(end_texts)
        name_box_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((center, 450), (150, 50)),
                                                                                manager=gui)

        while True:
            self.clock.tick(30)
            running = True
            offset = -50
            for text in texts:
                rect = pygame.Rect(
                    ((self.resolution[0] // 2 - 150), 150 + offset), (300, 90))
                pygame_gui.elements.ui_label.UILabel(rect, text, gui)
                offset += 110
                self.display.draw_gui(gui, time_delta)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_to_menu:
                            running = False
                gui.process_events(event)
            if not running:
                break
            self.display.text_to_screen(
                end_text, (self.resolution[0]//2, 50), 50)
        input = name_box_entry.get_text()
        self.display.text_to_screen(
            "Saving scores :)", (self.resolution[0]//2, self.resolution[1]-30), 40)
        ScoreUploader().upload_score(points, input, True)
        self.display.refresh()

    def settings(self, center):
        self.display.refresh()
        gui = pygame_gui.UIManager(self.resolution)
        exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center, 400), (150, 50)),
                                                   text='BACK TO MENU',
                                                   manager=gui)
        name_box_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((center, 250), (150, 50)),
                                                                                manager=gui)
        while True:
            running = True
            time_delta = self.clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.display.quit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == exit_button:
                            running = False
                gui.process_events(event)
            if not running:
                self.display.refresh()
                break
            self.display.draw_gui(gui, time_delta)
            self.display.text_to_screen("Preferences", (150, 80), 40)
        input = name_box_entry.get_text()
        print(input)


if __name__ == "__main__":
    pass
