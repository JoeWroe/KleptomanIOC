from hamcrest import assert_that
from matchmock import called_once
from mock import patch

import src.service.printer as printer_svc

from src.kleptomanioc import Kleptomanioc
from src.service.argument import ArgumentService
from src.service.printer import PrinterService

class TestKleptomaniac:

    @patch.object(ArgumentService, "parse")
    @patch.object(PrinterService, "asscii_art")
    def test_should_call_the_asscii_printer(self, mock_parse, mock_asscii_art):
        arg_svc = ArgumentService()
        print_svc = PrinterService()

        Kleptomanioc().run()

        assert_that(print_svc.asscii_art, called_once())
        assert_that(arg_svc.parse, called_once())
