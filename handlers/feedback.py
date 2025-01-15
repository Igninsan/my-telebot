from aiogram import Router, F, types


feedback_router = Router()

@feedback_router.callback_query(F.data == 'feedback')
async def feedback_handler(callback: types.CallbackQuery):
    await callback.message.answer('для обратной связи пишите на номер +996555678901')