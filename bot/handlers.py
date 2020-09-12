from aiogram import types
from pathlib import Path
from .core import dp

__all__ = ['send_welcome', 'cats', 'echo']


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    cat = Path('data/cat.png').read_bytes()
    await message.reply_photo(cat, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f'I head {message.text}')
