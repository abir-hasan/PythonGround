# Web Science Assignment - 3
# Team - Mike
# Task 4 - Python Programming
# 4.1 URL Parser
#
# Write a Python script called as urlparser.py. The script parses an url into the segments
# that are explained in the lecture Internet vs WWW, and additionally extracts top-level
# domains as one segment. When you execute the script
# (e.g python -m urlparser https://west.uni-koblenz.de/studying/ws2021) at the command-line, a dictionary
# containing the url and its segments should be returned. For the optional parts, you may use None values.
# Take a screenshot of the terminal output of your script for the following URLs
#
# 1. https://www.facebook.com/photo.php?fbid=2068026323275211&set=a.269104153167446&
#    type=3&theater
# 2. http://www.blog.google.uk:1000/path/to/myfile.html?key1=value1&key2=value2#
#    InTheDocument
# 3. https://www.overleaf.com/9565720ckjijuhzpbccsd#/347876331/
# 4. ftp://root@west.uni.koblenz.de
# 5. https://west.uni-koblenz.de/studying/ws2021
#
# You are not allowed to use any specific libraries that help in url parsing and regular expressions.

import sys

SCHEME = "scheme"
USER_INFO = "userinfo"  # Optional
HOST = "host"
PORT = "port"  # Optional
PATH = "path"  # Optional
QUERY = "query"  # Optional
FRAGMENT = "fragment"  # Optional
TLD = "tld"  # TOP LEVEL DOMAIN


# Parse an URL to it's segments
def parse_url(url):
    original_url = url
    parsed_segments = {}
    url = find_scheme(parsed_segments, url)  # Find Scheme From URL
    url = find_host(parsed_segments, url)  # Find Host From URL
    url = find_path(parsed_segments, url)  # Find Path From URL
    url = find_query(parsed_segments, url)  # Find Query From URL
    find_fragment(parsed_segments, url)  # Find Fragment From URL

    url_segments = {original_url: parsed_segments}  # Dictionary Containing URL and it's parsed segments
    print(f"\n{url_segments}")
    """print("\nIndividual URL Segments:\n")
    for k, v in parsed_segments.items():
        print(f"{k} : {v}")"""
    return url_segments


def find_fragment(parsed_segments, url):
    fragment = None if url == '' else url
    parsed_segments[FRAGMENT] = fragment


def find_query(parsed_segments, url):
    try:
        query_last_index = url.index("#")
        temp_query = url[:query_last_index]
        if temp_query == '':
            parsed_segments[QUERY] = None
        else:
            parsed_segments[QUERY] = temp_query
        url = url[query_last_index:]
    except ValueError as e:
        url = None if url == '' else url
        parsed_segments[QUERY] = url
        url = ""
    return url


def find_path(parsed_segments, url):
    try:
        path_last_index = url.index("?")
        temp_path = url[:path_last_index]
        parsed_segments[PATH] = temp_path
        url = url[path_last_index:]
    except ValueError as e:
        part = url.split("#")
        if len(part) > 1:
            parsed_segments[PATH] = part[0]
            url = '#' + part[1]
        else:
            if url == '':
                parsed_segments[PATH] = None
            else:
                parsed_segments[PATH] = url
            url = ""
    return url


def find_host(parsed_segments, url):
    try:
        host_last_index = url.index("/")
        temp_host = url[:host_last_index]
        host_parts(parsed_segments, temp_host)
        url = url[host_last_index:]
    except ValueError as e:
        host_parts(parsed_segments, url)
        url = ""
    return url


def host_parts(parse_segments, host):
    part = host.split("@")
    if len(part) > 1:
        parse_segments[USER_INFO] = part[0]
        host = part[1]
    else:
        parse_segments[USER_INFO] = None

    part = host.split(":")
    if len(part) > 1:
        host = part[0]
        parse_segments[PORT] = part[1]
    else:
        parse_segments[PORT] = None
    tld = host.split(".")  # Parsing Top Level Domain in Host
    tld = tld[len(tld) - 1]
    parse_segments[TLD] = tld
    parse_segments[HOST] = host


def find_scheme(parsed_segments, url):
    scheme = url.split("://")
    parsed_segments[SCHEME] = scheme[0]
    url = scheme[1]
    return url


if __name__ == "__main__":
    input_url = ""
    arg_len = len(sys.argv)

    if arg_len > 1:
        # Needs at-least 2 arguments for terminal.
        # first is the script name, second is the URL
        input_url = sys.argv[arg_len - 1]  # Last argument is the URL
    else:
        # Run program through console and take input
        input_url = input()

    # Run Parser
    parse_url(input_url)

    # parse_url("https://www.facebook.com/photo.php?fbid=2068026323275211&set=a.269104153167446&type=3&theater")  # 1
    # parse_url("http://www.blog.google.uk:1000/path/to/myfile.html?key1=value1&key2=value2#InTheDocument")  # 2
    # parse_url("https://www.overleaf.com/9565720ckjijuhzpbccsd#/347876331/")  # 3
    # parse_url("ftp://root@west.uni.koblenz.de")  # 4
    # parse_url("https://west.uni-koblenz.de/studying/ws2021")  # 5
