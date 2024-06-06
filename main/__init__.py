#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = #config("API_ID", default=23124867, cast=int)
API_HASH = #config("API_HASH", default=22cbd5a100dcd9892c89e8adee481541)
BOT_TOKEN = #config("BOT_TOKEN", default=7255509548:AAFDvUvE0vCTsnYgWms_UKT127gigUjyS2A)
SESSION = #config("SESSION", default=BQFg24MAtXjjtl43VEUrVhjPN7GjVc50s3e_wsPQ7Ha_3lDiRsHGp--Brn3Fz4F37t42deLaNyJuCULfOABmuVIX8zECcEMBBlvEeywF5qcfmVvLimk6BtYZNNlbDaaGJrsq7Q2lY7mzYw0yp8BFS2tH4L1CuIjkryAm0vc19Fj5VuTCCo-5AYHx1Z73B5F80fNgmZuhEjdDTlU_uukkZ8xqzggAAQGUAdky7e_BeJQlVcRtA5kH9lKk_AhjWs4-9jJd0STOslh3rqyqYt9NNzWwGQZuY8uIGs2fI-IDfZ_4r1Hi7KaPkCvm4xssWtLlLghiFtsHqLgIWTE812OH63QHsm6WkQAAAAEuTYqwAA)
FORCESUB = #config("FORCESUB", default=manu85O)
AUTH = #config("AUTH", default=5071801008)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
