import logging
from functools import lru_cache

import requests
from aiogram import executor, types, Bot, Dispatcher


_TOCKEN=""
_API_SUMMARY_URL= "https://api.covid19api.com/summary"


_HELP_TEXT = {
    'ru': 'Приветствую! Я телеграмм бот который умеет рассказывать какая сейчас статистика заболеваемости COVID-19.\n'
          'Напиши "покажи статистику" или "statistics" и я расскажу какая сейчас статистика по миру. '
          'По слову Россия (/russia) и я расскажу будет ли вторая волна',

    'en': 'Greetings! I am a telegram bot that knows the current statistics for the COVID-19. \n'
          'Write "show me statistics" or /statistics and I will tell you what statistics are in the world now.'
          'Tyoe Russia /russia and I will tell you if there will be a second wave',
}


_STATISTICS_TEXT = {
    'en': "{n}. {Country} new {NewConfirmed}, total {TotalConfirmed}",
    'ru': "{n}. {Country} новых случаев {NewConfirmed}, всего {TotalConfirmed}"
}


_COUNTRY_TEXT = {
    'en': "New cases {NewConfirmed} and new recovered {NewRecovered}. Pandemic is {grow}.\n"
          "BTW Total {TotalConfirmed}, recovered {TotalRecovered} but {TotalDeaths} in the better place",
    'ru': "Новых случаев {NewConfirmed}, вылечелись вылеченные {NewRecovered}. Пандемия {grow}. \n"
          "Для справки, всего заболело {TotalConfirmed}, "
          "выздоровели {TotalRecovered}, но {TotalDeaths} в лучшем месте, явно не здесь"
}


_GROW_TEXT = {
    'en': ['slow DOWN', 'grow UP'],
    'ru': ['СПАДАЕТ, нет повода для беспокойства', 'входит во ВТОРУЮ волну']
}


bot = Bot(token=_TOCKEN)
dp = Dispatcher(bot)


def get_country(language_code, country_code='RU'):
    country = None
    contries = request_summary()
    for c in contries:
        if c['CountryCode'] == country_code:
            country = c
            break
    if country is None:
        return f"Country with code {country_code} not found :-("
    grow = country['NewConfirmed'] > country['NewRecovered']
    grow = _GROW_TEXT[language_code][int(grow)]
    return _COUNTRY_TEXT[language_code].format(grow=grow, **country)


def get_language_code(message: types.Message):
    user: types.User = message.from_user
    language_code = user.language_code
    if language_code not in _HELP_TEXT:
        language_code = 'ru'
    return language_code


@lru_cache
def request_summary():
    response = requests.get(_API_SUMMARY_URL)
    countries = response.json()['Countries']
    countries.sort(key=lambda x: -x['NewConfirmed'])
    return countries


def get_summary(language_code, amount=10):
    countries = request_summary()
    lines = []
    text_template = _STATISTICS_TEXT[language_code]
    for n, country in enumerate(countries[:amount]):
        lines.append(text_template.format(**country, n=n))
    return '\n'.join(lines)


@dp.message_handler(regexp='.*(statist|статистик|мир|всего).*')
async def statistics_text(message: types.Message):
    await message.reply(get_summary(get_language_code(message)))


@dp.message_handler(commands=['statistics', 'world'])
async def statistics_cmd(message: types.Message):
    await message.reply(get_summary(get_language_code(message)))


@dp.message_handler(commands=['russia', 'ru'])
async def country_ru_cmd(message: types.Message):
    await message.reply(get_country(get_language_code(message), 'RU'))


@dp.message_handler(commands=['usa', 'ru'])
async def country_ru_cmd(message: types.Message):
    await message.reply(get_country(get_language_code(message), 'RU'))


@dp.message_handler(regexp='.*(ussi|оссия).*')
async def country_ru_text(message: types.Message):
    await message.reply(get_country(get_language_code(message), 'RU'))


@dp.message_handler(regexp='.*(help|start|умеешь|помощь).*')
async def welcome_text(message: types.Message):
    await message.reply(_HELP_TEXT[get_language_code(message)])


@dp.message_handler(commands=['start', 'help'])
async def welcome_cmd(message: types.Message):
    await message.reply(_HELP_TEXT[get_language_code(message)])


@dp.message_handler()
async def default(message: types.Message):
    await message.answer(f"I head {message.text} but don't know what to do. Type /help for help")


if __name__ == '__main__':
    logging.root.setLevel(logging.INFO)
    executor.start_polling(dp, skip_updates=True)

