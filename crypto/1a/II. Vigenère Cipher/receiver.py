import socket

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = ""
    j = 0
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            key_shift = ord(key[j % len(key)]) - 65
            plaintext += chr((ord(char) - shift_base - key_shift) % 26 + shift_base)
            j += 1
        else:
            plaintext += char
    return plaintext

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print("Vigenère Receiver listening...")
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024).decode('utf-8')
        key, ciphertext = data.split('|', 1)
        print(f"Received Ciphertext: {ciphertext}")
        print(f"Decrypted Text: {vigenere_decrypt(ciphertext, key)}")
