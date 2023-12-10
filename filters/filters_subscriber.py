from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message
from config_data.config import Config, load_config

config: Config = load_config()
CHAT_ID = config.tg_bot.chat_id

class IsSubscriber(BaseFilter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        for chat_id in CHAT_ID:
            sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
            if sub.status != 'left':
                return True
            else:
                return False

