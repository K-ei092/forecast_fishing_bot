import requests, json
from config_data.config import Config, load_config

# Загружаем конфиг
config: Config = load_config()
API_key=config.tg_bot.apy_key

# Словарь с направлением ветра
code_to_wind = {
        tuple(range(0, 23)): 'C ⬇ ',
        tuple(range(23, 68)): 'СВ ↙️',
        tuple(range(68, 113)): 'В ⬅',
        tuple(range(113, 158)): 'ЮВ ↖️',
        tuple(range(158, 203)): 'Ю ⬆',
        tuple(range(203, 248)): 'ЮЗ ↗️',
        tuple(range(248, 293)): 'З ➡',
        tuple(range(293, 338)): 'СЗ ↘️',
        tuple(range(338, 360)): 'С ⬇',
    }

# Словарь с временем суток
code_times_of_day = {
    '00': 'ночь \(04:00\)',
    '03': 'утро \(07:00\)',
    '09': 'день \(13:00\)',
    '15': 'вечер \(19:00\)'
}

# Функция определения направления ветра (дружественно к пользователю)
def _get_wind(data):

    for key, value in code_to_wind.items():
        if int(data) in key:
            return value

def get_weather(latitude, longitude):

    lat = latitude
    lon = longitude
    units = 'metric'
    lang = 'ru'

    li_forecast = []

    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&lang={lang}&appid={API_key}'

    response = requests.get(url=url)

    if response.status_code == 200:
        data = json.loads(response.text)
        if data['cod'] == '200':
            for i in range(24):
                if data['list'][i]['dt_txt'][-8:-6] in ['00', '03', '09', '15']:

                    dict_weather = {
                        'время дня': '',
                        't': '',
                        'АД': '',
                        'влажность': '',
                        'осадки': '',
                        'облачность': '',
                        'ветер': '',
                        'вероятность осадков': ''
                    }

                    dict_weather['время дня'] = code_times_of_day[data['list'][i]['dt_txt'][-8:-6]]
                    dict_weather['t'] = ('\\' if data['list'][i]['main']['temp'] < 0 else '') + \
                                        str(int(data['list'][i]['main']['temp'] +
                                                (0.5 if data['list'][i]['main']['temp'] >
                                                         0 else -0.5))) + ' °C'
                    dict_weather['АД'] = str(int(data['list'][i]['main']['grnd_level'] * 0.7500637554192 +
                                                 (0.5 if data['list'][i]['main']['grnd_level'] >
                                                         0 else -0.5))) + ' мм рт\. ст\.'
                    dict_weather['влажность'] = str(data['list'][i]['main']['humidity']) + ' %'
                    dict_weather['осадки'] = data['list'][i]['weather'][0]['description']
                    dict_weather['облачность'] = str(data['list'][i]['clouds']['all']) + ' %'
                    dict_weather['ветер'] = str(int(data['list'][i]['wind']['speed'])) + ' м/с, ' + \
                                            str(_get_wind(data['list'][i]['wind']['deg']))
                    dict_weather['вероятность осадков'] = int(data['list'][i]['pop'] * 100)

                    li_forecast.append(dict_weather)
                    # print(dict_weather)
                    # print(data['list'][i])

    res = ''
    for i in range(4):

        res += f'{li_forecast[i]["время дня"]}:\n' \
              f'🌡 \= {li_forecast[i]["t"]}\n' \
              f'🎛 \= {li_forecast[i]["АД"]}\n' \
              f'влажность💧 \= {li_forecast[i]["влажность"]}\n' \
              f'осадки: {li_forecast[i]["осадки"]}\n' \
              f'облачность: {li_forecast[i]["облачность"]}\n' \
              f'ветер🪁: до {li_forecast[i]["ветер"]}\n' \
              f'вероятность осадков \= {li_forecast[i]["вероятность осадков"]} %\n\n' \


    return res

if __name__ == "__main__":
    print(get_weather(46.40, 48.09))
