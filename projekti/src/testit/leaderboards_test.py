import csv
import unittest
import pygame
from services.leaderboard_uploader import ScoreUploader
from file_loader import csv_load, remove_pref, image_load


class Tests(unittest.TestCase):
    def setUp(self):
        self.score_upper = ScoreUploader()

    def test_upload_and_return_highscore_from_cloud(self):
        self.score_upper.upload_score(1009, "Unittest", False)
        data = self.score_upper.get_highscores_from_drive(1)
        self.score_upper.delete_first_colum()
        self.assertEqual(['1009', "Unittest"], data[0][0:2])

    def test_local_score_saver(self):
        remove_pref(["scores"])
        data = ["999", "TESTI", "5.5.2021"]
        csv_load("scores", data)
        scores = self.score_upper.get_highscores(1)
        self.assertEqual(scores[0], data)

    def test_image_loader(self):
        state = isinstance(image_load("coin"), pygame.Surface)
        self.assertEqual(True, state)

    def test_image_loader_invalid_input_returns_none(self):
        state = image_load("coinZzZR")
        self.assertEqual(None, state)
