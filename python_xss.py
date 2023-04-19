# Simply Python XSS
# By: Alan Joji
# Created: 19.04.2023
from requests import *

# Functions
def is_python_xss_vulnerable (url) :
    payload = "<script>alert(XSS)</script>"
    request = post(url + payload)


    if (payload in request.text) :
        print("XSS Vulnerability Found")
    else :
        print("Secure")


def tester () :
    url = "https://example.com/"
    is_python_xss_vulnerable(url)


# Main
if __name__ == "__main__" :
    tester()