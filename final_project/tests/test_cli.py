"""tests the Cli class"""

from unittest import mock
from cli import Cli
import io
import unittest


class TestCli(unittest.TestCase):
    """tests the Cli class"""

    def test_run_cli(self) -> None:
        """This tests the cli """
        Cli.reset_instance()
        user_input = ("1\nwh1\n1\nwh2\n2\napple\n1\nwh1\n3\n2\n"
                      "rice\n2\nwh1\n2\n3\nwh1\napple\nwh2\n4\n"
                      "wh2\napple\n5\nwh2\n6\n7\nwh1\n8\nrice\n"
                      "3\n0\n")
        with mock.patch('rich.console.Console.print') as new_console:
            with mock.patch('sys.stdin', io.StringIO(user_input)):
                Cli().run_cli()
                new_console.assert_called()

    def test_instance(self) -> None:
        """tests get/reset_instance"""

        Cli.reset_instance()

        self.assertIsNone(Cli.get_instance())

        _ = Cli()

        try:
            _ = Cli()

        except NameError:
            pass

        self.assertIsNotNone(Cli.get_instance())

    def test_exception3(self) -> None:
        Cli.reset_instance()
        user_input = ("3\nwh1\n")
        with mock.patch('rich.console.Console.print'):
            with mock.patch('sys.stdin', io.StringIO(user_input)):
                with self.assertRaises(ValueError):
                    Cli().run_cli()

    def test_exception3_2(self) -> None:
        Cli.reset_instance()
        user_input = ("1\nwh1\n2\napple\n2\nwh1\n2\n3\nwh1\napple\nwh2\n")
        with mock.patch('rich.console.Console.print'):
            with mock.patch('sys.stdin', io.StringIO(user_input)):
                with self.assertRaises(ValueError):
                    Cli().run_cli()

    def test_exception4(self) -> None:
        Cli.reset_instance()
        user_input = ("4\nwh1\n")
        with mock.patch('rich.console.Console.print'):
            with mock.patch('sys.stdin', io.StringIO(user_input)):
                with self.assertRaises(ValueError):
                    Cli().run_cli()

    def test_exception7(self) -> None:
        Cli.reset_instance()
        user_input = ("7\nwh1\n")
        with mock.patch('rich.console.Console.print'):
            with mock.patch('sys.stdin', io.StringIO(user_input)):
                with self.assertRaises(ValueError):
                    Cli().run_cli()

    def test_exception8(self) -> None:
        Cli.reset_instance()
        user_input = ("1\nwh1\n2\napple\n2\nwh1\n2\n8\ngrapes\n3\n")
        with mock.patch('rich.console.Console.print'):
            with mock.patch('sys.stdin', io.StringIO(user_input)):
                with self.assertRaises(ValueError):
                    Cli().run_cli()
