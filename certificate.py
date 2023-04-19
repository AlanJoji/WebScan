from socket import *
from ssl import *
from requests import *


# Functions
def check_url (url) :
    """
    Input:  
        URL of a website 
    Action: 
        Generates a request to the webpage with the get method with the verify set to True
    Output:     
        True for Site with SSL Certificate
        False for Site without SSL Certifcate
    """
    result = False
    try :
        response = get(url, verify = True)
        print(response)

        result = True
        return result

    except error :
        print(error)
        return result


def url_is_safe (url) :
    """
    Input:  
        URL of a website 
    Action: 
        Parent function to check_url
    Output:     
        True for Site with SSL Certificate
        False for Site without SSL Certifcate
    """
    result = check_url(url)
    return result


def check_hostname (context, unsecure_socket) :
    """
    Input:  
        Context for SSL set up using the HTTPS port (443)
        Unsecure Socket which has already been connected to the server
    Action: 
        Wraps a SSL context to the existing unsecure port to check whether the site is secure
    Output:     
        True for Site with SSL Certificate -> Can also produce the SSL Certificate 
        False for Site without SSL Certifcate -> Error is handled when the SSL wrap fails
    """
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
    """
    Input:  
        Hostname of the website
    Action: 
        Creates a context and a unsecure connection
    Output:     
        True for Site with SSL Certificate 
        False for Site without SSL Certifcate 
    """
    context = create_default_context()

    unsecure_socket = create_connection((hostname, 443))    
    result = check_hostname(context, unsecure_socket)

    return result

def tester () :
    hostname = "www.facebook.com"
    hostname_result =  hostname_is_safe(hostname)
    print(hostname_result)
    
    print()

    url = "https://alanjoji.com"
    url_result = url_is_safe(url)
    print(url_result)

    
# Main
if __name__ == "__main__" :
    tester()

