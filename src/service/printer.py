class PrinterService:

    def asscii_art(self, filename: str) -> None:
        file = open(filename, "r")
        print("".join([line for line in file]))
