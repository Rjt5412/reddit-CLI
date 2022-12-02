import typer
from rich import print
from rich.console import Console
from .login import (
    get_creds_config,
    get_auth_access_token,
    retrieve_auth_creds,
    save_access_token,
)
from .profile import app as profile_app
from .subreddit import app as subreddit_app
from .post import app as post_app

console = Console()

app = typer.Typer()
app.add_typer(profile_app, name="profile", help="Access user profile options")
app.add_typer(
    subreddit_app,
    name="subreddit",
    help="List and search for subreddits based on specific criterion",
)
app.add_typer(
    post_app,
    name="post",
    help="Display posts from subreddits based on specific criterion",
)


@app.callback()
def callback():
    """
    REDDIT CLI
    """


@app.command()
def login(
    username: str,
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    """
    Login in username and password. User might need to login again if user token is expired.
    """
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
