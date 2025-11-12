import sqlite3
from app.database.models import User
from . import queries
import config


class DatabaseManager:
    def __init__(self):
        config.get_database_path()
        self.dbPath = config.get_database_path()

    def _get_connection(self):
        """Получение соединения с БД"""
        conn = sqlite3.connect(self.dbPath)
        conn.row_factory = sqlite3.Row  # Для доступа к колонкам по имени
        return conn

    def create_user_table(self):
        """Создание таблици пользователя"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(queries.CREATE_USERS_TABLE)
