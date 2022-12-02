import unittest
from typer.testing import CliRunner
from reddit_cli.main import app

runner = CliRunner()


class TestsPost(unittest.TestCase):
    def test_post_hot(self):
        input_subreddit = "cricket"
        result = runner.invoke(app, ["post", "hot", input_subreddit])
        self.assertEqual(result.exit_code, 0)

    def test_post_new(self):
        input_subreddit = "cricket"
        result = runner.invoke(app, ["post", "new", input_subreddit])
        self.assertEqual(result.exit_code, 0)

    def test_post_rising(self):
        input_subreddit = "cricket"
        result = runner.invoke(app, ["post", "rising", input_subreddit])
        self.assertEqual(result.exit_code, 0)

    def test_post_top(self):
        input_subreddit = "cricket"
        result = runner.invoke(app, ["post", "top", input_subreddit])
        self.assertEqual(result.exit_code, 0)

    def test_post_controversial(self):
        input_subreddit = "cricket"
        result = runner.invoke(app, ["post", "controversial", input_subreddit])
        self.assertEqual(result.exit_code, 0)
