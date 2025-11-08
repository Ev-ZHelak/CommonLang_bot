from config import get_bot_token
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

BOT: Bot | None = None
DP: Dispatcher | None = None


def create_bot_dispatcher() -> tuple[Bot, Dispatcher]:
    global BOT, DP

    if BOT is None:
        BOT = Bot(token=get_bot_token())
    if DP is None:
        DP = Dispatcher()

    return BOT, DP


async def setup_commands():
    """Установка команд для личных чатов и групп (async)"""

    # Команды для личных чатов
    private_commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="profile", description="Профиль"),
        BotCommand(command="settings", description="Настройки"),
    ]

    # Команды для групп
    group_commands = [
        BotCommand(command="admins", description="Список админов"),
        BotCommand(command="info", description="Инфо о чате"),
        BotCommand(command="report", description="Пожаловаться"),
    ]

    if BOT is None:
        raise SystemExit("Bot not initialized")

    # Устанавливаем команды для разных типов чатов
    await BOT.set_my_commands(
        private_commands,
        scope=BotCommandScopeAllPrivateChats()
    )

    await BOT.set_my_commands(
        group_commands,
        scope=BotCommandScopeAllGroupChats()
    )
