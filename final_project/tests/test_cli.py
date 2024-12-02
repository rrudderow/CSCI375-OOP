from unittest import mock
from cli import Cli
import io
import unittest


class TestCli(unittest.TestCase):

    def test_run_cli(self) -> None:
        """This tests the cli """
        Cli.reset_instance()
        user_input = ("1\nwh1\n1\nwh2\n2\napple\n1\nwh1\n3\n2\n"
                      "rice\n2\nwh1\n2\n"
                      "3\nwh1\napple\nwh2\n4\nwh2\napple\n5\nwh2\n"
                      "6\n7\nwh1\n8\nrice\n3\n0\n")
        with mock.patch('rich.console.Console.print') as new_console:
            with mock.patch('sys.stdin', io.StringIO(user_input)):
                Cli().run_cli()
                new_console.assert_called()

    def test_get_instance(self) -> None:
        """tests get_instance"""

        Cli.reset_instance()

        self.assertIsNone(Cli.get_instance())

        _ = Cli()

        try:
            _ = Cli()

        except NameError:
            pass

        self.assertIsNotNone(Cli.get_instance())
