from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()
user_id_data = []

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_id_data:
        user_id_data.append(user_id)
    name = message.from_user.first_name
    await message.answer(f'Привет, {name}!\n'
                         f'Этот бот обслуживает уже {len(user_id_data)} человек\n'
                         'Мои команды:\n'
                         '/start - начать работу с ботом\n'
                         '/myinfo - информация о пользователе\n'
                         '/random - случайное блюдо\n')