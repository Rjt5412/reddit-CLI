from os import getenv, path
import json
from typing import Dict
import requests
from datetime import datetime, timedelta


AUTH_REQUEST_URL = "https://www.reddit.com/api/v1/access_token"
HOME_DIR = getenv("HOME")


def get_creds_config() -> Dict:
    """
    Get the locally stored credentials expected under ${HOME}/reddit_config.json
    Returns JSON file as a dictionary with client_id and client_secret as fields
    """
    config_dict = None

    config_file = f"{HOME_DIR}/reddit_config.json"

    # Check and open the config file
    if path.exists(config_file):
        with open(config_file, "r") as f:
            json_contents = f.read()
        config_dict = json.loads(json_contents)

    return config_dict


def get_auth_access_token(config: Dict, username: str, password: str) -> Dict:
    """
    Function to make an API request and get the auth access token for the user.
    Returns: Dict with access token details
    eg: {
        "access_token":"sampletoken1",
        'token_type': 'bearer',
        'expires_in': 86400,
        'scope': '*'
    }
    """
    response = None

    client_auth = requests.auth.HTTPBasicAuth(
        config["client_id"], config["client_secret"]
    )
    post_data = {"grant_type": "password", "username": username, "password": password}
    headers = {"User-Agent": f"reddit-cli/0.1 by {username}"}
    response = requests.post(
        url=AUTH_REQUEST_URL, auth=client_auth, data=post_data, headers=headers
    )

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e)

    return response.json()


def save_access_token(auth_dict: Dict):
    """
    Add an expiration timestamp to the auth token and save it locally to ${HOME}/reddit_auth.json
    """

    # Generate expiration timestamp

    expiration_timestamp = (
        datetime.now() + timedelta(seconds=(int(auth_dict["expires_in"]) - 200))
    ).strftime("%m/%d/%Y, %H:%M:%S")
    auth_dict["expiration_timestamp"] = expiration_timestamp

    # Save Dict as JSON
    with open(f"{HOME_DIR}/reddit_auth.json", "w") as f:
        json.dump(auth_dict, f)


def retrieve_auth_token() -> str:
    """
    A function to retrieve the auth acess token if it already exists locally(as JSON)
    under ${HOME}/reddit_auth.json and is not expired
    Returns: Access token string if present else None
    """
    access_token = None

    # Read the acess token info from file
    if path.exists(f"{HOME_DIR}/reddit_auth.json"):
        with open(f"{HOME_DIR}/reddit_auth.json") as f:
            json_content = f.read()
        auth_dict = json.loads(json_content)

        if (
            "expiration_timestamp" in auth_dict.keys()
            and "access_token" in auth_dict.keys()
        ):
            now = datetime.now()
            expiration_timestamp = datetime.strptime(
                auth_dict["expiration_timestamp"], "%m/%d/%Y, %H:%M:%S"
            )
            if now < expiration_timestamp:
                access_token = auth_dict["access_token"]

    return access_token
