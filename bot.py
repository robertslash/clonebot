#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import sys
from user import User
from pyrogram import Client
from presets import Presets as Msg
from pyrogram.enums import ParseMode

from config import Config
from config import LOGGER


class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="bot_session",
            api_hash=Config.104317bd259d9f2ebcc982a151e2b8b8,
            api_id=Config.26018914,
            bot_token=Config.7368009009:AAHzIPwXkcxtWmBpnssBIExpkz5_VbB-TuE,
            sleep_threshold=30,
            workers=8,
            plugins={
                "root": "plugins"
            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()
        try:
            await self.USER.send_message(usr_bot_me.username, "%session_start%")
        except Exception:
            print(Msg.BOT_BLOCKED_MSG)
            sys.exit()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
