import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers.command_handlers import command_router
from handlers.messange_handlers import message_router


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    await bot.set_my_commands(commands=[
        BotCommand(command='start', description='Start/restart bot'),
        BotCommand(command='help', description='Manuel for using bot'),
        BotCommand(command='courses', description='valyuta kurslari'),
        BotCommand(command='usd', description='dollar kursi'),
        BotCommand(command='euro', description='yevro kursi'),
        BotCommand(command='ruble', description='rubl kursi'),
        BotCommand(command='week', description='valyuta kurslarining joriy haftadagi ro\'yhati')
    ])
    dp = Dispatcher()
    dp.include_routers(command_router,message_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')


