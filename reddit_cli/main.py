import typer
from login import get_config_json, get_auth_access_token


app = typer.Typer()


@app.callback
def callback():
    pass


@app.command
def login(
    username: str,
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    # TODO: Prompt and return if auth token already exists and not expired

    # TODO:
    # 2. Send the request for auth access token
    # 3. Generate the expiration timestamp and add it to token json to be stored
    # 4. Store the access token locally under $HOME/.reddit-config

    config = get_config_json()
    auth_token = get_auth_access_token(config, username, password)
