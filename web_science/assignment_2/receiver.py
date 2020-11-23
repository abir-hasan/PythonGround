# Web Science Assignment - 2
# Team - Mike
# Task 2 - Python Programming
# 2.2 TCP Client Server
# In this task you will simulate the checksum operation. You will write a sender (sender.py)
# and a receiver (receiver.py). The communication between them will be with IPv4 and TCP.
# 1. sender.py generates random messages as shown Table 1. When it gets four segments
#    of messages, it calculates the checksum of a message with the method you will
#    implement for Assignment 2.1 and send them to the receiver.
# 2. The receiver.py performs checksum validation with the method you will implement
#    for Assignment 2.1 and sends the result of the validation to the sender.
# 3. When you execute python receiver.py from the console, you should print out the
#    flow of receiver similarly.
# 4. When you execute python sender.py from the console, you should print out the
#    flow of sender similarly:


import pickle
import socket

from task_2 import *

LOCAL_HOST = "127.0.0.1"
CON_PORT = 10000


def start_server():
    # Creating a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding the socket to the port
    server_address = (LOCAL_HOST, CON_PORT)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Using this to reuse same 'server_address'
    sock.bind(server_address)
    # Listen for incoming connection
    sock.listen(1)

    while True:
        # Wait for a connection
        # print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            in_con = client_address[0]  # Incoming Connection Address
            in_port = client_address[1]  # Incoming Connection Port
            in_server = f"{in_con}:{in_port}"
            print(f'connection from {in_server}')

            # Receive message in small chunks
            while True:
                data = connection.recv(48)
                data = pickle.loads(data)  # Using pickle to get 'list' out of received payload
                messages = data[0:4]  # Getting first 4 elements which are messages
                check_sum = data[4]  # Last element in the list is the checksum
                print(f"Got the following message {messages} and {check_sum} as checksum from the sender")
                is_valid = validate_data(messages, check_sum)  # Validate message against checksum
                if data:
                    if is_valid:
                        check_sum = bin(check_sum)
                        final_message = "Receiver Message : Data is correctly received and checksum is "
                        final_message += get_formatted_bits(check_sum)
                        connection.sendall(bytes(final_message, 'utf-8'))  # Send success message
                    else:
                        final_message = "Corrupted data"
                        connection.sendall(bytes(final_message, 'utf-8'))
                    connection.sendall(bytes("exit", 'utf-8'))  # Sending signal to close client connection
                else:
                    print(f'no more data from {client_address}')
                    break
        finally:
            # Clean up the connection
            connection.close()
            break


if __name__ == "__main__":
    start_server()  # Run receiver.py first to start the server
