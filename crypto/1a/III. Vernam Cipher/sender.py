import socket

def start_sender(host="127.0.0.1", port=5000):
    text = input("Enter the plaintext: ")
    key = input("Enter the key value: ")
    if len(key) != len(text):
        print("Error: key must be the same length as the plaintext for a Vernam cipher.")
        return

    l1 = []
    l2 = []
    for i in range(len(text)):
        l1.append(ord(text[i]))
    for i in range(len(key)):
        l2.append(ord(key[i]))

    cipher = ""
    for i in range(len(l1)):
        cipher = cipher + chr(l1[i] ^ l2[i])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"[SENDER] Connected to receiver at {host}:{port}")

    cipher_codes = ",".join(str(ord(c)) for c in cipher)
    message = f"{key}|{cipher_codes}"
    client_socket.send(message.encode())

    reply = client_socket.recv(4096).decode()
    print(f"[SENDER] {reply}")
    client_socket.close()

if __name__ == "__main__":
    start_sender()
