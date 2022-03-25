# import logging

# from telebot import types

# API = "5038427840:AAHioQd1ma2zmG9fxOOpShqM6NMcZXLR_IM"

# from aiogram import Bot,Dispatcher,executor,types
# from aiogram.types import inline

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API)
# dp = Dispatcher(bot)

# def welcome(message):
#     sti = open('static/salom.webp','rb')
#     bot.send_sticker(message.chat.id, sti)
    
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("Lavash")
#     item2 = types.KeyboardButton("Burger")

#     markup.add(item1,item2)

#     bot.send_message(message.chat.id,"Biror nima zakaz qilmoqchi bo'lsangiz, pastdagi menyudan tanlang!\nDostavka: 1$ = 12.000 so'm\nXomiyimiz: @buyuk_0906" , parse_mode='html', reply_markup = markup)

# @dp.message_handler(content_types=['text'])
# def lalala(message):
#     if message.chat.type == 'salom':
#         if message.text == 'exx':
#             bot.send_message(message.chat.id, "iya")
#         elif message.text == "nima gap":
#             bot.send_message(message.chat.id, "daxsh")
#         else:
#             bot.send_message(message.chat.id, "nimma diyshni bilmayma")


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = "5038427840:AAHioQd1ma2zmG9fxOOpShqM6NMcZXLR_IM"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    text_and_data = (
        ('Ha!', 'yes'),
        ('Yoq!', 'no'),
    )
    # in real life for the callback_data the callback data factory should be used
    # here the raw string is used for the simplicity
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)

    keyboard_markup.row(*row_btns)
    keyboard_markup.add(
        # url buttons have no callback data
        types.InlineKeyboardButton('salom', url='https://t.me/buyuk_0906'),
        types.InlineKeyboardButton('salon', url='https://t.me/buyuk_0906')
    )

    await message.reply("Tentakmisan?", reply_markup=keyboard_markup)


# Use multiple registrators. Handler will execute when one of the filters is OK
@dp.callback_query_handler(text='no')  # if cb.data == 'no'
@dp.callback_query_handler(text='yes')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')

    if answer_data == 'yes':
        text = "Bilgandim o'zzi🤔"
    elif answer_data == 'no':
        text = 'Aldama😂'
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_message(query.from_user.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)