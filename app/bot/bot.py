from config import get_bot_token
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

_BOT: Bot | None = None
_DP: Dispatcher | None = None


def create_bot_dispatcher() -> tuple[Bot, Dispatcher]:
    global _BOT, _DP
    if _BOT is None:
        _BOT = Bot(token=get_bot_token())
    if _DP is None:
        _DP = Dispatcher()
    return _BOT, _DP


async def setup_commands():
    """Установка команд для личных чатов и групп (async)"""

    # Команды для личных чатов
    private_commands = [
        BotCommand(command="start", description="Запустить бота"),
        # BotCommand(command="language", description="Язык интерфейса"),
        BotCommand(command="translate", description="Автоперевод вкл/выкл"),
        BotCommand(command="settings", description="Настройки"),
        BotCommand(command="status", description="Текущие настройки"),
        BotCommand(command="help", description="Список команд"),
    ]

    # Команды для групп
    group_commands = [
        BotCommand(command="report", description="Пожаловаться"),
    ]

    if _BOT is None:
        raise SystemExit("Bot not initialized")

    # Устанавливаем команды для разных типов чатов
    await _BOT.set_my_commands(
        private_commands,
        scope=BotCommandScopeAllPrivateChats()
    )

    await _BOT.set_my_commands(
        group_commands,
        scope=BotCommandScopeAllGroupChats()
    )
