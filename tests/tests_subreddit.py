import unittest
from typer.testing import CliRunner
from reddit_cli.main import app

runner = CliRunner()


class TestsSubreddit(unittest.TestCase):
    def test_subreddit_subscribed(self):
        result = runner.invoke(app, ["subreddit", "subscribed"])
        self.assertEqual(result.exit_code, 0)

    def test_subreddit_new(self):
        result = runner.invoke(app, ["subreddit", "new"])
        self.assertEqual(result.exit_code, 0)

    def test_subreddit_popular(self):
        result = runner.invoke(app, ["subreddit", "popular"])
        self.assertEqual(result.exit_code, 0)

    def test_subreddit_search(self):
        search_query = "cricket"
        result = runner.invoke(app, ["subreddit", "search", search_query])
        self.assertEqual(result.exit_code, 0)
