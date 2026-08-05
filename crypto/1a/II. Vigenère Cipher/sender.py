import socket

def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext = ""
    j = 0
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            key_shift = ord(key[j % len(key)]) - 65
            ciphertext += chr((ord(char) - shift_base + key_shift) % 26 + shift_base)
            j += 1
        else:
            ciphertext += char
    return ciphertext

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    plaintext = input("Enter plaintext: ")
    key = input("Enter string key: ")
    ciphertext = vigenere_encrypt(plaintext, key)
    print(f"Sending Ciphertext: {ciphertext}")
    s.sendall(f"{key}|{ciphertext}".encode('utf-8'))
