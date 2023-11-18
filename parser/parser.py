import random

import requests
from bs4 import BeautifulSoup
from database.database import users_db
from lexicon.lexicon import LEXICON_FORCE as LF
from lexicon.lexicon import BUTTONS

_tuple_user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit"
    "/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",

    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 "
    "Firefox/84.0",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like "
    "Gecko) Chrome/87.0.4280.141 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.66 (Edition Yx)",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/87.0.4280.141 Safari/537.36 Brave/1.18.77 Chrome/87.0.4280.141",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edge/88.0.705.50",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/87.0.4280.141 YaBrowser/20.12.2.107 Yowser/2.5 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/119.0.0.0 Safari/537.36"
)

def _get_dict_forecast(soup):

    dict_fish = {
        'Белый амур': [],
        'Быстрянка': [],
        'Бычок-подкаменщик': [],
        'Вырезуб (кутум)': [],
        'Вьюн': [],
        'Голавль': [],
        'Гольян': [],
        'Горчак': [],
        'Густера': [],
        'Елец': [],
        'Жерех': [],
        'Карась': [],
        'Карп': [],
        'Краснопёрка': [],
        'Лещ': [],
        'Линь': [],
        'Микижа (радужная форель)': [],
        'Налим': [],
        'Овсянка, верховка': [],
        'Озёрная форель': [],
        'Окунь': [],
        'Пескарь': [],
        'Плотва': [],
        'Подуст': [],
        'Ротан': [],
        'Ручьевая форель': [],
        'Синец': [],
        'Сом': [],
        'Сопа (белоглазка)': [],
        'Стерлядь': [],
        'Судак': [],
        'Уклейка': [],
        'Чехонь': [],
        'Щука': [],
        'Язь': [],
        'Ёрш': []
    }

    tag_section = soup.find('section', {"class": "grid table__fishing"})
    tag_today = tag_section.find_all('div',
                                     {'class': 'grid__oneday grid__oneday'
                                               '--current grid__col_0 grid'
                                               '__subcol'})
    tag_second = tag_section.find_all('div', {'class': 'grid__oneday grid__'
                                                       'col_1 grid__subcol'})
    tag_third = tag_section.find_all('div', {'class': 'grid__oneday grid__'
                                                      'col_2 grid__subcol'})

    li_today = [[x for x in tag.text.split() if x.isdigit()] for tag in tag_today]
    li_second = [[x for x in tag.text.split() if x.isdigit()] for tag in tag_second]
    li_third = [[x for x in tag.text.split() if x.isdigit()] for tag in tag_third]

    for key in dict_fish:
        if len(li_today) > 0:
            dict_fish[key].append(li_today.pop(0))
        if len(li_second) > 0:
            dict_fish[key].append(li_second.pop(0))
        if len(li_third) > 0:
            dict_fish[key].append(li_third.pop(0))

    return dict_fish

def _get_html(user_id):

    place = users_db[user_id][0]
    url = F'https://rybalku.ru/prognoz/ru/{place}'
    headers = {'User-Agent': f'{random.choice(_tuple_user_agent)}',
               'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
               'Accept': 'text/html,application/xhtml+xml',
    }

    try:
        session = requests.Session()
        response = session.get(url=url, headers=headers, timeout=3)
        if response.ok:
            return response.text

    except Exception as ex:
        print(ex)

# функция определения уровня клёва (дружественно к пользователю)
def _get_force(data):

    for key, value in LF.items():
        if int(data) in key:
            return value


# функция дл создания конечного результата
def get_result(id):
    html = _get_html(id)
    soup = BeautifulSoup(html, 'html.parser')
    forecast = _get_dict_forecast(soup=soup)

    if users_db[id][1] != 'vse':
        if forecast[users_db[id][1]]:
            fish = str(users_db[id][1])
            tn = forecast[users_db[id][1]][0][0]
            tm = forecast[users_db[id][1]][0][1]
            td = forecast[users_db[id][1]][0][2]
            te = forecast[users_db[id][1]][0][3]
            sn = forecast[users_db[id][1]][1][0]
            sm = forecast[users_db[id][1]][1][1]
            sd = forecast[users_db[id][1]][1][2]
            se = forecast[users_db[id][1]][1][3]
            thn = forecast[users_db[id][1]][2][0]
            thm = forecast[users_db[id][1]][2][1]
            thd = forecast[users_db[id][1]][2][2]
            the = forecast[users_db[id][1]][2][3]

            return f'<b>{fish}</b>\n' \
                   f'\n' \
                   f'<u>Сегодня</u>:\n' \
                   f'ночь - {_get_force(tn)} ({tn})\n' \
                   f'утро - {_get_force(tm)} ({tm})\n' \
                   f'обед - {_get_force(td)} ({td})\n' \
                   f'вечер - {_get_force(te)} ({te})\n\n' \
                   f'<u>Завтра</u>:\n' \
                   f'ночь - {_get_force(sn)} ({sn})\n' \
                   f'утро - {_get_force(sm)} ({sm})\n' \
                   f'обед - {_get_force(sd)} ({sd})\n' \
                   f'вечер - {_get_force(se)} ({se})\n\n' \
                   f'<u>Послезавтра</u>:\n' \
                   f'ночь - {_get_force(thn)} ({thn})\n' \
                   f'утро - {_get_force(thm)} ({thm})\n' \
                   f'обед - {_get_force(thd)} ({thd})\n' \
                   f'вечер - {_get_force(the)} ({the})\n' \
                   f'\n' \
                   f'прогноз клева на @prognoz_rubalku_bot'

        else:
            return 'К сожалению, информация о данной рыбе отсутствует.'

    else:
        with open('result.txt', 'w', encoding='utf-8') as file:
            for key, value in forecast.items():
                if ('$' + str(key) + '$' in BUTTONS) and forecast[key]:
                    fish = str(key)
                    tn = forecast[key][0][0]
                    tm = forecast[key][0][1]
                    td = forecast[key][0][2]
                    te = forecast[key][0][3]
                    sn = forecast[key][1][0]
                    sm = forecast[key][1][1]
                    sd = forecast[key][1][2]
                    se = forecast[key][1][3]
                    thn = forecast[key][2][0]
                    thm = forecast[key][2][1]
                    thd = forecast[key][2][2]
                    the = forecast[key][2][3]
                    res = f'{fish}.\n Сегодня: ночь - {_get_force(tn)} ({tn}) / утро - {_get_force(tm)} ({tm}) ' \
                          f'/ обед - {_get_force(td)} ({td}) / вечер - {_get_force(te)} ({te})\n' \
                          f'Завтра: ночь - {_get_force(sn)} ({sn}) / утро - {_get_force(sm)} ({sm})' \
                          f'/ обед - {_get_force(sd)} ({sd}) / вечер - {_get_force(se)} ({se})\n' \
                          f'Послезавтра: ночь - {_get_force(thn)} ({thn}) / утро - {_get_force(thm)} ({thm})' \
                          f'/ обед - {_get_force(thd)} ({thd}) /вечер - {_get_force(the)} ({the})\n\n'

                    file.write(res)

        text_file = 'result.txt'
        return text_file
