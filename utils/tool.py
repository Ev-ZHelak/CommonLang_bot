from googletrans import Translator
from os import makedirs


def create_folder(path: str):
    """Создать папку"""
    makedirs('path', exist_ok=True)


def get_flag_lang(lang: str) -> str:
    """Получить флаг языка"""
    LANGUAGE_FLAGS = {
        "en": "🇺🇸", "ru": "🇷🇺", "uk": "🇺🇦", "be": "🇧🇾", "kk": "🇰🇿",
        "de": "🇩🇪", "fr": "🇫🇷", "es": "🇪🇸", "it": "🇮🇹", "pt": "🇵🇹",
        "pl": "🇵🇱", "cs": "🇨🇿", "sk": "🇸🇰", "hu": "🇭🇺", "ro": "🇷🇴",
        "bg": "🇧🇬", "sr": "🇷🇸", "hr": "🇭🇷", "bs": "🇧🇦", "sl": "🇸🇮",
        "mk": "🇲🇰", "sq": "🇦🇱", "el": "🇬🇷", "tr": "🇹🇷", "ar": "🇸🇦",
        "he": "🇮🇱", "fa": "🇮🇷", "hi": "🇮🇳", "bn": "🇧🇩", "ur": "🇵🇰",
        "zh": "🇨🇳", "ja": "🇯🇵", "ko": "🇰🇷", "vi": "🇻🇳", "th": "🇹🇭",
        "id": "🇮🇩", "ms": "🇲🇾", "tl": "🇵🇭", "nl": "🇳🇱", "sv": "🇸🇪",
        "no": "🇳🇴", "da": "🇩🇰", "fi": "🇫🇮", "is": "🇮🇸", "et": "🇪🇪",
        "lv": "🇱🇻", "lt": "🇱🇹", "ka": "🇬🇪", "hy": "🇦🇲", "az": "🇦🇿",
        "uz": "🇺🇿", "tk": "🇹🇲", "tg": "🇹🇯", "ky": "🇰🇬", "mn": "🇲🇳",
        "ne": "🇳🇵", "si": "🇱🇰", "my": "🇲🇲", "km": "🇰🇭", "lo": "🇱🇦",
        "unknown": "🌐"
    }

    if lang in LANGUAGE_FLAGS:
        return LANGUAGE_FLAGS[lang]
    else:
        return LANGUAGE_FLAGS["unknown"]


async def message_translator(text: str, lang: str):
    """Пперевести сообщение"""
    translator = Translator()

    # Асинхронный перевод
    result = await translator.translate(text, dest=lang)
    # print(f"Перевод: {result.text}")
    # print(f"Исходный язык: {result.src}")
    # print(f"Произношение: {result.pronunciation}")

    # Асинхронное определение языка
    detection = await translator.detect(text)
    # print(f"Определен язык: {detection.lang}")

    return f"\n{get_flag_lang(lang)}: {result.text}"
