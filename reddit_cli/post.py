from typing import List
import typer
from rich.console import Console
from rich import print
from .login import retrieve_auth_creds
from .utils import get_api_response, prune_post_listing


app = typer.Typer()
console = Console()


def get_posts_by_criterion(
    auth_token: str, user_agent: str, subreddit: str, criterion: str
):
    url = f"https://oauth.reddit.com/r/{subreddit}/{criterion}"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    payload = {"raw_json": "1", "limit": "5"}
    response = get_api_response(url=url, headers=headers, payload=payload)
    subscribed_subreddits = prune_post_listing(response)
    return subscribed_subreddits


def print_posts(posts: List):
    for post in posts:
        print("\n")
        print("=" * 100)
        print(f"[yellow]TITLE:[/yellow] {post['title']}")
        print(f"[yellow]AWARDS:[/yellow] {post['awards']}")
        print(f"[yellow]UPVOTES:[/yellow] {post['upvotes']}")
        print(f"[yellow]DOWNVOTES:[/yellow] {post['downvotes']}")
        print(f"[yellow]COMMENTS:[/yellow] {post['comments']}")
        print(f"[yellow]TEXT:[/yellow] {post['text']}")
        print(f"[yellow]POST URL:[/yellow] {post['url']}")
        print(f"[yellow]MEDIA URL:[/yellow] {post['media_url']}")
        print("\n")
        print("=" * 100)


@app.command(
    help="List top 5 hot posts(most upvoted recently) from the subreddit mentioned"
)
def hot(subreddit: str):
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    posts = get_posts_by_criterion(auth_token, user_agent, subreddit.strip("r/"), "hot")
    print_posts(posts)


@app.command(help="List 5 recently created posts from the subreddit mentioned")
def new(subreddit: str):
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    posts = get_posts_by_criterion(auth_token, user_agent, subreddit.strip("r/"), "new")
    print_posts(posts)


@app.command(help="List top 5 rising posts from the subreddit mentioned")
def rising(subreddit: str):
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    posts = get_posts_by_criterion(
        auth_token, user_agent, subreddit.strip("r/"), "rising"
    )
    print_posts(posts)


@app.command(help="List top 5 posts(most upvoted) from the subreddit mentioned")
def top(subreddit: str):
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    posts = get_posts_by_criterion(auth_token, user_agent, subreddit.strip("r/"), "top")
    print_posts(posts)


@app.command(help="List top 5 controversial posts from the subreddit mentioned")
def controversial(subreddit: str):
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    posts = get_posts_by_criterion(
        auth_token, user_agent, subreddit.strip("r/"), "controversial"
    )
    print_posts(posts)
