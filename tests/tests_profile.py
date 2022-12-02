import unittest
from typer.testing import CliRunner
from reddit_cli.main import app

runner = CliRunner()


class TestsProfile(unittest.TestCase):
    def test_profile_prefs(self):
        result = runner.invoke(app, ["profile", "prefs"])
        self.assertEqual(result.exit_code, 0)
