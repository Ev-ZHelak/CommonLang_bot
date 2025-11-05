import yaml


def get_telegram_token():
    config = yaml.load(open('config/config.yaml', 'r'), Loader=yaml.SafeLoader)
    if not config.get('telegam_bot', {}).get('token'):
        raise SystemExit("yaml: No token provided")
    return config['telegam_bot']['token']

TG_TOKEN = get_telegram_token()
