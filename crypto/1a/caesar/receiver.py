import socket

def caesar_decrypt(ciphertext, shift):
    shift = int(shift)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            plaintext += char
    return plaintext

host = '127.0.0.1'
port = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print("Caesar Receiver listening...")
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024).decode('utf-8')
        key, ciphertext = data.split('|', 1)
        print(f"Received Ciphertext: {ciphertext}")
        print(f"Decrypted Text: {caesar_decrypt(ciphertext, key)}")
