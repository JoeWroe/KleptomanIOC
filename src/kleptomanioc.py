from src.service.argument import ArgumentService
from src.service.printer import PrinterService

class Kleptomanioc:

    def run(self):
        arg_svc = ArgumentService()
        print_svc = PrinterService()

        print_svc.asscii_art("src/asscii/dwarf.txt")
        arg_svc.parse()
