import os
import time

from typing import List


def asscii_art(filename: str) -> None:
    file = open(filename, "r")
    print("".join([line for line in file]))


def flashing_asscii_art(filenames: List[str]) -> None:
    os.system("clear")

    frames = []

    for filename in filenames:
        with open(filename, "r") as file:
            frames.append(file.readlines())

    for playthrough in range(5):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.5)
            os.system("clear")
