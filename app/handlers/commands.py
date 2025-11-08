from aiogram import Dispatcher, types
from aiogram.filters import Command


# Обработчик команд
def commandMessageHandler(dp: Dispatcher):
    # /start
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Привет! Я эхо-бот. Просто отправь мне любое сообщение!")