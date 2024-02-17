from aiogram import Router, F
from aiogram.types import Message , InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router
import requests
from aiogram.utils.chat_action import ChatActionSender

message_router = Router()
@message_router.message(F.text.isnumeric())
async def exchange_handler(message: Message):
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    js = response.json()
    a = f"{message.text} so\'m boshqa valyutalarda:\n\n {int(message.text) / float(js[0]['Rate']): f} {js[0]['CcyNm_UZ']}\n\n"
    a+= f"{int(message.text) / float(js[1]['Rate']): f} {js[1]['CcyNm_UZ']}\n\n"
    a+= f"{int(message.text) / float(js[2]['Rate']): f} {js[2]['CcyNm_UZ']}"
    await message.reply(text=a)


@message_router.message(F.text.contains('$'))
async def sum_handler(message: Message):
    x = message.text
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    js = response.json()
    if x[:-1].isnumeric():
        a = f"{x} - {int(x[:-1])*float(js[0]['Rate'])} so'm"
    elif x[1:].isnumeric():
        a = f"{x} - {int(x[1:])*float(js[0]['Rate'])} so'm"
    else:
        a = 'Xato kiritdingiz.'


    await message.reply(a)


@message_router.message(F.text.contains('€'))
async def sum_handler(message: Message):
    x = message.text
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    js = response.json()
    if x[:-1].isnumeric():
        a = f"{x} - {int(x[:-1])*float(js[1]['Rate'])} so'm"
    elif x[1:].isnumeric():
        a = f"{x} - {int(x[1:])*float(js[1]['Rate'])} so'm"
    else:
        a = 'Xato kiritdingiz.'


    await message.reply(a)

@message_router.message(F.text.contains('₽'))
async def sum_handler(message: Message):
    x = message.text
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    js = response.json()
    if x[:-1].isnumeric():
        a = f"{x} - {int(x[:-1])*float(js[2]['Rate'])} so'm"
    elif x[1:].isnumeric():
        a = f"{x} - {int(x[1:]) * float(js[2]['Rate'])} som"
    else:
        a = 'Xato kiritdingiz'


    await message.reply(a)


@message_router.message(F.text.contains(' dollar'))
async def sum_handler(message: Message):
    x = message.text
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    js = response.json()
    if x[:--7].isnumeric():
        a = f"{x} - {int(x[:-7])*float(js[0]['Rate'])} so'm"
    else:
        a = 'Xato kiritdingiz'


    await message.reply(a)

@message_router.message(F.text.contains(' yevro'))
async def sum_handler(message: Message):
    x = message.text
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    js = response.json()
    if x[:--7].isnumeric():
        a = f"{x} - {int(x[:-7])*float(js[1]['Rate'])} so'm"
    else:
        a = 'Xato kiritdingiz'


    await message.reply(a)

@message_router.message(F.text.contains(' rubl'))
async def sum_handler(message: Message):
    x = message.text
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    js = response.json()
    if x[:--7].isnumeric():
        a = f"{x} - {int(x[:-7])*float(js[2]['Rate'])} so'm"
    else:
        a = 'Xato kiritdingiz'


    await message.reply(a)

@message_router.message(F.text.contains('-'))
async def sum_handler(message: Message):
    x = message.text
    if x[:4].isnumeric() and x[4]=='-' and x[5:7].isnumeric() and x[7]=='-' and x[8:10].isnumeric():
        if x[10:] =='dollar' or x[10:]==' USD':
            y = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/{x[:9]}/'
            response = requests.get(y)
            js = response.json()
            a = f"{x} {js[0]['Rate']} so'm"
        elif x[10:]=='yevro' or x[10:]==' EUR':
            y = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/{x[0:10]}/'
            response = requests.get(y)
            js = response.json()
            a = f"{x} {js[0]['Rate']} so'm"

        elif x[10:]=='rubl' or x[10:]==' RUB':
            y = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/RUB/{x[0:10]}/'
            response = requests.get(y)
            js = response.json()
            a = f"{x} {js[0]['Rate']} so'm"
        else:
            a = f'Xato kiritdingiz.'
    elif x[4:8].isnumeric() and x[8]=='-' and x[9:11].isnumeric() and x[11]=='-' and x[12:].isnumeric() and len(x)==14:
        if x[:4]=='USD ':
            y = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/{x[4:]}/'
            response = requests.get(y)
            js = response.json()
            a = f"{x} {js[0]['Rate']} so'm"
        elif x[:4]=='EUR ':
            y = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/{x[4:]}/'
            response = requests.get(y)
            js = response.json()
            a = f"{x} {js[0]['Rate']} so'm"

        elif x[:4]=='RUB ':
            y = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/RUB/{x[4:]}/'
            response = requests.get(y)
            js = response.json()
            a = f"{x} {js[0]['Rate']} so'm"
        else:
            a = f'Xato kiritdingiz.'
    else:
        a = 'Xato kiritdingiz'

    await message.reply(a)




