from socket import *
from ssl import *

def get_certificate (hostname) :
    context = create_default_context()

    unsecure_socket = create_connection((hostname, 443))
    secure_socket = context.wrap_socket(unsecure_socket, server_hostname=hostname)

    certificate = secure_socket.getpeercert()
    # print(certificate)

    secure_socket.close()
    unsecure_socket.close()

# Todo: Implement the certificate verification part using requests as well as ssl
def verify_certificate () :
    return None

if __name__ == "__main__" :
    hostname = input("Enter the host name :")
    get_certificate(hostname)

