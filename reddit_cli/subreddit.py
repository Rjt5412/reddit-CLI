from typing import Dict, List
from .utils import get_api_response, prune_subreddit_listing
import typer
from rich.console import Console
from rich.table import Table
from .login import retrieve_auth_creds


app = typer.Typer()
console = Console()


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


@app.command()
def subscribed():
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    subreddits = get_subscribed_subreddits(auth_token, user_agent)
    table = Table("Subreddit name", "Subscribers", "Decription")
    for subreddit in subreddits:
        table.add_row(
            str(subreddit["name"]),
            str(subreddit["subscribers"]),
            str(subreddit["desc"].strip("\n")),
        )
        table.add_row("\n", "\n", "\n")
        table.add_row("=" * 15, "=" * 15, "=" * 15)
        table.add_row("\n", "\n", "\n")

    console.print(table)


@app.command()
def new():
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    subreddits = get_new_subreddits(auth_token, user_agent)

    table = Table("Subreddit name", "Subscribers", "Decription")
    for subreddit in subreddits:
        table.add_row(
            str(subreddit["name"]),
            str(subreddit["subscribers"]),
            str(subreddit["desc"].strip("\n")),
        )
        table.add_row("\n", "\n", "\n")
        table.add_row("=" * 15, "=" * 15, "=" * 15)
        table.add_row("\n", "\n", "\n")

    console.print(table)


@app.command()
def popular():
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    subreddits = get_popular_subreddits(auth_token, user_agent)
    table = Table("Subreddit name", "Subscribers", "Decription")
    for subreddit in subreddits:
        table.add_row(
            str(subreddit["name"]),
            str(subreddit["subscribers"]),
            str(subreddit["desc"].strip("\n")),
        )
        table.add_row("\n", "\n", "\n")
        table.add_row("=" * 15, "=" * 15, "=" * 15)
        table.add_row("\n", "\n", "\n")

    console.print(table)


@app.command()
def search(search_query: str):
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    subreddits = get_subreddits_searched(auth_token, user_agent, search_query)

    if len(subreddits) > 0:
        table = Table("Subreddit name", "Subscribers", "Decription")
        for subreddit in subreddits:
            table.add_row(
                str(subreddit["name"]),
                str(subreddit["subscribers"]),
                str(subreddit["desc"].strip("\n")),
            )
            table.add_row("\n", "\n", "\n")
            table.add_row("=" * 15, "=" * 15, "=" * 15)
            table.add_row("\n", "\n", "\n")

        console.print(table)
    else:
        print(f"[red]No subreddits found for query {search_query}[/red].")
