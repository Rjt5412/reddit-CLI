from typing import Dict, List
from .utils import get_api_response, prune_subscribed_response


def get_subscribed_subreddits(auth_token: str, user_agent: str) -> List:
    url = "https://oauth.reddit.com/subreddits/mine/subscriber"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    payload = {"raw_json": "1"}
    response = get_api_response(url=url, headers=headers, payload=payload)
    subscribed_subreddits = prune_subscribed_response(response)
    return subscribed_subreddits
