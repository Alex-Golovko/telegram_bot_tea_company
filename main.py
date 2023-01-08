import logging
import re

from aiogram.types import CallbackQuery, inline_query
from aiogram import Bot, Dispatcher, types, executor
from config import API_TOKEN
from keybords import start_up_menu, black_tea_menu, green_tea_menu
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class ShopCart(StatesGroup):
    choice = State()
    add_to_cart = State()
    order = State()
    name = State()
    mail = State()
    adminchange = State()

logging.basicConfig(filename='logs.log', level=logging.INFO)
bot = Bot(token=API_TOKEN,)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Добро пожаловать в наш чайный магазин\n'
                        'где вы сможете выбрать подходщий чай для себя.\n'
                        'Приятного чаяпития!', reply_markup=start_up_menu)
    await message.delete()

@dp.message_handler(text="admin", state='*')
async def admin_check(message: types.Message):
    user_id = message.chat.id
    admin_ind = False
    first_admin = 498618666
    print(user_id)
    if user_id == first_admin:
        print("Nice")
        await message.reply(text="darova admin") #, reply_markup=admin_start_markup()
        admin_ind = True
    else:
        print("fuckoff")
    print(message.chat.id)

@dp.message_handler(text='Назад', state='*')
async def back_button_commands(message: types.Message):
    await message.reply('Выберите какой чай вы хотите приобрести', reply_markup=start_up_menu)


@dp.message_handler(text=['Новости и Акции'])
async def avto_blogs(message: types.Message):
    await message.answer('Текущие товары по акции:') #, reply_markup=sales_markup()

@dp.message_handler(text=['Черный чай'], state='*')
async def black_tea_command(message: types.Message):
    await message.reply('Выберите производителя который вы любите', reply_markup=black_tea_menu)

@dp.message_handler(text=['Richard Black'], state='*')
async def richard_black(message: types.Message):
    photo = types.InputFile('photo/Richard_blac.jpg')
    await message.answer_photo(photo=photo)
    await message.answer('Доступны упаковки по 25 пакетиков (100 рублей), \n'
                         'по 100 пакетиков (400 рублей)')
    await message.answer('Выбери из списка') #, reply_markup = item_markup(table='autocarp', admin_ind=0)

@dp.message_handler(text=['Richard Green'], state='*')
async def richard_black(message: types.Message):
    photo = types.InputFile('photo/Richard_green.jpg')
    await message.answer_photo(photo=photo)
    await message.answer('Доступны упаковки по 25 пакетиков (100 рублей), \n'
                         'по 100 пакетиков (400 рублей)')
    await message.answer('Выбери из списка') #, reply_markup = item_markup(table='autocarp', admin_ind=0)

@dp.message_handler(text=['Greenfield Black'], state='*')
async def richard_black(message: types.Message):
    photo = types.InputFile('photo/Greenfield_black.jpg')
    await message.answer_photo(photo=photo)
    await message.answer('Доступны упаковки по 25 пакетиков (100 рублей), \n'
                         'по 100 пакетиков (400 рублей)')
    await message.answer('Выбери из списка') #, reply_markup = item_markup(table='autocarp', admin_ind=0)

@dp.message_handler(text=['Greenfield Green'], state='*')
async def richard_black(message: types.Message):
    photo = types.InputFile('photo/Greenfield_green.jpg')
    await message.answer_photo(photo=photo)
    await message.answer('Доступны упаковки по 25 пакетиков (100 рублей), \n'
                         'по 100 пакетиков (400 рублей)')
    await message.answer('Выбери из списка') #, reply_markup = item_markup(table='autocarp', admin_ind=0)

@dp.message_handler(text=['Lipton Black'], state='*')
async def richard_black(message: types.Message):
    photo = types.InputFile('photo/Lipton_black.jpg')
    await message.answer_photo(photo=photo)
    await message.answer('Доступны упаковки по 25 пакетиков (100 рублей), \n'
                         'по 100 пакетиков (400 рублей)')
    await message.answer('Выбери из списка') #, reply_markup = item_markup(table='autocarp', admin_ind=0)

@dp.message_handler(text=['Lipton Green'], state='*')
async def richard_black(message: types.Message):
    photo = types.InputFile('photo/Lipton_green.jpg')
    await message.answer_photo(photo=photo)
    await message.answer('Доступны упаковки по 25 пакетиков (100 рублей), \n'
                         'по 100 пакетиков (400 рублей)')
    await message.answer('Выбери из списка') #, reply_markup = item_markup(table='autocarp', admin_ind=0)

@dp.message_handler(text=['Зеленый чай'], state='*')
async def green_tea_command(message: types.Message):
    await message.reply('Выберите производителя который вы любите', reply_markup=green_tea_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)