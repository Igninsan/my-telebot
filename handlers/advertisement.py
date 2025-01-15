from aiogram import Router, F, types


advertisement_router = Router()

@advertisement_router.callback_query(F.data == 'advertisement')
async def advertisement_handler(callback: types.CallbackQuery):
    await callback.message.answer('С предложением о рекламе пишите на почту: restaurantPobeda@yandex.ru')