# EpicGamesBot

## This set of code has:

- Telegram bot

- Parser of free games from the Epic Games website

- Interaction with the database

**Technology stack**
>Python 3.10.5, PostgreSQL, Redis, docker-compose

**Python main modules**
>aiogram, selenium/webdriver, BeautifulSoup(bs4), redis, psycopg2

## How to Install and Run
First of need to git clone
```
$ git clone https://github.com/Suslicke/EpicGamesBot.git
```
Create venv
```
$ python3 -m venv venv
```
download requirements,
in venv
```
(venv) $ pip install -r requirements.txt
```

Create .env file

```
export SQLALCHEMY_URL=postgresql://USER:postgres@127.0.0.1:5434/DB_NAME
export POSTGRES_USER=USER
export POSTGRES_PASSWORD=postgres
export POSTGRES_DB=DB_NAME
export REDIS_HOST=redis
export REDIS_PORT=6379
export API_TOKEN=API_TOKEN
```

Change settings for docker in **docker-compose.yml**:
```
POSTGRES_USER=USER
POSTGRES_PASSWORD=postgres
POSTGRES_DB=DB_NAME
REDIS_HOST=redis
REDIS_PORT=6379
```
Run command
```
$ docker-compose up -d
```

Run 2 commands
```
python src/parser/main.py
```

```
python src/bot/bot.py
```

### All ready