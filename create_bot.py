from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot('6091681632:AAH5G5tOkVZbICXFvDwxf0dd23u2xl74Oio')
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
