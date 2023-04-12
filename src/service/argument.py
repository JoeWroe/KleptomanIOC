import argparse

class ArgumentService:

    def parse(self):
        parser = argparse.ArgumentParser(
                prog="KleptomanIOC",
                description="KleptomanIOC",
                usage=argparse.SUPPRESS,
                formatter_class=self._make_wide(argparse.HelpFormatter, w=140, h=60)
            )
        parser._optionals.title = f"Optional Arguments"
        parser.add_argument("-s", "--some-arg", help="Some argument help.")

        return parser.parse_args()


    def _make_wide(self, formatter, w=120, h=36):
        """Return a wider HelpFormatter, if possible."""
        try:
            # https://stackoverflow.com/a/5464440
            # beware: "Only the name of this class is considered a public API."
            kwargs = {'width': w, 'max_help_position': h}
            formatter(None, **kwargs)
            return lambda prog: formatter(prog, **kwargs)
        except TypeError:
            print("argparse help formatter failed, falling back.")
            return formatter


