import socket

HOST = "192.168.1.6"  # Server IP address or hostname
PORT = 2024  # Port for the connection

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connection from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            # Decode received data and split it into a and b
            numbers = data.decode('utf-8').split(',')
            if len(numbers) == 2:
                a = int(numbers[0])
                b = int(numbers[1])

                # Calculate a + b, a - b, a * b, and a / b
                add_result = a + b
                subtract_result = a - b
                multiply_result = a * b
                divide_result = a / b if b != 0 else "Division by zero"

                # Send the results back to the client
                result_str = f"Add: {add_result}, Subtract: {subtract_result}, Multiply: {multiply_result}, Divide: {divide_result}"
                conn.sendall(result_str.encode('utf-8'))
