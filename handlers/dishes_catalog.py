from aiogram import Router, F, types


catalog_router = Router()

@catalog_router.callback_query(F.data == 'dishes_catalog')
async def dishes_catalog_handler(callback: types.CallbackQuery):
    await callback.message.answer('Наши блюда: борщ, омлет, салат "Ёжик"')