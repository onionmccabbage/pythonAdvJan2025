import socket

def client():
    '''This microservice network client will 
    send requests to a server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9876)
    # connect to the server
    client.connect(port_t)
    # send some data to the servr
    message = 'hello from the client'
    client.send(message)


if __name__ == "__main__":
    client()