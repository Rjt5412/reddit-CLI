from os import getenv, path
import json
from typing import Dict
import requests


AUTH_REQUEST_URL = "https://www.reddit.com/api/v1/access_token"


def get_creds_config() -> Dict:
    """
    Get the locally stored credentials expected under ${HOME}/reddit_config.json
    Returns JSON file as a dictionary
    """
    config_dict = None

    home_dir = getenv("HOME")
    config_file = f"{home_dir}/reddit_config.json"

    # Check and open the config file
    if path.exists(config_file):
        with open(config_file, "r") as f:
            json_contents = f.read()
        config_dict = json.loads(json_contents)

    return config_dict


# TODO: Test this
def get_auth_access_token(config: Dict, username: str, password: str) -> Dict:
    client_auth = requests.auth.HTTPBasicAuth(
        config["client_id"], config["client_secret"]
    )
    post_data = {"grant_type": "password", "username": username, "password": password}
    headers = {"User-Agent": f"reddit-cli/0.1 by {username}"}
    response = requests.post(
        url=AUTH_REQUEST_URL, auth=client_auth, data=post_data, headers=headers
    )
    return response.json()
