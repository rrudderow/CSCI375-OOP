from unittest import mock
from cli import Cli
import io


def test_run_cli() -> None:
    """This tests the cli """

    user_input = ("1\nwh1\n1\nwh2\n2\napple\n1\nwh1\n3\n2\nrice\n2\nwh1\n2\n"
                  "3\nwh1\napple\nwh2\n4\nwh2\napple\n5\nwh2\n"
                  "6\n7\nwh1\n8\nrice\n3\n0\n")
    with mock.patch('rich.console.Console.print') as new_console:
        with mock.patch('sys.stdin', io.StringIO(user_input)):
            Cli().run_cli()
            new_console.assert_called()
        # test_input.readline.side_effect = ["2", "apple", "1", "wh1", "0"]
        # Cli().run_cli()
        # new_console.assert_called()
