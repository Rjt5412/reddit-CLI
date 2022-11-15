import unittest
from reddit_cli.login import get_config_json, get_auth_access_token
import json
import os


class Tests(unittest.TestCase):
    def test_get_config_json(self):
        val_dict = {"client_id": "abcd", "client_secret": "abcd"}
        home_dir = os.getenv("HOME")

        with open(f"{home_dir}/reddit_config.json", "w") as f:
            json.dump(val_dict, f)

        test_dict = get_config_json()

        self.assertDictEqual(test_dict, val_dict)

    # TODO
    def test_get_auth_access_token(self):
        pass
