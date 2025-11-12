import logging
from logging.handlers import RotatingFileHandler
from sys import stdout
from config import LOG_FOLDER, LOG_LEVEL
from functools import wraps
import inspect
from os import makedirs


def create_logging(NAME_LOGGER: str = 'bot', NAME_FILE: str ='app', CONCOL: bool = True) -> logging.Logger:
    # Создание папки для логов
    makedirs(LOG_FOLDER, exist_ok=True)

    level_mapping = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    if level_mapping.get(LOG_LEVEL.upper()):
        level = level_mapping[LOG_LEVEL]
    else:
        level = logging.NOTSET

    # Создаем логгер
    logger = logging.getLogger(NAME_LOGGER)
    logger.setLevel(level)

    # Форматтер
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Handler для файла
    file_handler = RotatingFileHandler(
        f'{LOG_FOLDER}/{NAME_FILE}.log',
        maxBytes=1024 * 1024,  # 1 MB
        backupCount=5,  # хранить 5 backup файлов
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    if CONCOL:
        # Handler для консоли
        console_handler = logging.StreamHandler(stdout)
        console_handler.setFormatter(formatter)

        # Добавляем оба handler
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

APP_LOGGER = create_logging()
USER_LOGGER = create_logging(NAME_LOGGER='user', NAME_FILE='user_action')
ERROR_LOGEER = create_logging(NAME_LOGGER='err', NAME_FILE='error')

def exception_handler_log(func):
    '''Обработчик исключений с логированием (декоратор)'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            APP_LOGGER.debug('|'.join((
                f'module:{func.__module__}',
                f'func:{func.__name__}',
                f'sig:{inspect.signature(func)}',
                f'doc:{func.__doc__}',
                f'*args:{args}',
                f'**kwargs:{kwargs}'
            )))
            APP_LOGGER.info('|'.join((
                f'module:{func.__module__}',
                f'func:{func.__name__}',
                f'doc:{func.__doc__}',
            )))

            return func(*args, **kwargs)

        except Exception as err:
            error_mesage = '|'.join((
                f'module:{func.__module__}',
                f'func:{func.__name__}',
                f'sig:{inspect.signature(func)}',
                f'doc:{func.__doc__}',
                f'*args:{args}',
                f'**kwargs:{kwargs}',
                f'err:{err}'
            ))
            APP_LOGGER.error(error_mesage)
            ERROR_LOGEER.error(error_mesage)

            return False
    return wrapper
