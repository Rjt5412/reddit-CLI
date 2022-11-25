from typing import Dict, List
from .utils import get_api_response, prune_subreddit_listing


def get_subscribed_subreddits(auth_token: str, user_agent: str) -> List:
    url = "https://oauth.reddit.com/subreddits/mine/subscriber"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    payload = {"raw_json": "1"}
    response = get_api_response(url=url, headers=headers, payload=payload)
    subscribed_subreddits = prune_subreddit_listing(response)
    return subscribed_subreddits


def get_new_subreddits(auth_token: str, user_agent: str) -> List:
    url = "https://oauth.reddit.com/subreddits/new"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    payload = {"raw_json": "1"}
    response = get_api_response(url=url, headers=headers, payload=payload)
    new_subreddits = prune_subreddit_listing(response)
    return new_subreddits


def get_popular_subreddits(auth_token: str, user_agent: str) -> List:
    url = "https://oauth.reddit.com/subreddits/popular"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    payload = {"raw_json": "1"}
    response = get_api_response(url=url, headers=headers, payload=payload)
    popular_subreddits = prune_subreddit_listing(response)
    return popular_subreddits


def get_subreddits_searched(auth_token: str, user_agent: str, search_str: str) -> List:
    url = "https://oauth.reddit.com/subreddits/search"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    payload = {"raw_json": "1", "q": search_str}
    response = get_api_response(url=url, headers=headers, payload=payload)
    searched_subreddits = prune_subreddit_listing(response)
    return searched_subreddits
