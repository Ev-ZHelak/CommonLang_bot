import yaml

_config: dict | None = None


def _load_config():
    global _config
    if _config is None:
        with open('config/config.yaml', 'r') as file:
            _config = yaml.load(file, Loader=yaml.SafeLoader)
    return _config


def get_bot_token():
    config = _load_config()
    if not config.get('telegam_bot', {}).get('token'):
        raise SystemExit("yaml: No token provided")
    return config['telegam_bot']['token']


def get_database_path():
    config = _load_config()
    if not config.get('database', {}).get('path'):
        raise SystemExit("yaml: No database path provided")
    return config['database']['path']
