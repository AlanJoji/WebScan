from socket import *
from ssl import *
from requests import *


# Functions
def check_url (url) :
    result = False
    try :
        response = get(url)
        print(response)

        result = True
        return result

    except error :
        print(error)
        return result


def url_is_safe (url) :
    result = check_url(url)
    return result


def check_hostname (context, unsecure_socket) :
    result = False
    try :
        secure_socket = context.wrap_socket(unsecure_socket, server_hostname = hostname)

        certificate = secure_socket.getpeercert()

        for element in certificate :
            print(element.upper(), ": ", certificate[element])
            print()

        secure_socket.close()
        unsecure_socket.close()

        result = True
        return True

    except SSLCertVerificationError :
        print(error)

        return result

def hostname_is_safe (hostname) :
    context = create_default_context()

    unsecure_socket = create_connection((hostname, 443))    
    result = check_hostname(context, unsecure_socket)

    return result

# Main
if __name__ == "__main__" :
    hostname = "www.facebook.com"
    hostname_result =  hostname_is_safe(hostname)
    print(hostname_result)
    
    print()

    url = "https://alanjoji.com"
    url_result = url_is_safe(url)
    print(url_result)


