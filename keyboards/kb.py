from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# функция создания клавиатуры с регионами
def create_state_keyboard() -> InlineKeyboardMarkup:

    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()

    # Создаем объекты инлайн-кнопок
    button_state_1 = InlineKeyboardButton(
        text='Астраханская область',
        callback_data='^astrakhan^')

    button_state_2 = InlineKeyboardButton(
        text='Белгородская область',
        callback_data='^belgorod^')

    button_state_3 = InlineKeyboardButton(
        text='Волгоградская область',
        callback_data='^volgograd^')

    button_state_4 = InlineKeyboardButton(
        text='Воронежская область',
        callback_data='^voronezh^')

    button_state_5 = InlineKeyboardButton(
        text='Ивановская область',
        callback_data='^ivanovo^')

    button_state_6 = InlineKeyboardButton(
        text='Калужская область',
        callback_data='^kaluga^')

    button_state_7 = InlineKeyboardButton(
        text='Карелия Республика',
        callback_data='^karelia^')

    button_state_8 = InlineKeyboardButton(
        text='Краснодарский край',
        callback_data='^krasnodar^')

    button_state_9 = InlineKeyboardButton(
        text='Курская область',
        callback_data='^kursk^')

    button_state_10 = InlineKeyboardButton(
        text='Ленинградская область',
        callback_data='^leningrad^')

    button_state_11 = InlineKeyboardButton(
        text='Московская область',
        callback_data='^moscow^')

    button_state_12 = InlineKeyboardButton(
        text='Омская область',
        callback_data='^omsk^')

    button_state_13 = InlineKeyboardButton(
        text='Ставропольский край',
        callback_data='^stavropol^')

    button_state_14 = InlineKeyboardButton(
        text='Тверская область',
        callback_data='^tver^')

    buttons: list[InlineKeyboardButton] =  [button_state_1, button_state_2, button_state_3,
                                            button_state_4, button_state_5, button_state_6,
                                            button_state_7, button_state_8, button_state_9,
                                            button_state_10, button_state_11, button_state_12,
                                            button_state_13, button_state_14]

    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()


# Функция для генерации инлайн-клавиатуры "Продолжить"
def create_continue_keyboard():
    button_continue = InlineKeyboardButton(
        text='Продолжить',
        callback_data='forecast')
    keyboard_continue = InlineKeyboardMarkup(inline_keyboard=[
                                                 [button_continue]])
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

