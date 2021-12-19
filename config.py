
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = "2146361275:AAF3mgx16FEFiw8ug6IHyXoCZlsrMKyu-e0"

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = "9956617"

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = "8f6e046c7e7f35808ae11e77f1ecc890"

# Generate a user session string 
TG_USER_SESSION = "AQBZidX6xpS7DlheXbgjAgjnTfDl9jWSdOtTp-F0DZKdD-FEs0lkCwcNhvb3S5VvwaoV47yqoq5JGux4SwYcb577h3PrPK4Wjwrgktq9l4dtBKWCF8_25SOtHpCz2RicN6KV3B_66ZcvuL_IH6TEfBmXDWNb_IZfsAa1OYCSh_s8A8OQiMjnBhX6UwPiwfeZRMweeAul-rdspd-uvXSTxAarwSB3kTXdPbFkBejvNwqWC6iYT2V9EdyX51S9bVxm5HGGVk6LCTkNNj1fMNb5es7pYOaxFBcsLWbzZ1xC-V7UCixFPRRifaDVbLHOFo-GXZrJg_9nvPrY53xB5aVHT70oe6AmBgA"

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = "mongodb+srv://erichdaniken:erichdaniken@cluster0.7enua.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Your database name from mongoDB
DATABASE_NAME = "Cluster0"

# ID of users that can use the bot commands
AUTH_USERS = "2074093062"

# Should bot search for document files in channels
DOC_SEARCH = "yes"

# Should bot search for video files in channels
VID_SEARCH = "yes"

# Should bot search for music files in channels
MUSIC_SEARCH = "no"




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
