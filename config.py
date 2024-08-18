import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("29343670"))
API_HASH = getenv("28010be97096919fe9511f8ddf1bfc54")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6880909457:AAGIMSvHx7GZzwuf-gvVEhYgzIvpdn4Sy78")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://ericabraham016:ericabraham016@cluster0.wrdspg0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)
MUSIC_BOT_NAME = getenv("GOJO SATORU", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002232962113", None))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002232962113"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("6436690546"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Gunjan890/disha",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/musictestttt")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/musictestttt")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("BQG_v7YAoT-VpN4uG6JQcfxIR79Ry42M6G6GlFD-B7ZkRimJG4y6OpmI8cgTxQZBRbt9l3CjJJOwXdzBcPRyWA13V4YsPXjhdrOEhPSZDpIVBjnSSSC-ymou5Qyzs_nN_3P2njRF0A2_m4c1dlKs59sNMtm-jPEe9Dd370te1yiDoKHN2vAcYizTVNwtdFLQLME_k6_UVQYxIb3E5XHN3Ncz1snvxf-b48MFKsOoN6D3X3T2Z2gVl0i4wf3IeQCgpsvqQKkn2tQ8cvIrfzM9DxWxa7yR7i8djXFamMn8IKHjN6fv1EaWA5_uI3nZ4uU9VcAMH9HKxsvn9Zm0Gf4lHAEyTsIZCAAAAAFJtncVAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/94918b340445db8a72c02.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/94918b340445db8a72c02.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/b869ffe0f2b6d233e21c1.jpg"
STATS_IMG_URL = "https://telegra.ph/file/f58134b916951c71f5bdc.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/0fbd2c68884973f262e12.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/0fbd2c68884973f262e12.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/a580337fd47ffe84c85b2.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/a580337fd47ffe84c85b2.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/693f06799e2138a4694d0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/693f06799e2138a4694d0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/b869ffe0f2b6d233e21c1.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/b869ffe0f2b6d233e21c1.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
        
