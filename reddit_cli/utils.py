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


def prune_post_listing(response: Dict) -> List:
    posts = list()
    for item in response["data"]["children"]:
        post = dict()
        post["title"] = item["data"]["title"].strip("\n")
        post["text"] = item["data"]["selftext"].strip("\n")
        post["awards"] = item["data"]["total_awards_received"]
        post["upvotes"] = item["data"]["ups"]
        post["downvotes"] = item["data"]["downs"]
        post["comments"] = item["data"]["num_comments"]
        post["url"] = f"https://reddit.com{item['data']['permalink']}"

        # Check for media links
        media_url = ""
        if item["data"].get("preview"):
            if item["data"]["preview"].get("images"):
                if len(item["data"]["preview"]["images"]) > 0:
                    if item["data"]["preview"]["images"][0].get("source"):
                        if item["data"]["preview"]["images"][0]["source"].get("url"):
                            media_url = item["data"]["preview"]["images"][0]["source"][
                                "url"
                            ]
        post["media_url"] = media_url

        posts.append(post)

    return posts
