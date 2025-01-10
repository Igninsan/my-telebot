from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()

@myinfo_router.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    if username is None:
        await message.answer(f'Ваш id: {user_id}\nВаше имя: {first_name}\nу Вас нет ника')
    else:
        await message.answer(f'Ваш id: {user_id}\nВаше имя: {first_name}\nВаш ник: {username}')