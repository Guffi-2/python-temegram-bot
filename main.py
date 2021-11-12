import asyncio
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

import keyb as kb
from config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, пожалуйста зарегестрируйтесь или войдите. (Внимание вы запишитесь как {0.username} и если у вас нет аккаунта зарегистрируйтесь! Если вы зарегистрировались но у вас еть аккаун просто нажмите выход! Если вы просто так нажмёте "Регистрация" и у вас есть аккаунт из-за этого у вас откроется новое окно и оно не будет сохронять ввод. Если у вас нет аккаунта и вы нажмёте "Вход" вы не сохранитесь и мы не сможем вернуть данные!)'.format(message.from_user), reply_markup=kb.Mnum_1)

@dp.message_handler(commands=['регистрация_📃'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать, {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)
    conn = sqlite3.connect('People.db')

    cur = conn.cursor()

    cur.execute('INSERT INTO Users VALUES ("{0.username}", NULL, "{0.id}");'.format(message.from_user))
    conn.commit()

@dp.message_handler(commands=['Вход_📄'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()

    cur.execute('SELECT *FROM Users WHERE username = "Programmer_f" AND userid = "1350804202";'.format(message.from_user))
    conn.commit()

@dp.message_handler(commands=['регистрация_📃'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)


@dp.message_handler(commands=['курсы_валют_📈'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот список валют!'.format(message.from_user), reply_markup=kb.Mnum_3)

@dp.message_handler(commands=['Выход_🚪'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выход из аккаунта!'.format(message.from_user), reply_markup=kb.Mnum_1)

@dp.message_handler(commands=['доллар_руб_💵'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'этого нету пока что.', reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['📰_Новости'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот сводка новостей', reply_markup=kb.MNews)

@dp.message_handler(commands=['📈_Крипто'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Цены на крипту! (Внимание цены в 💵!)', reply_markup=kb.MKnum)

@dp.message_handler(commands=['Крипто'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости по крипте!', reply_markup=kb.MnBitcoin_2)

@dp.message_handler(commands=['Назад'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Назад!', reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['⚙_Настройки'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Настройки', reply_markup=kb.Mse)

@dp.message_handler(commands=['Bitcoin'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Bitcoin!', reply_markup=kb.MBitcoin)

@dp.message_handler(commands=['Bitcoin_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости о Bitcoin! https://ru.investing.com/crypto/bitcoin/news', reply_markup=kb.MnBitcoin_3)

@dp.message_handler(commands=['Ethereum'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ethereum!', reply_markup=kb.MEthereum)

@dp.message_handler(commands=['Ethereum_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости о Ethereum! https://ru.investing.com/crypto/ethereum/news', reply_markup=kb.MNEthereum)

@dp.message_handler(commands=['Binance_Coin_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости о Binance Coin! https://ru.investing.com/crypto/binance-coin/news', reply_markup=kb.MNBinance_Coin)

@dp.message_handler(commands=['📈_Акции'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите тикет Акции!', reply_markup=kb.Ak)

@dp.message_handler(commands=['💵_Валюты'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Валюты!', reply_markup=kb.NM)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
