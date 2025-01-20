from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton

from bot_config import database


review_router = Router()
review_id_data = []

class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    date = State()
    rate = State()
    extra_comments = State()


@review_router.callback_query(F.data == 'review')
async def start_review(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Как вас зовут?')
    await state.set_state(RestaurantReview.name)


@review_router.message(RestaurantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    if message.from_user.id in review_id_data:
        await message.answer('Нельзя оставлять отзыв больше одного раза')
        await state.clear()
    else:
        name = message.text
        await state.update_data(name=name)
        await message.answer('Ваш номер телефона?')
        await state.set_state(RestaurantReview.phone_number)


@review_router.message(RestaurantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer('В какой день вы нас посещали?')
    await state.set_state(RestaurantReview.date)


@review_router.message(RestaurantReview.date)
async def process_date(message: types.Message, state: FSMContext):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
        [
            types.InlineKeyboardButton(text='1', callback_data='1'),
            types.InlineKeyboardButton(text='2', callback_data='2'),
            types.InlineKeyboardButton(text='3', callback_data='3'),
            types.InlineKeyboardButton(text='4', callback_data='4'),
            types.InlineKeyboardButton(text='5', callback_data='5')
        ]
    ])
    date = message.text
    await state.update_data(date=date)
    await message.answer('Поставьте нам оценку от 1 до 5', reply_markup=kb)
    await state.set_state(RestaurantReview.rate)


@review_router.callback_query(RestaurantReview.rate)
async def process_rate(callback: types.callback_query, state: FSMContext):
    rate = callback.data
    await state.update_data(rate=rate)
    await callback.message.answer('Напишите дополнительные комментарии или жалобы')
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(extra_comments=extra_comments)
    data = await state.get_data()
    await message.answer('Спасибо за ваш отзыв!')
    review_id_data.append(message.from_user.id)
    database.save_review(data)
    await state.clear()