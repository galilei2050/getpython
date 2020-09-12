from argparse import ArgumentParser
from aiogram import Bot, Dispatcher


parser = ArgumentParser()
parser.add_argument('-t', '--token', help='Bot token', required=True)
args = parser.parse_args()


# Initialize bot and dispatcher
bot = Bot(token=args.token)
dp = Dispatcher(bot)
