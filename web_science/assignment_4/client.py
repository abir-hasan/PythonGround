if __name__ == '__main__':
    URL = "TODO"
    contacts = read_file("contacts.txt")
    "TODO"
    for contact in contacts:
        status, text = register(contact=contact, url=URL)
        print(f"Status code from the app {status}")
        print(f"Text is {text}")
        list_size, contains_success_msg = parse_response(text)
        "TODO"
    total_request = len(contacts)
    assert error_count + success_count == total_request
    plot_timeline(list_sizes, output_file="list_size_timeline.png")
    plot_bar(success_count, error_count, output_file="results.png")

