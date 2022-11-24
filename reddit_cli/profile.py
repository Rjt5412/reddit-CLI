from typing import Dict
from .utils import get_api_response
import webbrowser


def get_profile_prefs(auth_token: str, user_agent: str) -> Dict:
    url = "https://oauth.reddit.com/api/v1/me/prefs"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    prefs_dict = get_api_response(url=url, headers=headers)
    return prefs_dict


def update_prefs():
    webbrowser.open_new_tab("https://reddit.com/prefs")
