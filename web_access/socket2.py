import socket

# Create a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (domain, port)
mysock.connect(('data.pr4e.org', 80))

# Proper HTTP request (VERY important format)
cmd = 'GET /intro-short.txtHTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'
mysock.send(cmd.encode())

# Receive data from server
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
