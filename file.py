def read_from_file(filename: str) -> bytes:
    """
    The function reads text from file.
    :param filename: name of the input file
    :return: text from file.
    """
    with open(filename, 'rb') as file:
        text: bytes = file.read()
    return text


def write_to_file(filename: str, encrypted_text: str) -> None:
    """

    :param encrypted_text:
    :param filename:
    :return:
    """
    with open(filename, 'w') as file:
        file.write(encrypted_text)
