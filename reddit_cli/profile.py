from typing import Dict
from .utils import get_api_response_post
import webbrowser


def get_profile_prefs(auth_token: str) -> Dict:
    url = "https://oauth.reddit.com/api/v1/me/prefs"
    headers = {"Authorization": f"bearer {auth_token}"}
    prefs_dict = get_api_response_post(url=url, headers=headers)
    return prefs_dict


def update_prefs():
    webbrowser.open_new_tab("https://reddit.com/prefs")
