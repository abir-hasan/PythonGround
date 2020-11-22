import pickle
import random
import socket

from task_2 import *

ENCODING = "utf-8"
LOCAL_HOST = "127.0.0.1"
CON_PORT = 10000

X = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
Y = [0b01110110, 0b01100101, 0b00100000, 0b01110111]
Z = [0b01100101, 0b01100010, 0b00100000, 0b01110011]


def start_client():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (LOCAL_HOST, CON_PORT)
    print(f'connected to tmps-{LOCAL_HOST}:{CON_PORT}')
    sock.connect(server_address)

    # Generating four 8-bit values
    message_list = random.sample(range(0, 256), 4)

    check_sum_int = int(calculate_checksum(message_list), 2)
    message_list.append(check_sum_int)
    try:
        # Send Data to Server
        send_data(sock, message_list)
    finally:
        while True:
            ack = sock.recv(300)
            #ack = ack.decode(ENCODING)
            if ack == "exit".encode(ENCODING):
                break
            else:
                print(f"Response from the receiver {ack}")
    # Close Connection
    sock.close()


def send_data(sock, message):
    # Send data
    data = pickle.dumps(message)  # Using pickle to send 'list' as payload
    sock.sendall(data)


if __name__ == "__main__":
    start_client()
