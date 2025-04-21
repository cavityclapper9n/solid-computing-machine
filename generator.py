import string
import random

def generate_password(length=12, use_digits=True, use_special=True):
    characters = list(string.ascii_letters)
    if use_digits:
        characters += list(string.digits)
    if use_special:
        characters += list("!@#$%^&*()-_=+[]{}<>?")

    if not characters:
        raise ValueError("No characters available to generate password.")

    return ''.join(random.choice(characters) for _ in range(length))
