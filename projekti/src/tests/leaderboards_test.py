import unittest
from leaderboard_uploader import ScoreUploader


class Tests(unittest.TestCase):
    def setUp(self):
        self.score_upper = ScoreUploader()

    def test_return_highscore_from_cloud(self):
        self.score_upper.upload_score(1009, "Unittest", False)
        data = self.score_upper.get_highscores_from_drive(1)
        self.score_upper.delete_first_colum()
        self.assertEqual(['1009', "Unittest"], data[0][0:2])
