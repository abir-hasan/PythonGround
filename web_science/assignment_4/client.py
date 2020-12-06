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
            contact_name_email = []
            name_email = item.split(",")
            contact_name_email.append(name_email[0].strip())
            contact_name_email.append(name_email[1].strip())
            contact_list.append(contact_name_email)
        print(data)
        print(contact_list)
    return contact_list


def register(contact, url):
    name = contact[0]
    email = contact[1]
    params = {'name': name, 'email': email}
    response = requests.post(url, data=params)
    return response.status_code, response.text


def parse_response(response):
    result = re.findall('>(.*)</', response)
    message = result[0]
    size = result[1]
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
    print(f"{success_count} {error_count}")
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
