# Polyfun
Discord bot with language games

## Commands

`/guess_lang` - Starts a guessing game where a sentence is translated into a random language and users have 60 seconds to guess which language it is.

`/detect_lang` - Detects the language of a given sentence and returns its name (disabled while a guessing game is active in the channel)

`/health_check` - Checks if bot is running

## How to run

### Docker

- Clone repo
- Build image
- Run it with `DISCORD_TOKEN` env variable

### w8 docker

- Clone repo
- Install dependencies from `requirements.txt`
- Put your `DISCORD_TOKEN` in .env
- Run `app.py`