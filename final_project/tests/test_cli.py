"""

from unittest import mock
from cli import Cli


def test_run_cli() -> None:
    """"""This tests the cli """"""

    with (mock.patch('rich.console.Console.print') as new_console,
            mock.patch('sys.stdin') as test_input):

        test_input.readline.side_effect = ["1", "wh1", "2", "apple", "1", "wh1", "0"]
        Cli().run_cli()
        new_console.assert_called()


        # test_input.readline.side_effect = ["2", "apple", "1", "wh1", "0"]
        # Cli().run_cli()
        # new_console.assert_called()
"""