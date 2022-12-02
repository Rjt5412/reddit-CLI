# Installation Steps

- Install(if not already installed) following:
  - python 3.10 or above
  - git
  - [Poetry](https://python-poetry.org/docs/#installation)

- Clone the repository: `git clone https://github.com/Rjt5412/reddit-cli.git`
- Navigate to the cloned directory: `cd reddit-cli`
- Install dependencies `poetry install .`
- Create the credentials file `reddit_config.json.json` under `$HOME`. It should follow the following fields in it:

```JSON
{
    "client_id": "<your_client_id>", 
    "client_secret": "<your_client_secret>"
}
```

- You can get your `client_id` and `client_secret` by creating an app [here](https://www.reddit.com/prefs/apps). Make sure to create the app with the name as `reddit-cli`

- Install the CLI using `python -m reddit_cli --install-completion`

- This should add CLI to your shell. Now you can access the CLI by simply running `reddit-cli --help`.
