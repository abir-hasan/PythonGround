# Web Science Assignment - 3
# Team - Mike
# Task 4 - Python Programming
# 4.2 Simple HTTP Web Client
#
# You are asked to write a simple HTTP client (httpclient.py) that takes a URL and is
# able to download that web-page from the World Wide Web and store it on your hard drive
# (in the same directory as your python code is running). The program should also print
# out the complete HTTP header of the response and store the header in a separate file.
# You are allowed to use 1) socket, 2) urlparser.py that you implement for the Question 4.1
# 3) sys for reading input from the command-line.
# Run your code on the following urls. Analyse the responses: (1) what is the response code
# (2) explain briefly why does the website respond with that code?

import socket

from urlparser import *


def make_http_request(url):
    url_segments = parse_url(url)
    parsed_url = url_segments[url]
    scheme = parsed_url['scheme']
    host = parsed_url['host']
    port = parsed_url['port']
    path = parsed_url['path']

    # port = ((443 if scheme == 'https' else 80) if port == None else port)
    port = 80 if port == None else port
    path = '' if path == None else path

    print(f"host [{host}] port [{port}] path [{path}]\n")

    request = f"GET {path}/ HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    request = request.encode('utf-8')

    # TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)

    try:
        sock.connect(server_address)
        sock.sendall(request)
        result = sock.recv(4096)
        while len(result) > 0:
            print(result.decode("utf-8"))
            result = sock.recv(4096)
        sock.close()
    except Exception as e:
        print(e)
        sock.close()


if __name__ == "__main__":
    print("hello")
    make_http_request("https://west.uni-koblenz.de/research/projects")
    # make_http_request("http://example.com")
    # make_http_request("http://example.com/test.html")
