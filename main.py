from aiogram import Bot, Dispatcher, types, executor
from config import API_TOKEN
from keybords import start_up_menu, black_tea_menu, green_tea_menu

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer('Добро пожаловать в наш чайный магазин\n'
                        'где вы сможете выбрать подходщий чай для себя.\n'
                        'Приятного чаяпития!', reply_markup=start_up_menu)
    await message.delete()

@dp.message_handler(text='Назад')
async  def back_button_commands(message: types.Message):
    await message.reply('Выберите какой чай вы хотите приобрести', reply_markup=start_up_menu)

@dp.message_handler(text=['Черный чай'])
async def black_tea_command(message: types.Message):
    await message.reply('Выберите производителя который вы любите', reply_markup=black_tea_menu)


@dp.message_handler(text=['Зеленый чай'])
async def black_tea_command(message: types.Message):
    await message.reply('Выберите производителя который вы любите', reply_markup=green_tea_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)