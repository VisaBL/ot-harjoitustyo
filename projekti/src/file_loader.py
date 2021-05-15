import os
import csv
import pygame

dirname = os.path.dirname(__file__)


def image_load(asset):
    """[will load and return image from the asset folder]

    Args:
        asset (string): [name of the image]

    Returns:
        [pygame.image]: [texture for the sprite, if file not found returns None]
    """
    try:
        return pygame.image.load(os.path.join(dirname, "assets", asset+".png"))
    except FileNotFoundError:
        print("Asset does not exist")
        return None

# Funktio luo kansion pref, sekä luo tiedoston, jos sitä ei ole oleassa.


def csv_load(table: str, data: list):
    """[Function will load data into csv spreadsheet and write given data into it ]

    Args:
        table (str): [file name to create or to append data to ]
        data (list): [the data to be saved into the file ]
    """
    mode = "a"
    if not os.path.exists("pref"):
        os.makedirs("pref")
    path = os.path.join(dirname, "pref", table+".csv")
    if not os.path.isfile(path):
        mode = "w"
    try:
        with open(path, mode) as table:
            writer = csv.writer(table)
            if data:
                writer.writerow(data)
    except OSError:
        print("Error")

# funktio tarpeellinen huippupisteiden lataamista varten


def return_path(file):
    path = os.path.join(dirname, "pref", file+".csv")
    if not os.path.isfile(path):
        return None
    return path


def remove_pref(files: list):
    status = False
    try:
        for file in files:
            path = os.path.join(dirname, "pref", file+".csv")
            os.remove(path)
        status = True
    except FileNotFoundError:
        print("No such file found")
    try:
        os.rmdir("pref")
    except FileNotFoundError:
        print("No such Folder/or other files in folder")
    return status


if __name__ == "__main__":
    # remove_pref(["scores"])
    #csv_load("scores", ["44", "Visa", "5.5.20201"])
    print(image_load("coin"))
