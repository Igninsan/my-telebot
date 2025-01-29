from aiogram import Router, F, types
from aiogram_widgets.pagination import TextPaginator

from bot_config import database

dishes_catalog_router = Router()

@dishes_catalog_router.callback_query(F.data == 'dishes_catalog')
async def dishes_catalog_handler(callback: types.CallbackQuery):
    await callback.message.answer('Наши блюда:')
    dishes_list = database.get_all_dishes()
    for dish in dishes_list:
        image = dish.get('image')
        await callback.message.answer_photo(photo=image, caption=
            f'Название блюда: {dish.get("name", "Без названия")}\nЦена: {dish.get("price")}\nОписание блюда: {dish.get("description", "Без описания")}\nКатегория: {dish.get("category")}\nВарианты порций: {dish.get("options")}')

@dishes_catalog_router.callback_query(F.data == 'dishes_catalog_pagination')
async def dishes_catalog_pagination_handler(callback: types.CallbackQuery):
    await callback.message.answer('Наш каталог блюд:')
    dishes_list = database.get_all_dishes()

    text_data = [
f'Название блюда: {dish.get("name", "Без названия")}\nЦена: {dish.get("price")}\nОписание блюда: {dish.get("description", "Без описания")}\nКатегория: {dish.get("category")}\nВарианты порций: {dish.get("options")}' for dish in dishes_list
]
    paginator = TextPaginator(data=text_data, router=dishes_catalog_router, per_page=1)
    current_text_chunk, reply_markup = paginator.current_message_data

    await callback.message.answer(text=current_text_chunk, reply_markup=reply_markup)