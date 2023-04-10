# pyright: reportWildcardImportFromLibrary=false

from hamcrest import *
from matchmock import *

import src.service.printer as printer_svc

from src.kleptomanioc import Kleptomanioc

def test_should_call_the_asscii_printer(mocker):
    mocker.patch("src.service.printer.asscii_art")

    Kleptomanioc().run()

    assert_that(printer_svc.asscii_art, called_once())
