from typing import Dict, List
import requests


def get_api_response(url: str, headers: Dict, payload: Dict = None) -> Dict:
    response = requests.get(url, headers=headers, params=payload)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        response_headers = response.headers
        if "retry-after" in response_headers.keys():
            print(f"Retry after {response_headers['retry-after']}")
        raise Exception(e)

    return response.json()


def prune_subreddit_listing(response: Dict) -> List:
    subreddits = list()
    for item in response["data"]["children"]:
        subreddit = dict()
        subreddit["name"] = item["data"]["display_name_prefixed"]
        subreddit["desc"] = item["data"]["public_description"]
        subreddit["subscribers"] = item["data"]["subscribers"]
        subreddits.append(subreddit)

    return subreddits
