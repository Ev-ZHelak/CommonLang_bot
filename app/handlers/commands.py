from aiogram import Dispatcher, types
from aiogram.filters import Command


# Обработчик команд
def commandMessageHandler(dp: Dispatcher):
    # /start
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer(
            "Привет! Я бот-переводчик. Добавь меня в группу, "
            "назначь администратором (с правом 'Отправка сообщений'), и используй "
            "команду /setup в самой группе для настройки"
        )