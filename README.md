# ⚒️ ICRS Lab ⚒️


## 🚒 Set up

### 1. Clone the repository

`git clone git@github.com:ICRS/icrs_lab.git`

#### Clone submodules

For the first time: `git submodule update --recursive --remote`

Every update after that: `git submodule update --recursive`


### 2. Recommended VScode extensions

- Postgres
- Python
- Autopep8
- Pylance
- Docker

### 3. Set up discord Bot

[https://discord.com/developers/applications/](https://letmegooglethat.com/?q=how+to+set+up+a+discord+bot)

Add Bot to the ICRS test server (or your own) with `administrator` permissions, and `bot` &`application` scopes, and all the intents

Then get Discord token (eg `xxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.x-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

### 4. Prerequisites

Install the following

- Docker
- Docker-compose
- Python 3.10+
- Postman (non essential but recommended)

## ⚙️ Config

### Create ENV files

copy paste the follow files and remove the "template" part of teh file name:

- `.env_template` -> `.env`
- `discord_settings_template.json` -> `discord_settings.json`
- `printer_settings_template.json` -> `printer_settings.json`

### .env

Enter your discord token into a `.env` replacing `<YOUR_DISCORD_TOKEN>`


### discord_settings

Replace `YOUR_DISCORD_SERVER_ID` with the server ID

Replace `YOUR_ADMIN_ID` with your Discord user ID


## 🏃 Build and Run

`docker compose up --build --watch`

This should take about 1 minute for the first build and about 30 seconds for subsequent builds

`ctrl + c` to stop the server

Then go to discord and use the bot (make sure to reboot Discord on the first launch or after adding new commands)

Wait about 20 seconds between changes and testing for the bot to rebuild

`http://localhost:8000/docs` for the FastAPI docs


### DB

use the VS code extensions to connect to the DB
with the settings in `example_postgress.ini` and the IP `172.18.0.2:8000/`


## 💿 Deployment

TODO: Do this section properly

Set up SSH
ssh into server

```bash
cd code;
cd <REPO>;
git pull;
docker-compose up --build -d
```

Delete Pod on Kubernetes
