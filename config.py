import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "X MUSIC PLAYER")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/3296f014fb0de1368a09e.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/3296f014fb0de1368a09e.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/3296f014fb0de1368a09e.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/3296f014fb0de1368a09e.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "X_MUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "X_MUSIC_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "x_fighter_op")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "STATUS_LOVER_OP")
OWNER_NAME = getenv("OWNER_NAME", "MR_X_OP_BOLTE") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "MR_X_OP_BOLTE")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "80"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
