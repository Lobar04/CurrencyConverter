from datetime import datetime, timedelta

from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
import requests
from aiogram.utils.chat_action import ChatActionSender

command_router = Router()

@command_router.message(CommandStart())
async def start_handler(message: Message):
    a = ('Assalomu alaykum.\n'
         'Xush kelibsiz.\n'
         'Bot haqida ko\'proq ma\'lumotga ega bo\'lishni hohlasangiz /help ni bosing.')
    await message.answer(text=a)


@command_router.message(Command('help', prefix='!/#'))
async def help_handler(message: Message):
    a = ('Bu botda quyidagi komandallardan foydalanishingiz mumkin:\n\t/courses - hamma kurslar haqidagi ma\'lumotni ekranga chiqaradi\n\t/usd - dollar kursini ko\'rish uchun\n\t/euro - yevro kursini ko\'rish uchun\n\t/ruble - rubl kursini ko\'rish uchun\n\t/week - joriy haftadagi valyuta kurslarini ko\'rish uchun.\n\nAgar sizga biror sanadagi valyuta kursi kerak bo\'lsa yyyy-mm-dd (usd,euro,rubl) kabi habar yuborasiz.\nMasalan: 2012-02-12 USD yoki USD 2012-02-12 yoki 2012-02-12dollar kabi\n\n')
    a += ("Agar biror sonni boshida yoki oxirida valyuta belgilari bilan kiritsangiz uni so'mda qancha bo'lishini hisoblab beradi.Agar son (dollar,yevro,rubl) kabi kiritsangiz ham hisoblab beradi")

    await message.answer(text=a)


@command_router.message(Command('courses', prefix='!/#'))
async def courses_handler(message: Message):
    a = 'Bugungi valyuta kurslari ro\'yhati:\n\n\t'
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.from_user.id):
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
        js = response.json()
        for i in range(3):
            a+=f'{js[i]["CcyNm_UZ"]}:\t{js[i]["Rate"]} so\'m \n\n\t'

    await message.answer(text=a)



@command_router.message(Command('usd', prefix='!/#'))
async def usd_handler(message: Message):
    a = ('Bugungi dollar kursi:')
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.from_user.id):
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
        js = response.json()
        a += f'\t{js[0]["Rate"]} so\'m.'

    await message.answer(text=a)


@command_router.message(Command('euro', prefix='!/#'))
async def euro_handler(message: Message):
    a = ('Bugungi yevro kursi:')
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.from_user.id):
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
        js = response.json()
        a += f'\t{js[1]["Rate"]} so\'m.'
    await message.answer(text=a)


@command_router.message(Command('ruble', prefix='!/#'))
async def EURO_handler(message: Message):
    a = ('Bugungi Rossiya rubl kursi:')
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.from_user.id):
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
        js = response.json()
        a += f'\t{js[2]["Rate"]} so\'m.'
    await message.answer(text=a)


@command_router.message(Command('week', prefix='/!#'))
async def week_handler(message: Message):
    a = 'Valyuta kurslarining joriy haftadagi ro\'yhati:\n\n\n'
    today = datetime.now().date()
    last_7_days_dates = [today - timedelta(days=i) for i in range(7)]
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.from_user.id):
        r = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
        for i in last_7_days_dates:
            response = requests.get(r+f'all/{i}/')
            js = response.json()
            a +=f"{i}:\n\tUSD - {js[0]['Rate']} so'm\n\tEUR - {js[1]['Rate']} so'm\n\tRUB - {js[2]['Rate']} so'm\n\n"

    await message.answer(text=a)




