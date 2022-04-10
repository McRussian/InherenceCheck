from random import choice
from string import ascii_letters


def random_string(size: int) -> str:
    s = ''.join([choice(ascii_letters) for _ in range(size)])
    return s
