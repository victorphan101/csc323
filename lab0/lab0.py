# This is a sample Python script.
import codecs
from base64 import b64decode
from binascii import hexlify
from collections import Counter
from string import ascii_lowercase, ascii_uppercase, ascii_letters


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def asciiToHex(text):
    asciiText = text.encode()
    return hexlify(asciiText).decode()


def hexToAscii(text):
    return bytes.fromhex(text)


def base64Tohex(text):
    base64 = b64decode(text.encode())
    hex = base64.hex()
    return hex


def hexToBase64(text):
    hex = codecs.decode(text, 'hex')
    base64 = codecs.encode(hex, 'base64');
    return base64.decode()


def xor(text, keyInput):
    result = ""
    key = ""
    if len(keyInput) == len(text):
        key = keyInput
    elif len(keyInput) < len(text):
        while len(key) < len(text):
            # repeat the key
            for c in keyInput:
                key += c
    if len(keyInput) > len(text):
        key = keyInput[0:len(text)]

    for c, n in zip(text, key):
        if c == '0' and n == '0' or c == '1' and n == '1':
            result += '0'
        elif c == '1' and n == '0' or c == '0' and n == '1':
            result += '1'
        else:
            result += c
    return result


def xor_bytes(text, keyInput):
    return bytes(textByte ^ keyByte for textByte, keyByte in zip(text, keyInput))


def getFreq(text, characters):
    counts = Counter()
    for letter in characters:
        counts[letter] += text.count(letter)
    total = sum(counts.values())
    return {letter: counts[letter] / total for letter in characters}


def text_scoring(text, freq_list):
    score = 0.0
    length = len(text)
    for letter, freq_exp in freq_list.items():
        freq_actual = text.count(ord(letter)) / length
        err = abs(freq_exp - freq_actual)
        score += err

    return score


def xor_single(text, freq_list) -> float | None:
    text = hexToAscii(text)
    # format as tuple
    guess = (float('inf'), None)
    for key in range(256):
        complete_key = bytes([key]) * len(text)
        reg_text = xor_bytes(complete_key, text)
        score = text_scoring(reg_text, freq_list)
        curr_guess = (score, reg_text)
        guess = min(guess, curr_guess)

    if guess[1] is None:
        exit("Error within code as no key was found")
    return guess


def xor_single_worse(text, freq_list):
    text = hexToAscii(text)
    # format as tuple
    result = []
    for key in range(256):
        complete_key = bytes([key]) * len(text)
        reg_text = xor_bytes(text, complete_key)
        score = text_scoring(reg_text, freq_list)
        curr_guess = (score, reg_text)
        result.append(curr_guess)

    result.sort()
    return result[:2]


def xor_single_result(freq_list):
    results = []
    text = ''
    with open("Lab0.TaskII.B.txt", 'r') as f:
        for line in f:
            text = line.strip()
            results.append(xor_single(text, freq_list))

    results.sort()
    return results[0][1]


def generate_keys(text):
    length = len(text)
    result_keys = []
    if length % 2 == 0:
        for a in range(256):
            for b in range(256):
                increment = int(length / 2)
                key = (bytes([a]) + bytes([b])) * increment
                result_keys.append(key)
    if length % 3 == 0:
        for a in range(256):
            for b in range(256):
                for c in range(256):
                    increment = int(length / 3)
                    key = (bytes([a]) + bytes([b]) + bytes([c])) * increment
                    result_keys.append(key)
    if length % 4 == 0:
        for a in range(256):
            for b in range(256):
                for c in range(256):
                    for d in range(256):
                        increment = int(length / 4)
                        key = (bytes([a]) + bytes([b]) + bytes([c]) + bytes([d])) * increment
                        result_keys.append(key)
    if length % 5 == 0:
        for a in range(256):
            for b in range(256):
                for c in range(256):
                    for d in range(256):
                        for e in range(256):
                            increment = int(length / 5)
                            key = (bytes([a]) + bytes([b]) + bytes([c]) + bytes([d]) + bytes([e])) * increment
                            result_keys.append(key)
    if length % 6 == 0:
        for a in range(256):
            for b in range(256):
                for c in range(256):
                    for d in range(256):
                        for e in range(256):
                            for f in range(256):
                                increment = int(length / 6)
                                key = (bytes([a]) + bytes([b]) + bytes([c]) + bytes([d]) + bytes([e]) + bytes(
                                    [f])) * increment
                                result_keys.append(key)
    if length % 7 == 0:
        for a in range(256):
            for b in range(256):
                for c in range(256):
                    for d in range(256):
                        for e in range(256):
                            for f in range(256):
                                for g in range(256):
                                    increment = int(length / 7)
                                    key = (bytes([a]) + bytes([b]) + bytes([c]) + bytes([d]) + bytes([e]) + bytes(
                                        [f]) + bytes([g])) * increment
                                    result_keys.append(key)
    if length % 8 == 0:
        for a in range(256):
            for b in range(256):
                for c in range(256):
                    for d in range(256):
                        for e in range(256):
                            for f in range(256):
                                for g in range(256):
                                    for h in range(256):
                                        increment = int(length / 8)
                                        key = (bytes([a]) + bytes([b]) + bytes([c]) + bytes([d]) + bytes([e]) + bytes(
                                            [f]) + bytes([g]) + bytes([h])) * increment
                                        result_keys.append(key)
    if length % 9 == 0:
        for a in range(256):
            for b in range(256):
                for c in range(256):
                    for d in range(256):
                        for e in range(256):
                            for f in range(256):
                                for g in range(256):
                                    for h in range(256):
                                        for i in range(256):
                                            increment = int(length / 9)
                                            key = (bytes([a]) + bytes([b]) + bytes([c]) + bytes([d]) + bytes(
                                                [e]) + bytes([f]) + bytes([g]) + bytes([h]) + bytes([i])) * increment
                                            result_keys.append(key)
    return result_keys


