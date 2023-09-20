def encrypt_text(text: bytes, key: bytes) -> bytes:
    """

    :param text:
    :param key:
    :return:
    """
    encrypted_text: bytes = b''
    blocks: list[bytes] = split_text_into_blocks(text)
    gamma_keys: list[bytes] = generate_gamma_keys(key)
    for block, key in zip(blocks, gamma_keys):
        encrypted_text += block ^ key
    return encrypted_text


def decrypt_text(encrypted_text: bytes, key: bytes) -> bytes:
    """

    :param encrypted_text:
    :param key:
    :return:
    """
    decrypted_text: bytes = b''
    blocks: list[bytes] = split_text_into_blocks(encrypted_text)
    gamma_keys: list[bytes] = generate_gamma_keys(key)
    for block, key in zip(blocks, gamma_keys):
        decrypted_text += block ^ key
    return decrypted_text


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
