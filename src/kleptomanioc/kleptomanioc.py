import kleptomanioc.service.printer as print_svc


class Kleptomanioc():

    def run(self):
        print_svc.flashing_asscii_art(
                [
                    "src/kleptomanioc/asscii/dwarf.txt",
                    "src/kleptomanioc/asscii/dwarf_$_eyes.txt",
                    "src/kleptomanioc/asscii/dwarf_ioc_eyes.txt",
                ]
            )
