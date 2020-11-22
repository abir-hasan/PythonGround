import pickle
import socket

from task_2 import *

LOCAL_HOST = "127.0.0.1"
CON_PORT = 10000


def start_server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (LOCAL_HOST, CON_PORT)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Using this to reuse same 'server_address'
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        # print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            in_con = client_address[0]
            in_port = client_address[1]
            in_server = f"{in_con}:{in_port}"
            print(f'connection from {in_server}')

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(48)
                data = pickle.loads(data)  # Using pickle to get 'list' out of received payload
                messages = data[0:4]
                check_sum = data[4]
                print(f"Got the following message {messages} and {check_sum} as checksum from the sender")
                is_valid = validate_data(messages, check_sum)  # Validate message against checksum
                if data:
                    if is_valid:
                        check_sum = bin(check_sum)[2:]  # slicing 0b
                        final_message = "Receiver Message : Data is correctly received and checksum is "
                        final_message += check_sum
                        connection.sendall(bytes(final_message, 'utf-8'))  # Send success message
                    else:
                        final_message = "Corrupted data"
                        connection.sendall(bytes(final_message, 'utf-8'))
                    connection.sendall(bytes("exit", 'utf-8'))  # Sending signal to close
                else:
                    print(f'no more data from {client_address}')
                    break
        finally:
            # Clean up the connection
            connection.close()
            break


if __name__ == "__main__":
    start_server()
