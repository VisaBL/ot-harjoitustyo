import os
import pygame
import csv

dirname = os.path.dirname(__file__)


def image_load(asset):
    try:
        return pygame.image.load(os.path.join(dirname, "assets", asset+".png"))
    except:
        print("Asset does not exist")
        return None

# Funktio luo kansion pref, sekä luo tiedoston, jos sitä ei ole oleassa.


def csv_load(table, data):
    mode = "a"
    path = os.path.join(dirname, "pref", table+".csv")
    if not os.path.exists("pref"):
        os.makedirs("pref")
    if not os.path.isfile(path):
        print(os.path.isfile(path))
        mode = "w"
    with open(path, mode) as table:
        writer = csv.writer(table)
        if data:
            writer.writerow(data)


def return_path(file):
    path = os.path.join(dirname, "pref", file+".csv")
    if not os.path.isfile(path):
        return None
    else:
        return path
# testejä varetn toimito, jolla voi poistaa


def remove_pref(files: list):
    for file in files:
        path = os.path.join(dirname, "pref", file+".csv")
        os.remove(path)
    try:
        os.rmdir("pref")
    except OSError:
        print("Couldn't delete folder")


if __name__ == "__main__":
    csv_load("scores", ["69", "l-User", "Today"])
    remove_pref(["scores"])
