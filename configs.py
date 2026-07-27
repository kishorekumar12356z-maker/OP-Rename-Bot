# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "24681559"))
    API_HASH = os.environ.get("API_HASH", "d967929e0100f3c119bb356e43d6fa77")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8653566072:AAG-MvuHXxw17MEQj_lP7HufkCKyzVvPayI")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("8030254824", ))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "
mongodb+srv://vegitobule77_db_user:gokuda@cluster0.hgifx7y.mongodb.net/?appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003985227353")
    "))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
