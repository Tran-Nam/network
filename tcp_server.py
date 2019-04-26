import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print('[*] Listen on %s: %d'%(bind_ip, bind_port))

# client handling thread
def handle_client(client_socket):

    # what client send
    request = client_socket.recv(1024)

    print('[*] Received: %s'%request)

    # send back a packet
    a = str(input()).encode('utf-8')
    client_socket.send(a)
    client_socket.send(b'ACK!')
    client_socket.close()

while True:
    client, addr = server.accept()

    print('[*] Accept connect from %s: %d'%(addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handle = threading.Thread(target=handle_client, args=(client, ))
    client_handle.start()