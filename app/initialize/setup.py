from os import makedirs
from utils import exception_handler_log

@exception_handler_log
def create_data_folder():
    """Создание папки данных"""
    makedirs('data', exist_ok=True)

@exception_handler_log
def setup():
    """Настройка приложения"""
    create_data_folder()
