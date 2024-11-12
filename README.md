# ⚒️ ICRS Lab ⚒️

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)
![Espressif](https://img.shields.io/badge/espressif-E7352C.svg?style=for-the-badge&logo=espressif&logoColor=white)


[//]: <> ( TODO: add DDWRT, NFC cards,  )

## 👋 Introduction

This is the main code base for the Lab infrastructure which keeps ICRS running. ICRS is the [Imperial College Robotics Society](https://linktr.ee/icrobotics), helping about 500 members to make cool robotics projects!

### ⭐ Features

- Live-streaming Bambu Lab printer statuses to Discord, and live-streaming
- Only allowing printing once a card has been scanned
- A hand-held card scanner to see if members are inducted
- A Discord Quiz platform for inductions
- [Published at ISAM 2024](https://www.researchgate.net/publication/385302645_Automated_Student_3D_Printing_Verification_Process)

[//]: <> ( TODO: add Images )

### 🧩 Components

- **🤖 Lab Manager Discord Bot**: Uses Discord as a UI for members and staff
- **🗃️ ICRS LAB Back end**: Handles Communication between Discord, the Database, notion and APIs
- **⛃ ICRS Database**: Database for everything
- **💳 ICRS Card Scanner**: Can scan HF Cards and display a member's status

[//]: <> ( TODO: add system diagram )


## 🚒 Set up

### 1. Clone the repository

`git clone git@github.com:ICRS/icrs_lab.git`

#### Clone submodules

For the first time: `git submodule update --recursive --remote`

Every update after that: `git submodule update --recursive`

Run `python project_setup.py` and follow the instructions.


### 2. Recommended VScode extensions

- Postgres
- Python
- Autopep8
- Pylance
- Docker

### 3. Set up Discord Bot

[https://discord.com/developers/applications/](https://letmegooglethat.com/?q=how+to+set+up+a+discord+bot)

Add Bot to the ICRS test server (or your own) with `administrator` permissions, and `bot` &`application` scopes, and all the intents

Then get Discord token (eg `xxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.x-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

### 4. Prerequisites

Install the following

- Docker
- Docker-compose
- Python 3.10+
- Postman (non-essential but recommended)

## ⚙️ Config

### Create ENV files

copy paste the following files and remove the "template" part of teh file name:

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

Then go to Discord and use the bot (make sure to reboot Discord on the first launch or after adding new commands)

Wait about 20 seconds between changes and testing for the bot to rebuild

`http://localhost:8000/docs` for the FastAPI docs


### DB

use the VS code extensions to connect to the DB
with the settings in `example_postgress.ini` and the IP `172.18.0.2:8000/`


## 🚀 Deployment

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


## 📝 Paper

https://www.researchgate.net/publication/385302645_Automated_Student_3D_Printing_Verification_Process