def xor_multi(text, freq_list):
    # format as tuple
    guess = (float('inf'), None)

    key_list = generate_keys(text)
    for key in key_list:
        complete_key = bytes(key)
        reg_text = xor_bytes(complete_key, text)
        score = text_scoring(reg_text, freq_list)
        curr_guess = (score, reg_text)
        guess = min(guess, curr_guess)

    if guess[1] is None:
        exit("Error within code as no key was found")
    return guess


def xor_multi_result(freq_list):
    # freq_key_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)
    # freq_key_list = dict(freq_key_list)
    results = []
    text = ''
    with open("Lab0.TaskII.C.txt", 'r') as f:
        for line in f:
            text = hexToAscii(base64Tohex(line.strip()))
            results.append(xor_multi(text, freq_list))
    return results


def finding_key_possibilities(text, index, result):
    count = 0
    if index == len(text):
        return result
    i = index
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            count += 1
        i += 1
    result.append(count)
    return finding_key_possibilities(text, index + 1, result)


def finding_numbers(text, key_len, index):
    target_chars = []
    while index + key_len < len(text):
        target_chars.append(text[index])
        index += key_len
    target_chars.sort()
    text_freq_list = Counter()
    for letter in target_chars:
        text_freq_list[letter] += text.count(letter)
    total = sum(text_freq_list.values())
    return {letter: text_freq_list[letter] / total for letter in text}


def rotate(l, n):
    return l[n:] + l[:n]


def vigenere_cipher(text, upper_freq_list):
    # deteremine the length of key
    key_possibilities = []
    index = 0
    key_possibilities = finding_key_possibilities(text, 0, key_possibilities)
    # find and add max num
    max_count = 0
    for value in key_possibilities:
        if value > max_count:
            max_count = value
    key_len = 0
    for value in key_possibilities:
        if value == max_count:
            key_len += max_count

    # take chars from ciphertext by incrementing by len(key)
    index = 0
    est_key = ''
    while index < len(text) - key_len:
        text_freq_list = finding_numbers(text, key_len, index)
        text_freq_list = sorted(text_freq_list.items(), key=lambda x: x[1])

        temp_upper_list = []
        temp_text_list = []
        for itemUpper, itemText in upper_freq_list, text_freq_list:
            if itemText.contains(itemUpper.key):
                temp_upper_list.append(itemUpper.value)
                temp_text_list.append(itemText.value)

        sum = 0
        score = 0
        curr_key = 0
        line_position = 0
        for i in range(len(temp_upper_list)):
            for num1, num2 in temp_upper_list, temp_text_list:
                sum = num1 + num2
            if sum > score:
                score = sum
                curr_key = line_position
            temp_text_list = rotate(temp_text_list, 1)

        est_key += bytes([curr_key + 65])
        index += key_len

    # key found, now cipher
    decryption = ''
    index = 0

    for char in text:
        if char in ascii_uppercase:
            offset = ord(est_key[index]) - ord('A')
            positive_offset = 90 - offset

            decrypted_char = chr((ord(char) - ord('A') + positive_offset) & 26 + ord('A'))

            decryption = decryption + decrypted_char
            index = (index + 1) % len(est_key)


def vigenere_cipher_result(freq_list):
    results = []
    text = ''
    with open("Lab0.TaskII.D.txt", 'r') as f:
        for line in f:
            text = line.strip()
            print(results.append(vigenere_cipher(text, freq_list)))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script
    # ascii to hex
    asciii = 'abc123'
    print(asciiToHex(asciii))

    # hex to ascii
    hex = "616263313233"
    print(hexToAscii(hex))

    # base64 to hex
    base64Text = "fh6X"
    print(base64Tohex(base64Text))

    # hex to base64
    hexText = "7e1e97"
    print(hexToBase64(hexText))

    #  XOR
    print(xor("0b01000001", "0b01000010"))

    # vigenere cipher
    # with open("book_ref.txt", 'r') as f:
    #     ref_text = f.read()
    # upper_freq_list = getFreq(ref_text, ascii_uppercase)
    # print(vigenere_cipher_result(upper_freq_list))

    ref_text = ''
    with open("book_ref.txt", 'r') as f:
        ref_text = f.read()
    freq_list = getFreq(ref_text, ascii_lowercase)
    # single xor
    print(xor_single_result(freq_list))

    # multi xor
    # print(xor_multi_result(freq_list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
