from typing import Dict
import webbrowser
import typer
from rich.console import Console
from rich.table import Table
from .login import retrieve_auth_creds
from .utils import get_api_response

app = typer.Typer()
console = Console()


def get_profile_prefs(auth_token: str, user_agent: str) -> Dict:
    url = "https://oauth.reddit.com/api/v1/me/prefs"
    headers = {"Authorization": f"bearer {auth_token}", "User-Agent": user_agent}
    prefs_dict = get_api_response(url=url, headers=headers)
    return prefs_dict


def update_prefs():
    webbrowser.open_new_tab("https://reddit.com/prefs")


@app.command()
def prefs():
    # Get token if it exists
    auth_token, user_agent = retrieve_auth_creds()
    if auth_token is None or user_agent is None:
        print("[red]User not logged in.[/red].")
        raise typer.Abort()
    subreddit_dict = get_profile_prefs(auth_token, user_agent)

    # Print the prefs as a pretty table
    table = Table("Preference", "Value")
    for key, value in subreddit_dict.items():
        table.add_row(str(key), str(value))

    console.print(table)


@app.command()
def update_prefs():
    typer.echo("Redirecting to reddit preferences page on web browser.")
    update_prefs()
