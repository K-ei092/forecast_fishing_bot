import os

from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message, FSInputFile, ContentType

from keyboards.kb import create_state_keyboard, create_inline_kb, create_forecast_keyboard, create_geo_keyboard
from lexicon.lexicon import LEXICON, LEXICON_STATE, BUTTONS
from database.database import users_db
from config_data.config import Config, load_config
from parser.parser_fish import get_result
from parser.parser_weather import get_weather


router = Router()

# Загружаем конфиг
config: Config = load_config()
CHAT_ID=config.tg_bot.chat_id

# Этот хэндлер будет срабатывать на команду "/start" -
# проверяет есть подписан ли пользователь на канал
# и предлагает продолжить либо подписаться на канал
@router.message(CommandStart())
async def process_start_command(message: Message):
    # user_channel_status = await bot.get_chat_member(chat_id=CHAT_ID[0], user_id=message.from_user.id)
    # if user_channel_status.status != 'left':
    keyboard_forecast = create_forecast_keyboard()
    await message.answer(
        text=LEXICON[message.text],
        reply_markup = keyboard_forecast)
    # else:
    #     await message.answer(
    #         text=LEXICON['channel_left'])


# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


# Этот хэндлер будет срабатывать на инлайн-кнопку "Продолжить"
# и отправлять пользователю инлайн-клавиатуру с доступными к выбору регионами
@router.callback_query(F.data == 'fishing')
async def process_forecast_command(callback: CallbackQuery):
    keyboard_state = create_state_keyboard()
    await callback.message.edit_text(
        text='Виберете необходимую область \(край\)',
        reply_markup=keyboard_state)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки с выбранным регионом
# и предлагать выбрать вид рыбы из списка путем нажатия инлайн-кнопки
@router.callback_query(F.data.startswith('^') and F.data.endswith('^'))
async def process_fish_press(callback: CallbackQuery):
    users_db[callback.from_user.id] = [LEXICON_STATE[callback.data]]
    keyboard_fish = create_inline_kb(6, last_btn='25', **BUTTONS)
    text = LEXICON['fish']
    await callback.message.edit_text(
        text=text,
        reply_markup=keyboard_fish)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки с выбранной
# и отправлять ответ по виду рыбы (в сообщении) либо всем видам (в файле)
@router.callback_query(F.data.startswith('$') and F.data.endswith('$'))
async def process_fish_press(callback: CallbackQuery):
    users_db[callback.from_user.id].append(callback.data[1:-1])
    text = LEXICON['wait']
    await callback.message.edit_text(
        text=text)
    result = get_result(callback.from_user.id)
    if result != 'result.txt':
        await callback.message.edit_text(
            text=result)
    else:
        file = FSInputFile(result)
        await callback.message.edit_text(
            text="Ваш прогноз")
        await callback.message.answer_document(file)
        os.remove(result)

@router.callback_query(F.data == 'weather')
async def process_location_command(callback: CallbackQuery):
    keyboard_geo = create_geo_keyboard()

    await callback.message.edit_text(
        text='Поделитесь вашим местоположением')

    await callback.message.answer(
        text='⬇ кнопка снизу ⬇',
        reply_markup = keyboard_geo)


@router.message(F.content_type == ContentType.LOCATION)
async def process_handle_location(message: Message):
    latitude = round(message.location.latitude, 2)
    longitude = round(message.location.longitude, 2)
    result = get_weather(latitude, longitude)
    await message.answer(
        text=f'Ваш прогноз\n{result}'
    )


