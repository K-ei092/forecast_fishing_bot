from aiogram import Router
from aiogram.types import Message

router = Router()

# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(
        text=f'Мне неизвестна команда "{message.text}"\n'
             'Попробуй набрать /start или /forecast'
    )