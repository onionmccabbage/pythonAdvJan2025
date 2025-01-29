import socket
import sys

def client():
    '''This microservice network client will 
    send requests to a server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9876)
    # connect to the server
    client.connect(port_t)
    # send some data to the servr
    # NB every interaction must be byte-encoded
    # check to see if additional sys.argv exist
    # if so, pass them to the server
    if len(sys.argv)>1:
        message = ' '.join(sys.argv[1:])
    else:
        message = 'hello from the client'
    client.send(message.encode()) # we must ensure all comms are compatible
    data = client.recv(1024)
    print(f'Client received {data}')
    client.close()


if __name__ == "__main__":
    # the zeroth system argument varialb is ALWAYS the name of the module
    print(sys.argv[0])
    
    client()