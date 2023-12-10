LEXICON: dict[str, str] = {
    '/start': 'Нажми нужную кнопку 🟢',
    '/help': 'Доступная команда:\n/start \- формирование нового запроса\n\n'
             'Градация клёва по возрастанию:\n'
             'клюёт только у соседа ❌\n'
             'веришь в удачу ⁉\n'
             'клёв хуже среднего 😐\n'
             'средний клёв 🤏\n'
             'хороший клёв 👍\n'
             'отличный клёв ✅\n\n'
             'Откуда берутся прогнозы?\n'
             'Мы их получаем из различных популярных сервисов, обобщаем\n'
             'и стараемся в максимально удобном формате предоставить Вам 🙂\n\n'
             'Применяйте полученную информацию в совокупности со своим '
             'рыбацким опытом\n\n'             
             'Сервис доступен для подписчиков канала [РЫБАЧОК](https://t.me/ryba_choc)\n\n'
             'Сведения об ошибках и отзывы просим оставлять в комментариях '
             'к последнему посту канала',
    'channel_left': 'Это бот с прогнозом клева и погоды\n\n'
                    'Сервис доступен для подписчиков канала '
                    '[РЫБАЧОК](https://t.me/ryba_choc)\n\n'
                    'После подписки вернитесь в бот и наберите /start\n\n'
                    '_Мы не сохраняем ваши личные данные и местоположение\n'
                    'И мы не распространяем рекламу в личных сообщениях_',
    'fish': 'Выберете позицию по которой необходим прогноз или нажмите '
            'последнюю кнопку "весь список" для получения обобщенных сведений ' 
            'в одном файле:\n'
            '```\n'
            '1.Белый амур   | 2.Быстрянка\n'
            '3.Голавль      | 4.Густера\n'
            '5.Елец         | 6.Жерех\n'
            '7.Карась       | 8.Карп\n'
            '9.Краснопёрка  | 10.Лещ\n'
            '11. Налим      | 12.Озёрная форель\n'
            '13.Окунь       | 14.Плотва\n'
            '15.Подуст      | 16.Синец\n'
            '17.Сом         | 18.Сопа (белоглазка) \n'
            '19.Стерлядь    | 20.Судак\n'
            '21.Чехонь      | 22.Щука\n'
            '23.Ёрш         | 24.Язь\n\n'
            '    25.Весь список \(одним файлом\)'
            '```',
    'wait': 'Ожидайте, результат формируется'
}

LEXICON_COMMANDS = {
    '/start': 'Начать',
    '/help': 'Помощь'
}


LEXICON_FORCE = {
    tuple(range(0, 21)): 'клюёт только у соседа ❌',
    tuple(range(21, 36)): 'веришь в удачу ⁉',
    tuple(range(36, 51)): 'клёв хуже среднего 😐',
    tuple(range(51, 71)): 'средний клёв 🤏',
    tuple(range(71, 91)): 'хороший клёв 👍',
    tuple(range(91, 101)): 'отличный клёв ✅',
}


BUTTONS: dict[str, str] = {
    '$Белый амур$': '1',
    '$Быстрянка$': '2',
    '$Голавль$': '3',
    '$Густера$': '4',
    '$Елец$': '5',
    '$Жерех$': '6',
    '$Карась$': '7',
    '$Карп$': '8',
    '$Краснопёрка$': '9',
    '$Лещ$': '10',
    '$Налим$': '11',
    '$Озёрная форель$': '12',
    '$Окунь$': '13',
    '$Плотва$': '14',
    '$Подуст$': '15',
    '$Синец$': '16',
    '$Сом$': '17',
    '$Сопа (белоглазка)$': '18',
    '$Стерлядь$': '19',
    '$Судак$': '20',
    '$Чехонь$': '21',
    '$Щука$': '22',
    '$Ёрш$': '23',
    '$Язь$': '24'
}

LEXICON_STATE: dict[str, str] = {
    '^astrakhan^': 'astrakhan%20oblast/astrakhan/astrakhan',
    '^bashkortostan^': 'bashkortostan/city%20district%20ufa/ufa',
    '^belgorod^': 'belgorod%20oblast/the%20urban%20district%20of%20belgorod/belgorod',
    '^vladimir^': 'vladimir%20oblast/city%20district%20vladimir/vladimir',
    '^volgograd^': 'volgograd%20oblast/volgograd/volgograd',
    '^voronezh^': 'voronezh%20oblast/voronezh/voronezh',
    '^ivanovo^': 'ivanovo%20oblast/ivanovo/ivanovo',
    '^irkutsk^': 'irkutsk%20oblast/municipal%20okrug%20of%20irkutsk/irkutsk',
    '^kaluga^': 'kaluga%20oblast/city%20district%20of%20kaluga/kaluga',
    '^krasnodar^': 'krasnodar%20krai/krasnodar%20municipality/krasnodar',
    '^kursk^': 'kursk%20oblast/kursk/kursk',
    '^krasnoyarsk^': 'krasnoyarsk%20krai/krasnoyarsk%20urban%20okrug/krasnoyarsk',
    '^kurgan^': 'kurgan%20oblast/kurgan/kurgan',
    '^leningrad^': 'leningrad%20oblast/olhava%20district/volkhov',
    '^lipetsk^': 'lipetsk%20oblast/lipetsk/lipetsk',
    '^moscow^': 'moscow%20oblast/lyuberetsky%20district/lyubertsy',
    '^omsk^': 'omsk%20oblast/the%20county%20town%20of%20omsk/omsk',
    '^rostov-na-donu^': 'rostov%20oblast/rostov-on-don/rostov-na-donu',
    '^karelia^': 'republic%20of%20karelia/medvezhyegorsky%20district/medvezhyegorsk',
    '^stavropol^': 'stavropol%20krai/stavropol/stavropol',
    '^tver^': 'tver%20oblast/tver/tver',
}