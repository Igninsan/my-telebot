from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot_config import database


dish_admin_router = Router()


class Dish(StatesGroup):
    name = State()
    price = State()
    description = State()
    category = State()
    options = State()


@dish_admin_router.message(Command('newdish'))
async def new_book(message: types.Message, state: FSMContext):
    await message.answer('Введите название блюда')
    await state.set_state(Dish.name)


@dish_admin_router.message(Dish.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену блюда')
    await state.set_state(Dish.price)


@dish_admin_router.message(Dish.price)
async def process_price(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit():
        await message.answer('Введите число')
        return
    price = int(price)
    if price <= 0:
        await message.answer('Введите положительное число')
        return
    await state.update_data(price=message.text)
    await message.answer('Введите описание блюда')
    await state.set_state(Dish.description)


@dish_admin_router.message(Dish.description)
async def process_name(message: types.Message, state: FSMContext):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
        [
            types.InlineKeyboardButton(text='первое', callback_data='первое'),
            types.InlineKeyboardButton(text='второе', callback_data='второе'),
            types.InlineKeyboardButton(text='пицца', callback_data='пицца'),
            types.InlineKeyboardButton(text='салаты', callback_data='салаты')
            ],
        [
            types.InlineKeyboardButton(text='горячие напитки', callback_data='горячие напитки'),
            types.InlineKeyboardButton(text='холодные напитки', callback_data='холодные напитки'),
            types.InlineKeyboardButton(text='горячительные напитки', callback_data='горячительные напитки')]
        ])
    await state.update_data(description=message.text)
    await message.answer('Введите категорию блюда', reply_markup=kb)
    await state.set_state(Dish.category)


@dish_admin_router.callback_query(Dish.category)
async def process_name(callback: types.callback_query, state: FSMContext):
    await state.update_data(category=callback.data)
    await callback.message.answer('Введите варианты порций блюда')
    await state.set_state(Dish.options)


@dish_admin_router.message(Dish.options)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(options=message.text)
    await message.answer('Спасибо, блюдо было добавлено')
    data = await state.get_data()
    print(data)
    database.save_dish(data)
    await state.clear()