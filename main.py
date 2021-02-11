import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram.types import reply_keyboard
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram.types import KeyboardButton
import asyncio
logging.basicConfig(level=logging.INFO)

bot = Bot(token='1276910299:AAHzjDM1Z02_eSYBhR5uiB2m2LHtgZnYxrI')
dp = Dispatcher(bot)



token = "1276910299:AAHzjDM1Z02_eSYBhR5uiB2m2LHtgZnYxrI"
URL = 'https://api.telegram.org/bot' + token + '/'
#https://api.telegram.org/bot1276910299:AAHzjDM1Z02_eSYBhR5uiB2m2LHtgZnYxrI/setWebhook?url=https://dd50f1ea6479.ngrok.io/

button1 = KeyboardButton('Анекдоты')
button2 = KeyboardButton('Рассказы')
button3 = KeyboardButton('Афоризмы')
button4 = KeyboardButton('Цитаты')
button5 = KeyboardButton('Тосты')
button6 = KeyboardButton('Статусы')
button7 = KeyboardButton('Анекдоты (18+)')
button8 = KeyboardButton('Рассказы (18+)')
button9 = KeyboardButton('Афоризмы (18+)')
button10 = KeyboardButton('Цитаты (18+)')
button11 = KeyboardButton('Тосты (18+)')
button12 = KeyboardButton('Статусы (18+)')
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.insert(button1)
menu.insert(button2)
menu.insert(button3)
menu.insert(button4)
menu.insert(button5)
menu.insert(button6)
menu.insert(button7)
menu.insert(button8)
menu.insert(button9)
menu.insert(button10)
menu.insert(button11)
menu.insert(button12)
# start
@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    sticker = open('./welcome_sticker.jpg', 'rb')
    await bot.send_sticker(message.chat.id, sticker)
    await message.reply(f"Добрый вечер, {message.from_user.first_name}!\n", reply_markup=menu)



@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    if str(message["text"]) == 'Анекдоты':
        await bot.send_message(message.chat.id,
                           get_anekdot(1))
    elif str(message["text"]) == 'Рассказы':
        await bot.send_message(message.chat.id,
                           get_anekdot(2))
    elif str(message["text"]) == 'Афоризмы':
        await bot.send_message(message.chat.id,
                           get_anekdot(4))
    elif str(message["text"]) == 'Цитаты':
        await bot.send_message(message.chat.id,
                           get_anekdot(5))
    elif str(message["text"]) == 'Тосты':
        await bot.send_message(message.chat.id,
                           get_anekdot(6))
    elif str(message["text"]) == 'Статусы':
        await bot.send_message(message.chat.id,
                           get_anekdot(8))
    elif str(message["text"]) == 'Анекдоты (18+)':
        await bot.send_message(message.chat.id,
                           get_anekdot(11))
    elif str(message["text"]) == 'Рассказы (18+)':
        await bot.send_message(message.chat.id,
                           get_anekdot(12))
    elif str(message["text"]) == 'Афоризмы (18+)':
        await bot.send_message(message.chat.id,
                           get_anekdot(14))
    elif str(message["text"]) == 'Цитаты (18+)':
        await bot.send_message(message.chat.id,
                           get_anekdot(15))
    elif str(message["text"]) == 'Тосты (18+)':
        await bot.send_message(message.chat.id,
                           get_anekdot(16))
    elif str(message["text"]) == 'Статусы (18+)':
        await bot.send_message(message.chat.id,
                           get_anekdot(18))
    else:
        await bot.send_message(message.chat.id,
                               "С мамкой своей так будешь базарить.")


def get_anekdot(n):
    #url = 'https://yobit.net/api/2/btc_usd/ticker'
    #print("Выберите категорию:\n1 - Анекдот; \n2 - Рассказы; \n3 - Стишки;\n4 - Афоризмы;\n5 - Цитаты;\n6 - Тосты;\n8 - Статусы;\n11 - Анекдот (+18);\n12 - Рассказы (+18);\n13 - Стишки (+18);\n14 - Афоризмы (+18);\n15 - Цитаты (+18);\n16 - Тосты (+18);\n18 - Статусы (+18);")
    #n=input()
    #n=1
    url = 'http://rzhunemogu.ru/RandJSON.aspx?CType={}'.format(n)
    response = requests.get(url).text
    y = response.rfind('"')
    return response[12:y]


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

