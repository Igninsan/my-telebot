from aiogram import Router, F, types

group_router = Router()
group_router.message.filter(F.chat.type != 'private')

BAD_WORDS = ('тупой', 'дурак')

@group_router.message(F.text)
async def echo_handler(message: types.Message):
    for word in BAD_WORDS:
        if word in message.text.lower():
            author_id = message.from_user.id
            await message.reply('Не ругайся!')
            await message.chat.ban(author_id)