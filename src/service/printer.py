def asscii_art(filename: str) -> None:
    file = open(filename, "r")
    print("".join([line for line in file]))
