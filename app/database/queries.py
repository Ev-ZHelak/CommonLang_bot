CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    phone_number TEXT,
    language_code TEXT,
    is_premium BOOLEAN DEFAULT FALSE,
    is_admin BOOLEAN DEFAULT FALSE,
    message_count INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_activity DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""