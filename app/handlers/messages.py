from aiogram import Dispatcher
from aiogram import types
from utils import tool


# Обработчик текстовых сообщений
def textMessageHandler(dp: Dispatcher):
    @dp.message()
    async def echo_message(message: types.Message):
        t = await tool.message_translator(message.text, 'en')
        # await message.delete()
        # await message.answer(f"{message.from_user.first_name.upper()}*** {t}")
        await message.reply(f"{t}")

        # Проверяем, что команда вызвана в группе
        if message.chat.type in ["group", "supergroup"]:
            await message.reply("Эта команда работает только в группах!")