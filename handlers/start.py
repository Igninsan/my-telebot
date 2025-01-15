from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()
user_id_data = []

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_id_data:
        user_id_data.append(user_id)

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='каталог блюд', callback_data='dishes_catalog'),
                types.InlineKeyboardButton(text='реклама', callback_data='advertisement')
            ],
            [
                types.InlineKeyboardButton(text='обратная связь', callback_data='feedback'),
                types.InlineKeyboardButton(text='о нас', callback_data='about_us')
            ],
            [
                types.InlineKeyboardButton(text='оставить отзыв', callback_data='review')
            ]
        ]
    )

    name = message.from_user.first_name
    await message.answer(f'Привет, {name}!\n'
                         f'Этот бот обслуживает уже {len(user_id_data)} человек\n'
                         'Мои команды:\n'
                         '/start - начать работу с ботом\n'
                         '/myinfo - информация о пользователе\n'
                         '/random - случайное блюдо\n', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us_handler(callback: types.CallbackQuery):
    await callback.message.answer('Мы - ресторан "Победа"')