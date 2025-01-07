import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from random import choice


token =dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher()
name_list = ['Абдыкалык', 'Айсулуу', 'Ильгиз', 'Мирбек', 'Алмазбек', 'Ислам', 'Айдар', 'Петр', 'Мухаммад', 'Кутман', 'Искендер', 'Никита']
user_id_data = []

@dp.message(Command('start'))
async def start_handler(message):
    user_id = message.from_user.id
    if user_id not in user_id_data:
        user_id_data.append(user_id)
    name = message.from_user.first_name
    await message.answer(f'Привет, {name}!\n'
                         f'Этот бот обслуживает уже {len(user_id_data)} человек\n'
                         'Мои команды:\n'
                         '/start - начать работу с ботом\n'
                         '/myinfo - информация о пользователе\n'
                         '/random - случайное имя\n')


@dp.message(Command('myinfo'))
async def myinfo_handler(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    if username is None:
        await message.answer(f'Ваш id: {user_id}\nВаше имя: {first_name}\nу Вас нет ника')
    else:
        await message.answer(f'Ваш id: {user_id}\nВаше имя: {first_name}\nВаш ник: {username}')


@dp.message(Command('random'))
async def random_handler(message):
    await message.answer(f'Случайное имя: {choice(name_list)}')


@dp.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())