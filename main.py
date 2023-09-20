from file import (
    read_from_file,
    write_to_file
)
from lab_1.lab_1 import (
    encrypt_text,
    decrypt_text
)


def main():
    key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef'
    result = ""
    input_filename = 'lab_1/input.txt'
    output_filename = 'lab_1/output.txt'
    text = read_from_file(input_filename)
    encrypted_text = encrypt_text(text, key)
    result += f"Encrypted: {encrypted_text}\n"
    decrypted_text = decrypt_text(encrypted_text, key)
    result += f"Decrypted: {decrypted_text}"
    write_to_file(output_filename, result)


if __name__ == "__main__":
    main()