import socket

def server():
    '''this microservice will listen for network requests,
    and respond to requests'''
    # we need an instance of a server
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # configure the server
    port_t = ('localhost', 9876)
    server.bind(port_t)
    # we need our server to listen for requests
    server.listen(4) # NB we may include a 'backlog' integer
    print(f'Server is listening on {port_t[0]}:{port_t[1]}')
    # we need a run loop
    while True:
        # for any request, we can unpack the cient object
        (client, addr) = server.accept()
        print(f'Request received from {addr}')
        # read the first few bytes of the client request object
        buf = client.recv(1024) # accept as much or as little as you like
        print(f'Server received {buf}') # NB the buffer contains encoded bytes
        # write logic to handle requests for data
        # e.g. API, Database, File....
        # send something back from the server
        client.send( buf.upper() )
        
        # if the buffer is 'quit' then terminate the server
        if buf == b'quit':
            break

if __name__ == "__main__":
    server()