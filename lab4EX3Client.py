import socket

def ex3Client():
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 443 ))
    message=("hello server!")
    sock.sendall(message.encode())  
    while True:
        print('receving data')
        data=sock.recv(1024)
        print(data.decode())
        if not data:
            break
    sock.close()
ex3Client()