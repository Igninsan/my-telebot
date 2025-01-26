from aiogram import Router, F, types

from bot_config import database

dishes_catalog_router = Router()

@dishes_catalog_router.callback_query(F.data == 'dishes_catalog')
async def dishes_catalog_handler(callback: types.CallbackQuery):
    await callback.message.answer('Наши блюда:')
    dishes_list = database.get_all_dishes()
    for dish in dishes_list:
        await callback.message.answer(
            f'Название блюда: {dish.get("name", "Без названия")}\nЦена: {dish.get("price")}\nОписание блюда: {dish.get("description", "Без описания")}')