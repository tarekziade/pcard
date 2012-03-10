# -*- encoding: utf8 -*-
import os
import binascii
from string import ascii_letters, digits
from hashlib import sha256
import base64


SYMBOLS = "☀ ☂ ☎ ☠ ☭ ☮ ☺ ☹ ♔ ♘ ♜ ♥ ♣ ♪ ♻ ⚓ ⚛ ⚖ ★ ☕ ☯ ⚪ ⚫ ⚥ ♂ ♀ ☾ ☞ ☢"
ALLOWED = ascii_letters + digits


def generate_key(size=8):
    return binascii.b2a_hex(os.urandom(size))[:size]


def bin2hex(digest):
    def _char(number):
        return ALLOWED[ord(number) % len(ALLOWED)]

    return ' '.join([_char(c) for c in digest])


def create_card(key=None):
    if key is None:
        key = generate_key()
    lines = []
    for i in range(8):
        hash_ = sha256(key)
        hash_.update(str(i))
        digest = hash_.digest()[:29]
        lines.append(bin2hex(digest))

    return key, lines


def print_card(key, lines):
    res = ['   ' + SYMBOLS]
    for index, line in enumerate(lines):
        res.append('%d. %s' % (index, line))
    res.append('')
    res.append(' ' * 20 + 'KEY: %s' % key)
    return '\n'.join(res)


if __name__ == '__main__':
    key, lines = create_card('plqs9876')
    print print_card(key, lines)
    print print_card(*create_card(key))
