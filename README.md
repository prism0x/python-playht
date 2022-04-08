# python-playht

This is a Python module for easy access to [play.ht's AI voice generation API](https://github.com/playht/text-to-speech-api).

## Install

```sh
python setup.py install
```

## Configure

Play.ht is not a free service, so you need to buy a subscription and configure your environment variables with your user id and secret token.

Create a file called `.env` in the same directory where you call Manim with your authentication information:

```sh
PLAY_HT_USER_ID="..."
PLAY_HT_SECRET="..."
```

You can find these in play.ht's web interface.

This is a work in progress and does not cover the full API. Use at your own risk.