from hamcrest import assert_that
from matchmock import called_once

import src.service.printer as printer_svc

from src.kleptomanioc import Kleptomanioc

class TestKleptomaniac():

    def test_should_call_the_asscii_printer(self, mocker):
        mocker.patch("src.service.printer.asscii_art")

        Kleptomanioc().run()

        assert_that(printer_svc.asscii_art, called_once())
