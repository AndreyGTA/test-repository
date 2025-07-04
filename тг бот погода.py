import re
import telebot
import requests
from datetime import datetime
from telebot import types

BOT_TOKEN = '7798818033:AAEaBcDReUNQtfjJdQNfOqUEl2DFeSXkCKw'
OWM_API_KEY = '134995876b8440fb5056831016f81627'
LANG = 'ru'
UNITS = 'metric'

bot = telebot.TeleBot(BOT_TOKEN)


def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OWM_API_KEY}&units={UNITS}&lang={LANG}&cnt=40'
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != '200':
        return None

    daily_forecast = {}
    for item in data['list']:
        date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
        if date not in daily_forecast:
            daily_forecast[date] = {
                'temp_min': item['main']['temp_min'],
                'temp_max': item['main']['temp_max'],
                'conditions': [],
                'humidity': [],
                'wind_speed': []
            }

        if item['main']['temp_min'] < daily_forecast[date]['temp_min']:
            daily_forecast[date]['temp_min'] = item['main']['temp_min']
        if item['main']['temp_max'] > daily_forecast[date]['temp_max']:
            daily_forecast[date]['temp_max'] = item['main']['temp_max']

        daily_forecast[date]['conditions'].append(item['weather'][0]['description'])
        daily_forecast[date]['humidity'].append(item['main']['humidity'])
        daily_forecast[date]['wind_speed'].append(item['wind']['speed'])

    result = []
    for date, values in daily_forecast.items():
        main_condition = max(set(values['conditions']), key=values['conditions'].count)
        avg_humidity = round(sum(values['humidity']) / len(values['humidity']))
        avg_wind = round(sum(values['wind_speed']) / len(values['wind_speed']), 1)

        weekday = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
        weekday_ru = {
            'Monday': 'Понедельник',
            'Tuesday': 'Вторник',
            'Wednesday': 'Среда',
            'Thursday': 'Четверг',
            'Friday': 'Пятница',
            'Saturday': 'Суббота',
            'Sunday': 'Воскресенье'
        }.get(weekday, weekday)

        result.append({
            'date': f"{weekday_ru} ({date.split('-')[2]}.{date.split('-')[1]})",
            'temp_min': values['temp_min'],
            'temp_max': values['temp_max'],
            'condition': main_condition,
            'humidity': avg_humidity,
            'wind': avg_wind
        })

    return result[:7]


# Создаём меню с двумя кнопками: общая погода и погода в Новосибирске
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_weather = types.KeyboardButton('Погода')
    btn_nsk = types.KeyboardButton('Погода в Новосибирске')
    markup.add(btn_weather, btn_nsk)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Выберите действие:",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: message.text == 'Погода в Новосибирске')
def send_nsk_weather(message):
    city = "Novosibirsk"
    bot.send_chat_action(message.chat.id, 'typing')
    forecast = get_weather_forecast(city)

    if not forecast:
        bot.reply_to(message, "⚠️ Не удалось получить данные о погоде для Новосибирска.")
        return

    response = f"🌦️ Прогноз погоды в Новосибирске на 7 дней:\n\n"
    for day in forecast:
        response += (
            f"📅 <b>{day['date']}</b>\n"
            f"🌡️ Температура: от {day['temp_min']}°C до {day['temp_max']}°C\n"
            f"☁️ Погода: {day['condition'].capitalize()}\n"
            f"💧 Влажность: {day['humidity']}%\n"
            f"🌬️ Ветер: {day['wind']} м/с\n\n"
        )

    bot.send_message(message.chat.id, response, parse_mode='HTML', reply_markup=main_menu())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот погоды. Нажмите кнопку «Погода», чтобы получить прогноз на неделю для любого города.",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda message: message.text == 'Погода')
def ask_city(message):
    msg = bot.reply_to(message, "Введите название города (например: Новосибирск, ru):")
    bot.register_next_step_handler(msg, send_weather_for_city)


@bot.message_handler(commands=['weather'])
def send_weather(message):
    parts = message.text.split(maxsplit=1)
    if len(parts) == 1:
        msg = bot.reply_to(message, "Введите название города (например: Новосибирск, ru):")
        bot.register_next_step_handler(msg, send_weather_for_city)
    else:
        city = parts[1].strip()
        send_weather_for_city(message, city)


def send_weather_for_city(message, city=None):
    if city is None:
        city = message.text.strip()

    bot.send_chat_action(message.chat.id, 'typing')
    forecast = get_weather_forecast(city)

    if not forecast:
        bot.reply_to(message, "⚠️ Не удалось получить данные о погоде для этого города. "
                              "Проверьте правильность написания и попробуйте снова.")
        return

    response = f"🌦️ Прогноз погоды в {city} на 7 дней:\n\n"
    for day in forecast:
        response += (
            f"📅 <b>{day['date']}</b>\n"
            f"🌡️ Температура: от {day['temp_min']}°C до {day['temp_max']}°C\n"
            f"☁️ Погода: {day['condition'].capitalize()}\n"
            f"💧 Влажность: {day['humidity']}%\n"
            f"🌬️ Ветер: {day['wind']} м/с\n\n"
        )

    bot.send_message(message.chat.id, response, parse_mode='HTML', reply_markup=main_menu())
    import re

    def is_valid_city_name(city):
        # Разрешаем только буквы (латиницу и кириллицу), пробелы, запятые и дефисы
        pattern = r'^[a-zA-Zа-яА-ЯёЁ\s,\-]+$'
        return bool(re.match(pattern, city.strip()))

    def send_weather_for_city(message, city=None):
        if city is None:
            city = message.text.strip()

        if not is_valid_city_name(city):
            msg = bot.reply_to(message, "❌ Название города содержит недопустимые символы. "
                                        "Пожалуйста, введите название без цифр и специальных символов:")
            bot.register_next_step_handler(msg, send_weather_for_city)
            return

        bot.send_chat_action(message.chat.id, 'typing')
        forecast = get_weather_forecast(city)

        if not forecast:
            msg = bot.reply_to(message, "⚠️ Не удалось получить данные о погоде для этого города. "
                                        "Проверьте правильность написания и попробуйте снова:")
            bot.register_next_step_handler(msg, send_weather_for_city)
            return


if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
