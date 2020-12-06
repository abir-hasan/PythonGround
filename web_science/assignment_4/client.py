# Web Science Assignment - 4
# Team - Mike
# Task 3 - Dynamic Web Content
#
# You are provided with simpleapp.zip that contains a simple HTTP web server that we
# have designed for you. It has a simple HTTP registration page (localhost:5000/form)
# that asks you to enter the first name and email ID to register.
# Your task is to write a python script client.py that automates the process of registering.
# The simpleapp.zip contains contacts.txt and alternate_contacts.txt that have the
# different names and email IDs that you need to register automatically through your script.
# In the the template folder, you will find an html form whose actions you need to automate
# through your script. The script should look for error messages if the entry that you are
# trying to register is already in the system or not. If no error message, your entry gets
# stored in the server. The script should save all the responses from the server into lists
# and count the number of successful and unsuccessful attempts to register.
# We give the following code snippet as starting code. When you execute this code, you
# will have a compiled errors because it is incomplete. Please replace "TODO" with your
# codes and implement the methods in the __main__. First you need to run the client
# script for contacts.txt, and then after restarting your server you need to run it for
# alternate_contacts.txt. You should get the following error message from the server:
# sqlite3.Warning: You can only execute one statement at a time.
# Please briefly explain, what we try to achieve here and what could be the fix for preventing
# such message from the server side.

import re
import sys

import matplotlib.pyplot as plt
import requests


def read_file(file_path):
    contact_list = []
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
        temp_list = data.split("\n")

        for item in temp_list:
            contact_name_email = []  # Sublist for name, email pair
            name_email = item.split(",")
            contact_name_email.append(name_email[0].strip())
            contact_name_email.append(name_email[1].strip())
            contact_list.append(contact_name_email)
        # print(data)
        # print(contact_list)
    return contact_list


def register(contact, url):
    name = contact[0]
    email = contact[1]
    params = {'name': name, 'email': email}
    response = requests.post(url, data=params)  # Sending request to server for registration
    return response.status_code, response.text


def parse_response(response):
    result = re.findall('>(.*)</', response)
    message = result[0]  # Server response message
    size = result[1]  # Current DB Entry Size
    # print(f"size: {size} message: {message}")
    return size, message


def plot_timeline(list_sizes, output_file):
    plt.plot(range(1, len(list_sizes) + 1), list_sizes)
    plt.xlabel("Attempt No")
    plt.ylabel("Saved item count in DB")
    plt.title("Registration attempt vs Saved contact count graph")
    plt.savefig(output_file)


def plot_bar(success_count, error_count, output_file):
    plt.close()
    # print(f"{success_count} {error_count}")
    title_list = ["success", "error"]
    title_count = [success_count, error_count]
    plt.bar(title_list, title_count)
    plt.xlabel("Success vs Error")
    plt.ylabel("Attempts count")
    plt.title("Success vs Error Graph")
    plt.savefig(output_file)


if __name__ == '__main__':
    URL = "http://127.0.0.1:5000/form"
    fname = ""
    arg_len = len(sys.argv)
    if arg_len > 1:
        fname = sys.argv[1]
    else:
        # Run program through console and take input
        fname = input()
    contacts = read_file(fname)
    # contacts = read_file("contacts.txt")
    # contacts = read_file("alternate_contacts.txt")
    list_sizes = []
    success_count = 0
    error_count = 0
    for contact in contacts:
        status, text = register(contact=contact, url=URL)
        print(f"Status code from the app {status}")
        print(f"Text is {text}")
        list_size, contains_success_msg = parse_response(text)
        list_sizes.append(list_size)
        if contains_success_msg.find("Success") != -1:
            success_count += 1
        else:
            error_count += 1
    total_request = len(contacts)
    # print(list_sizes)
    assert error_count + success_count == total_request
    plot_timeline(list_sizes, output_file="list_size_timeline.png")
    plot_bar(success_count, error_count, output_file="results.png")
