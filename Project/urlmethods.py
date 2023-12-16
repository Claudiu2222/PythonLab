from urllib.parse import urlparse, urlunparse,urlencode, parse_qs, urljoin
import idna

def encode_url_to_punycode(url):
    parsed_url = urlparse(url)
    #print(parsed_url)
    hostname = parsed_url.hostname
    #print(hostname)

    if hostname:
        ascii_hostname = idna.encode(hostname).decode('ascii')
        parsed_url = parsed_url._replace(netloc=ascii_hostname)
    return urlunparse(parsed_url)

def encode_url_queries(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    encoded_query = urlencode(query_params,doseq=True)
    return urlunparse(parsed_url._replace(query=encoded_query))

def encode_url(url):
    try:
        url = encode_url_to_punycode(url)
        url = encode_url_queries(url)
        return url
    except:
        print("Error parsing")
        
def get_url_params(url):
    params = url.split('?')
    if len(params) == 1:
        return {}
    query_params = parse_qs(params[1])
    return query_params

def add_params_to_url(url, params):
    parsed_url = urlparse(url.split('?')[0])
    encoded_query = urlencode(params, doseq=True)
    return urlunparse(parsed_url._replace(query=encoded_query))

        
# url = "http://xn--p1ai.xn--p1acf/path?query=ceva2%40%4033+ok+test&t=2"
# url = "http://рф.рус?d=22&c=33,2"
# encoded_url = get_url_params(url)
# print(encoded_url) 
