import socket

def vernam_decrypt(cipher, key):
    l1 = []
    l2 = []
    for i in range(len(cipher)):
        l1.append(ord(cipher[i]))
    for i in range(len(key)):
        l2.append(ord(key[i]))

    plain = ""
    for i in range(len(l1)):
        plain = plain + chr(l1[i] ^ l2[i])
    return plain

def start_receiver(host="127.0.0.1", port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[RECEIVER] Listening on {host}:{port} ...")

    conn, addr = server_socket.accept()
    print(f"[RECEIVER] Connected by {addr}")

    data = conn.recv(4096).decode()
    key, cipher_codes = data.split("|", 1)
    cipher = "".join(chr(int(c)) for c in cipher_codes.split(","))

    print(f"[RECEIVER] Received ciphertext (codepoints): {cipher_codes}")
    print(f"[RECEIVER] Key used: {key}")

    if len(key) != len(cipher):
        confirmation = "Error: key length does not match ciphertext length."
        print(f"[RECEIVER] {confirmation}")
    else:
        plaintext = vernam_decrypt(cipher, key)
        print(f"[RECEIVER] Decrypted plaintext: {plaintext}")
        confirmation = f"Receiver decrypted your message as: {plaintext}"
        conn.send(confirmation.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_receiver()
