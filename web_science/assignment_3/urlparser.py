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
    url = find_host(parsed_segments, url)
    url = find_path(parsed_segments, url)
    url = find_query(parsed_segments, url)
    find_fragment(parsed_segments, url)

    # print(url)
    print(parsed_segments)
    print(original_url)
    for k, v in parsed_segments.items():
        print(f"{k} : {v}")


def find_fragment(parsed_segments, url):
    fragment = None if url == '' else url
    parsed_segments[FRAGMENT] = fragment


def find_query(parsed_segments, url):
    try:
        query_last_index = url.index("#")
        temp_query = url[:query_last_index]
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
        url = None if url == '' else url
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
    parse_segments[HOST] = host


def find_scheme(parsed_segments, url):
    scheme = url.split("://")
    parsed_segments[SCHEME] = scheme[0]
    url = scheme[1]
    return url


if __name__ == "__main__":
    # parse_url("https://www.facebook.com/photo.php?fbid=2068026323275211&set=a.269104153167446&type=3&theater")  # 1
    # parse_url("http://www.blog.google.uk:1000/path/to/myfile.html?key1=value1&key2=value2#InTheDocument")  # 2
    parse_url("https://www.overleaf.com/9565720ckjijuhzpbccsd#/347876331/")  # 3 TODO - Path/fragment no query
    # parse_url("ftp://root@west.uni.koblenz.de")  # 4
    # parse_url("https://west.uni-koblenz.de/studying/ws2021")  # 5
