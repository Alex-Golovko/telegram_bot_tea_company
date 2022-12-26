from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

start_up_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
black_tea_button = KeyboardButton(text='Черный чай')
green_tea_button = KeyboardButton(text='Зеленый чай')
news_button = KeyboardButton(text='Новости и Акции')
basket_button = KeyboardButton(text='Корзина')

start_up_menu.add(black_tea_button, green_tea_button, news_button, basket_button)

black_tea_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bbrand_1_button = KeyboardButton(text='Бренд 1')
bbrand_2_button = KeyboardButton(text='Бренд 2')
bbrand_3_button = KeyboardButton(text='Бренд 3')
bbrand_4_button = KeyboardButton(text='Назад')

black_tea_menu.add(bbrand_1_button, bbrand_2_button, bbrand_3_button, bbrand_4_button)

green_tea_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
gbrand_1_button = KeyboardButton(text='Бренд 1')
gbrand_2_button = KeyboardButton(text='Бренд 2')
gbrand_3_button = KeyboardButton(text='Бренд 3')
gbrand_4_button = KeyboardButton(text='Назад')

green_tea_menu.add(gbrand_1_button, gbrand_2_button, gbrand_3_button, gbrand_4_button)

