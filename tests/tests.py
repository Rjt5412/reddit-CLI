import unittest
from reddit_cli.login import get_creds_config, get_auth_access_token
import json
import os


class Tests(unittest.TestCase):
    def test_get_creds_config(self):
        val_dict = {"client_id": "abcd", "client_secret": "abcd"}
        home_dir = os.getenv("HOME")

        with open(f"{home_dir}/reddit_config.json", "w") as f:
            json.dump(val_dict, f)

        test_dict = get_creds_config()

        self.assertDictEqual(test_dict, val_dict)

    def test_get_creds_config_empty(self):
        # Test to see if None is returned if local credentials config is not found

        home_dir = os.getenv("HOME")
        filename = f"{home_dir}/reddit_config.json"
        os.remove(filename)

        test_dict = get_creds_config()

        self.assertEqual(test_dict, None)

    # TODO
    def test_get_auth_access_token(self):
        pass
