import logging
from aiogram import executor
from .core import dp
from .handlers import *


if __name__ == '__main__':
    logging.root.setLevel(logging.INFO)
    executor.start_polling(dp, skip_updates=True)
