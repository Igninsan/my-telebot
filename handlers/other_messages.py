from aiogram import Router, types

other_router = Router()

@other_router.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)