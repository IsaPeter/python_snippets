from argparse import ArgumentParser
import requests
import sys
from urllib.parse import urlparse, urljoin
import urllib3
urllib3.disable_warnings()

def check_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    while "/" in path:
        path = path[:path.rfind('/')]
        visiturl = urljoin(parsed_url.scheme+"://"+parsed_url.netloc, path)
        response = requests.get(visiturl, verify=False, timeout=10)
        if "index of" in response.text.lower():
            print("[+] Directory Listing! URL: " + visiturl)
        
def read_urls(path):
    with open(path, "r") as f:
        lines = [ l.strip().replace("\n",'') for l in f.readlines()]
    return lines

def read_stdin():
    lines = []
    for line in sys.stdin.buffer:
        try:
            decoded_line = line.decode("utf-8").strip()
        except UnicodeDecodeError:
            decoded_line = line.decode("latin-1", errors="replace").strip()
        lines.append(decoded_line)
    return lines


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="Set the target url")
    parser.add_argument("-iL", dest="input_list", help="Specify an input list")
    parser.add_argument("--stdin", dest="readfrom_stdin", action="store_true", help="Read urls from STDIN")

    return parser.parse_args()

def main():
    args = parse_arguments()
    url = ""
    input_list = []

    if args.url:
        url = args.url
        check_url(url)
            
    
    if args.input_list:
        input_list = args.input_list
        url_list = read_urls(input_list)
        for url in url_list:
            check_url(url)

    if args.readfrom_stdin:
        input_urls = read_stdin()
        for url in input_urls:
            check_url(url)



if __name__ == '__main__':
    main()