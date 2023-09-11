import socket

HOST = "192.168.1.6"  # Server IP address or hostname
PORT = 2024  # Port for the connection

# Input two numbers, a and b, from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
data_to_send = f"{a},{b}".encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data_to_send)
    data = s.recv(1024)

print(f"Results from the server: {data.decode('utf-8')}")
