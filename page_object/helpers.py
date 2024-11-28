import random
import string


def generate_random_email(domain="example.com"):
    """
    Генерирует случайный email с указанным доменом.
    :param domain: Домен для email. По умолчанию используется "example.com".
    :return: Случайный email.
    """
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@{domain}"


def generate_random_password(length=12):
    """
    Генерирует случайный пароль, который включает буквы, цифры и спецсимволы.
    :param length: Длина пароля. По умолчанию 12 символов.
    :return: Случайно сгенерированный пароль.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
