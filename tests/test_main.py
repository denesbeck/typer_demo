from typer.testing import CliRunner

import main

runner = CliRunner()


def test_app():
    result = runner.invoke(main.app, ["goodbye", "--formal", "Denes"])
    assert result.exit_code == 0
    assert "Goodbye Mr. Denes. Have a good day."
