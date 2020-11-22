import socket


def start_client():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print(f'connecting to port {server_address}')
    sock.connect(server_address)

    try:

        # Send data
        message = "1234567890123456"
        print(f'sending  {message}')
        sock.sendall(bytes(message, 'utf-8'))

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f'received {data}')

    finally:
        print('Client connection closed')
        sock.close()


if __name__ == "__main__":
    start_client()
