import socket 

target_host = '0.0.0.0'#'www.google.com'
target_port = 8888# 80

# creat socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host, target_port))

# send data
#client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send(b'Phuong Nam')

# receive data
response = client.recv(4096)
print(response)