# This is a sample Python script.
import base64
import sys
from binascii import hexlify, unhexlify

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def pad_text(plaintext):
    return plaintext + bytes(16 - len(plaintext) % 16) * (16 - len(plaintext) % 16)


def unpad_text(ciphertext):
    return ciphertext[:-ciphertext[-1]]


def ecb_encrypt(key, plaintext):
    # pad
    text = pad(plaintext)
    # encrypt using AES-128
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = cipher.encrypt(text)
    return cipher_text


def ecb_decrypt(key, ciphertext):
    decipher = AES.new(key, AES.MODE_ECB)
    plaintext = decipher.decrypt(ciphertext)
    return plaintext


def cbc_encrypt(key, plaintext, IV):
    # pad
    text = pad(plaintext)
    # encrypt using AES-128
    cipher = AES.new(key, AES.MODE_CBC, IV)
    cipher_text = cipher.encrypt(text)
    return cipher_text


def cbc_decrypt(key, ciphertext, IV):
    decipher = AES.new(key, AES.MODE_CBC, IV)
    plaintext = decipher.decrypt(ciphertext)
    return plaintext


def ecb_test(single_line_text):
    # ecb mode test
    # print(single_line_text)
    single_line_text = base64.b64decode(single_line_text)
    key = "CALIFORNIA LOVE!"

    actual_message = ecb_decrypt(key.encode('utf-8'), single_line_text)
    print(unpad(actual_message, 32).decode("utf-8"))


def cbc_test(single_line_text):
    # cbc mode test
    single_line_text = base64.b64decode(single_line_text)
    key = "MIND ON MY MONEY"
    IV = "MONEY ON MY MIND"

    actual_message = cbc_decrypt(key.encode('utf-8'), single_line_text, IV.encode('utf-8'))
    print(unpad(actual_message, 32)[16:].decode('utf-8'))


def main():
    """
    KEY = sha256(passphrase).digest()  # returns 256 bit key
    cipher = AES.new(KEY, AES.MODE_ECB)  # creates a AES-256 instance using ECB mode
    ciphertext = cipher.encrypt(pad(data)).encode('base64')
    """
    filename = sys.argv[1]
    file = open(filename)
    single_line_text = ""
    for i in file.read():
        single_line_text += i
    array_text = []
    for line in file:
        array_text.append(line)

    # pad and unpad tests

    # ecb mode test
    ecb_test(single_line_text)

    #cbc test
    # cbc_test(single_line_text)


"""
    # identify ecb mode test
    decode_list = []
    for text in array_text:
        base64.b64decode(text)
        ecb_text = ecb_decrypt("CALIFORNIA_LOVE", single_line_text)
        actual_message = unpad(ecb_text)
        decode_list.append(actual_message)

    # cbc mode test
    print(single_line_text)
    base64.b64decode(single_line_text)
    cbc_text = cbc_decrypt("MIND ON MY MONEY", single_line_text, "MONEY ON MY MIND")
    actual_message = unpad(cbc_text)
    print(actual_message)

    # identify cbc mode test
    decode_list = []
    for text in array_text:
        base64.b64decode(text)
        cbc_text = cbc_decrypt("MIND ON MY MONEY", single_line_text, "MONEY ON MY MIND")
        actual_message = unpad(cbc_text)
        decode_list.append(actual_message)

"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
