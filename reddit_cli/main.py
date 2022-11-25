import typer
from rich import print
from rich.table import Table
from rich.console import Console
from .login import (
    get_creds_config,
    get_auth_access_token,
    retrieve_auth_creds,
    save_access_token,
)
from .profile import get_profile_prefs, update_prefs
from .subreddit import get_subscribed_subreddits

app = typer.Typer()
console = Console()


@app.callback()
def callback():
    """
    Reddit CLI
    """


@app.command()
def login(
    username: str,
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    auth_token, _ = retrieve_auth_creds()
    if auth_token is not None:
        print("[green]User already logged in[/green] :thumbsup:")
    else:
        config = get_creds_config()
        if not config:
            typer.echo(
                "Config JSON with credentials not found. Refer documentation to create this file before login"
            )
            raise typer.Abort()
        else:
            auth_dict = get_auth_access_token(config, username, password)
            save_access_token(auth_dict, username)
            typer.echo("Auth token generated. User logged in!")


@app.command()
def profile_prefs():
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
def update_profile_prefs():
    typer.echo("Redirecting to reddit preferences page on web browser.")
    update_prefs()


@app.command()
def subreddit_subscribed():
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
