from datetime import datetime
import csv
import gspread
from file_loader import csv_load, return_path

# private keyn tallentaminen ideaalisesti erittäin huono idea. Kuitenkin tällä tilillä on hyvin rajatut oikeudet siihen, mitä se voi tehdä
credintentials = {
    "type": "service_account",
    "project_id": "ohtu2021",
    "private_key_id": "4985d0186c1d44b6d63fd7c21e1b65ed49bdf190",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCYbDT4h+exgGlU\ntb7SFUkGmTvT00/cGt00yK36xhiQ6HKJyt5ZkurtsmGSvEVCHYKpPE1bQYu8rWuv\nZ70UBH3al2YtK1ZK7yd2dsFbvSI4AFzO13llI4uv03aWQL8oo/e/x4P15IA0Qs8M\n135t3XdrQfgZxXa2AK9r8+SnYGKgBKEQwwx5B490D7THgWXOr9rU6WfILS5GuHd9\n9cVwX+mxo2IiKiDkyHwV2QwhdBxvTgIr6dAFP+1fa9Pu7jO3P+roD5VuwTKdJqVC\ngMWWbDQfo83tN7T7zraR/eWCpWjVA0oMk+tAagIc+k8Alo07BywGLFjtE6b4bKHI\nP9L/gj9NAgMBAAECggEAQrWhHWEF05b7Apskr/em5V9tYtEqM5ACXpayJn5KxCkn\n8Ay88gEuFugqcjk6KqyVwhHlXVo7mVFhPvytMTSiDGiUzJIaC2POJrfk+oy1jEME\nW3bM56n9+e8YCLy/rT7OML5Wj+j4/2Z6DgnGiLkUCfpuZoEY6qE0JZAx89tobtXK\nfuvaolGggcPecvYmfNUG93z2nlRkmBidveCS4kFBfBzb6wlzAfigoAdK8T6K5PA+\nwj4Ex8Z3aTB/1yT+4x6S48dfFulfbxYG9ZHONoE4Vp/WwyUG5w6iCot1MATxfcv1\nmCkGLlgcnuGoroRTy0pCmG/JepnJIZFxAFXeTRjDNQKBgQDT3n1X2hBGJI9kRagR\nMywXV3WbgnA+p6qFUruPhl+F/T0VZALSVrdgQ2U6LbnVvMaIwGpb7tdNijPmyvmv\nPwobj65t4rJlBpWoc/50OgQhcZXG2kPw5fnMNvUF0CgBA/qwt0BC2qy1OzNFyDw3\nHqHbPU/W7NbaVQOe2+apempVkwKBgQC4K9oboiryWW566YAQ61h16sAUiWZDvIhI\nz03yPHf4jhS0r5x3hILhkhpT83JWlrni4AbNmYRTizZBzr1C94X3c6JzuIA9Ff7Y\nxUF6gxWR/57BHm6MfWKp7GKZyEQcRsLdALFp1nhqlbuUfI8Lpt5y3RCBqIcYPXZJ\nde47tawjnwKBgQDD22Gz3Po+XX3RDDOZ8txHl6o44BQzV3vjU9/fhjC4BKp7I8EY\nAOH0M1lYtvycAa7mrDmmUtzl6WShbfHzdys431I4cuDHU5b16oTHnPpEkGQNN6in\nAXIyvnszrIHOrocI5d6Z7tzJjLiRQdGogsDNk5hC7x6PJxf5uv84nNm/0QKBgEBh\npAdQ825w8PwqsEg53VyrSaZkOcmoGIRLY9YwaUgMcxSO50WonxA3wNhkHC5E1oqH\nAhnRdr61xavPl73XRY+xbrLBZqL0E3i3zCIFvP6iu16LQt393wXDytwzdAvmeKxF\nV7/F56Zq3X4U5PSPyuege+q3fTJuGfGoNjXNVnXFAoGABPyulY91CK4wQFh6RAWp\nEojpCPX+cyRw8sd22zfZXspgWMWPlCX8ACL81Tj3Xvw8SIvuIZSXfXxbEb55fAF5\nkJyARIATLrWii1U4jZz6T/9Ug77RUcLoA+gtD3KmHAuQQID1b3W0JKFBEkwmA+Sz\nReUR/LZBK84B5s9jg9bl5R0=\n-----END PRIVATE KEY-----\n",
    "client_email": "snake-game@ohtu2021.iam.gserviceaccount.com",
    "client_id": "111137526593560819093",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/snake-game%40ohtu2021.iam.gserviceaccount.com"
}


class ScoreUploader:
    def __init__(self):
        self._account = gspread.service_account_from_dict(credintentials)
        self._sheet = self._account.open_by_key(
            "1R_l6bVt1Nv4qHsrjebW5CB9oWCTRUVKSWbtS2Apcp2A")

    def upload_score(self, score: int, username: str, local: bool):
        """[will save given highscore and username into google drive and 
            to local file]

        Args:
            score (int): [The score to be uploaded to]
            username (str): [The name of the player]
            local (bool): [True if the score will be saved locally as well, mainly for the tests]

        Returns:
            [Bool]: [True if successfull, False if fails ]
        """
        data = [score, username,
                str(datetime.now().strftime("%m/%d/%Y, %H:%M"))]
        if local:
            csv_load("scores", data)
            print("saved scores locally")
        try:
            self._sheet.sheet1.insert_row(data)
            print("Uploaded score:", data)
            return True
        except:  # Couldn't get suitable expection work here :( )
            print("Random Error has occoured :(( ")
            return False

# Funktio, joka palauttaa paikalliset huippupisteet

    def get_highscores(self, count: int):
        path = return_path("scores")
        data = [["N/A", "N/A", "N/A"]]
        if path is not None:
            with open(path, "r") as data:
                reader = csv.reader(data)
                data = sorted(reader, key=lambda row: int(
                    row[0]), reverse=True)
        return data[0:count]

    def get_highscores_from_drive(self, count: int):
        try:
            data = sorted(self._sheet.sheet1.get_all_values(),
                          key=lambda row: int(row[0]), reverse=True)
        except:
            data = [["NO ", "NETWORK", "01/01/1970, 00:00"]]
            print(data)
        return data[0:count]


# funktio lähinnä testejä varten, jotta testin luoma tulos ei jää tulostaulukkon


    def delete_first_colum(self):
        sheet = self._sheet.sheet1
        try:
            sheet.delete_dimension("ROWS", 1, 1)
            return True
        except:
            return False


if __name__ == "__main__":
    luokka = ScoreUploader()
    print(luokka.get_highscores(5))
