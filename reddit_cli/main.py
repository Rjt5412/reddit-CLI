import typer
from rich import print
from .login import (
    get_creds_config,
    get_auth_access_token,
    retrieve_auth_token,
    save_access_token,
)

app = typer.Typer()


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
    if retrieve_auth_token() is not None:
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
            save_access_token(auth_dict)
            typer.echo("Auth token generated. User logged in!")


if __name__ == "__main__":
    app()
