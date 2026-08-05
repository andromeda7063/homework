import socket

def caesar_encrypt(plaintext, shift):
    shift = int(shift)
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            ciphertext += char
    return ciphertext

host = '127.0.0.1'
port = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    plaintext = input("Enter plaintext: ")
    key = input("Enter shift key (integer): ")
    ciphertext = caesar_encrypt(plaintext, key)
    print(f"Sending Ciphertext: {ciphertext}")
    s.sendall(f"{key}|{ciphertext}".encode('utf-8'))
