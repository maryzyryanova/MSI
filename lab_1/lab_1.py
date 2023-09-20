import base64
import struct


def encrypt_text(text: bytes, key: bytes) -> bytes:
    """

    :param text:
    :param key:
    :return:
    """
    encrypted_text: bytes = b''
    gamma_keys = generate_gamma_keys(key)
    text = base64.b64encode(text)
    for i in range(0, len(text), 8):
        block = text[i:i + 8]
        encrypted_text += bytes(x ^ int.from_bytes(y, byteorder='little') for x, y in zip(block, gamma_keys))

    return encrypted_text


def decrypt_text(encrypted_text: bytes, key: bytes) -> str:
    """

    :param encrypted_text:
    :param key:
    :return:
    """
    decrypted_text: bytes = b''
    gamma_keys = generate_gamma_keys(key)

    for i in range(0, len(encrypted_text), 8):
        block = encrypted_text[i:i + 8]
        decrypted_text += bytes(x ^ int.from_bytes(y, byteorder='little') for x, y in zip(block, gamma_keys))
    decrypted_text = base64.b64decode (decrypted_text)
    return decrypted_text.decode("utf-8")


def split_text_into_blocks(text: bytes) -> list[bytes]:
    """
    The method splits text into 64-bit blocks.
    :param text: input string.
    :return: list of 64-bit blocks.
    """
    bits: int = 8
    n: int = len(text)
    blocks: list[bytes] = []
    for i in range(0, n, bits):
        blocks.append(text[i:i+bits])
    return blocks


def generate_gamma_keys(key: bytes) -> list[bytes]:
    """
    The method generates 8-bit gamma keys.
    :param key: encrypt key.
    :return: list of 8-bit gamma keys.
    """
    counter: int = 0
    bits: int = 8
    keys: list[bytes] = []
    for i in range(bits):
        block: int = key[i]
        for j in range(bits):
            bit: int = counter >> (7 - j)
            value: int = bit & 0x01
            block ^= value
            counter += 1
        keys.append(bytes(block))
    return keys
