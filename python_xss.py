# Simply Python XSS
# By: Alan Joji
# Created: 19.04.2023
from requests import *

# Functions
def is_python_xss_vulnerable (url) :
    try :
        payload = "<script>alert(XSS)</script>"
        request = post(url + payload)


        if (payload in request.text) :
            print("XSS Vulnerability Found")
            return True
        else :
            print("Secure")
            return False

    except Exception as exception:
        print(exception)


def tester () :
    url = "https://www.yahoo.com/"
    is_python_xss_vulnerable(url)


# Main
if __name__ == "__main__" :
    tester()