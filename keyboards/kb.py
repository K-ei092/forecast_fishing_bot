from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


# функция создания кнопки "поделиться местоположением"
def create_geo_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Поделиться местоположением", request_location=True)
    )
    keyboard = builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    return keyboard


# функция построения клавиатуры с регионами
def create_state_keyboard() -> InlineKeyboardMarkup:

    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()

    # Создаем объекты инлайн-кнопок
    button_state_1 = InlineKeyboardButton(
        text='Астраханская область',
        callback_data='^astrakhan^')

    button_state_2 = InlineKeyboardButton(
        text='Башкортостан Республика',
        callback_data='^bashkortostan^')

    button_state_3 = InlineKeyboardButton(
        text='Белгородская область',
        callback_data='^belgorod^')

    button_state_4 = InlineKeyboardButton(
        text='Владимирская область',
        callback_data='^vladimir^')

    button_state_5 = InlineKeyboardButton(
        text='Волгоградская область',
        callback_data='^volgograd^')

    button_state_6 = InlineKeyboardButton(
        text='Воронежская область',
        callback_data='^voronezh^')

    button_state_7 = InlineKeyboardButton(
        text='Ивановская область',
        callback_data='^ivanovo^')

    button_state_8 = InlineKeyboardButton(
        text='Иркутская область',
        callback_data='^irkutsk^')

    button_state_9 = InlineKeyboardButton(
        text='Калужская область',
        callback_data='^kaluga^')

    button_state_10 = InlineKeyboardButton(
        text='Карелия Республика',
        callback_data='^karelia^')

    button_state_11 = InlineKeyboardButton(
        text='Краснодарский край',
        callback_data='^krasnodar^')

    button_state_12 = InlineKeyboardButton(
        text='Курская область',
        callback_data='^kursk^')

    button_state_13 = InlineKeyboardButton(
        text='Красноярский край',
        callback_data='^krasnoyarsk^')

    button_state_14 = InlineKeyboardButton(
        text='Курганская область',
        callback_data='^kurgan^')

    button_state_15 = InlineKeyboardButton(
        text='Ленинградская область',
        callback_data='^leningrad^')

    button_state_16 = InlineKeyboardButton(
        text='Липецкая область',
        callback_data='^lipetsk^')

    button_state_17 = InlineKeyboardButton(
        text='Московская область',
        callback_data='^moscow^')

    button_state_18 = InlineKeyboardButton(
        text='Омская область',
        callback_data='^omsk^')

    button_state_19 = InlineKeyboardButton(
        text='Ростовская область',
        callback_data='^rostov-na-donu^')

    button_state_20 = InlineKeyboardButton(
        text='Ставропольский край',
        callback_data='^stavropol^')

    button_state_21 = InlineKeyboardButton(
        text='Тверская область',
        callback_data='^tver^')

    buttons: list[InlineKeyboardButton] =  [button_state_1, button_state_2, button_state_3,
                                            button_state_4, button_state_5, button_state_6,
                                            button_state_7, button_state_8, button_state_9,
                                            button_state_10, button_state_11, button_state_12,
                                            button_state_13, button_state_14, button_state_15,
                                            button_state_16, button_state_17, button_state_18,
                                            button_state_19, button_state_20, button_state_21]

    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()


# Функция для генерации инлайн-клавиатуры "Продолжить"
def create_forecast_keyboard():
    button_forecast_fishing = InlineKeyboardButton(
        text='Прогноз клёва 🎣',
        callback_data='fishing')
    button_forecast_weather = InlineKeyboardButton(
        text='Прогноз погоды ⛈',
        callback_data='weather')
    keyboard_continue = InlineKeyboardMarkup(inline_keyboard=[
        [button_forecast_fishing],
        [button_forecast_weather]
    ])
    return keyboard_continue


# Функция для генерации инлайн-клавиатур "на лету"
def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Добавляем в билдер последнюю кнопку, если она передана в функцию
    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='$vse$'
        ))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()

