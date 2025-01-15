from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


review_router = Router()
review_id_data = []

class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
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
        await message.answer('Ваш номер телефона?')
        await state.set_state(RestaurantReview.phone_number)


@review_router.message(RestaurantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    await message.answer('Поставьте нам оценку от 1 до 5')
    await state.set_state(RestaurantReview.rate)


@review_router.message(RestaurantReview.rate)
async def process_rate(message: types.Message, state: FSMContext):
    await message.answer('Напишите дополнительные комментарии или жалобы')
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await message.answer('Спасибо за ваш отзыв!')
    review_id_data.append(message.from_user.id)
    await state.clear()