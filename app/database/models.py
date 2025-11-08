from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    user_id: int
    username: str | None
    first_name: str
    last_name: str | None
    phone_number: str | None
    language_code: str | None
    is_premium: bool = False
    is_admin: bool = False
    message_count: int = 0
    created_at: datetime | None = None
    last_activity: datetime | None = None


@dataclass
class Message:
    message_id: int
    user_id: int
    text: str
    created_at: datetime | None = None
