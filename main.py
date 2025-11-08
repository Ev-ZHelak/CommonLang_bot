import asyncio
from app.bot import create_bot_dispatcher, setup_commands
from app.handlers import textMessageHandler, commandMessageHandler
from app.database.manager import DatabaseManager


# Запуск бота
async def main():
    db = DatabaseManager()
    db.create_user_table()

    # Создание бота и диспетчера
    bot, dp = create_bot_dispatcher()

    # Установка команд
    await setup_commands()

    # Обработчик команд
    commandMessageHandler(dp)

    # Обработчик текстовых сообщений
    textMessageHandler(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())