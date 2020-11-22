import socket


def start_server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print(f'starting up on  port  {server_address}')
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print(f'connection from {client_address}')

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print(f'received {data}')
                if data:
                    print(f'sending data back to the client {type(data)}')
                    # connection.sendall(bytes("121212", 'utf-8'))
                    connection.sendall(data)
                else:
                    print(f'no more data from {client_address}')
                    break

        finally:
            # Clean up the connection
            print('Server Connection Closed')
            connection.close()
            break


if __name__ == "__main__":
    start_server()
