import yaml

__all__ = ['get_bot_token', 'get_database_path']

__config = yaml.load(open('config/config.yaml', 'r'), Loader=yaml.SafeLoader)


def get_bot_token():
    if not __config.get('telegam_bot', {}).get('token'):
        raise SystemExit("yaml: No token provided")
    return __config['telegam_bot']['token']


def get_database_path():
    if not __config.get('database', {}).get('path'):
        raise SystemExit("yaml: No database path provided")
    return __config['database']['path']