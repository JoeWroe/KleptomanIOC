from hamcrest import assert_that, contains_string

import src.service.printer as printer_svc

class TestPrinterService():

    def test_should_print_asscii_art_to_std_out(self, capsys):
        printer_svc.asscii_art("src/asscii/banner.txt")

        result = capsys.readouterr()

        with open("src/asscii/banner.txt", "r") as input_file:
            expected_output = input_file.read()

        assert_that(result.out, contains_string(expected_output))
        assert_that(result.err, contains_string(""))


