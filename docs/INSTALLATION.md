# Installation Steps

- Create the credentials file `reddit_config.json.json` under `$HOME`. It should follow the following fields in it:

```JSON
{
    "client_id": "<your_client_id>", 
    "client_secret": "<your_client_secret>"
}
```

- You can get your `client_id` and `client_secret` by creating an app [here](https://www.reddit.com/prefs/apps). Make sure to create the app with the name as `reddit-cli`

- Install(if not already installed) following:
  - python 3.10 or above

- Download the release wheel(.whl) to be installed as python package from [here](https://github.com/Rjt5412/reddit-cli/releases/tag/0.1.0)

- Then just run `pip install --user <PATH_TO_DOWNLOADED_WHEEL_FILE>`

- This should add CLI to your shell. Now you can access the CLI by simply running `reddit-cli --help`.
