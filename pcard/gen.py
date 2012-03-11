# -*- encoding: utf8 -*-
import os
import binascii
from string import ascii_letters, digits
from hashlib import sha256
import base64
import getpass
import sys


SYMBOLS = u"☀ ☂ ☎ ☠ ☭ ☮ ☺ ☹ ♔ ♘ ♜ ♥ ♣ ♪ ♻ ⚓ ⚛ ⚖ ★ ☕ ☯ ⚪ ⚫ ⚥ ♂ ♀ ☾ ☞ ☢"
ALLOWED = ascii_letters + digits
_LINES = 10


def generate_key(size=_LINES):
    return binascii.b2a_hex(os.urandom(size))[:size]


def bin2hex(digest):
    def _char(number):
        return ALLOWED[ord(number) % len(ALLOWED)]

    return ' '.join([_char(c) for c in digest])


def create_card(key=None):
    if key is None:
        key = generate_key()
    lines = []
    for i in range(_LINES):
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
    return '\n'.join(res)


def main():
    key = getpass.getpass('Type a key : ')
    key2 = getpass.getpass('Type again : ')
    if key != key2:
        print('key mismatch')
        sys.exit(0)
    key, lines = create_card(key)
    print(print_card(key, lines))


if __name__ == '__main__':
    main()
