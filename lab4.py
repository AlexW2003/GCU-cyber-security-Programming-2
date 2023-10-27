#lab 4 working with pyhton sockets

import socket

def ex1():
    print(dir(socket))

def ex2():
    ip ='127.0.0.1'
    portlist=[]
   
    for i in range (0,int(input('how many ports '))):
        portlist.append(int(input('enter a port number ')))
    for port in portlist:
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((ip,port))
        print(port,":", result)
    sock.close()


def testing():
    
    
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #create local interface
    server_address = ('localhost', 8888)
    sock.bind(server_address)
    #connect to server 
    sock.connect(server_address)

    #send data
    message="Hello, server!"
    sock.sendall(message.encode())

    #recive data from server
    data=sock.recv(1024)#1024 rate at which data can be recived bytes/sec
    print(data.decode())
    sock.close()

def ex3():
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address =(('127.0.0.1', 443))
    sock.bind(server_address)
    sock.listen(10)
    while True:
        print('Waiting for connection ')
        (recvSocket,address)=sock.accept()
        print(recvSocket.recv(1024))
        message='You are connected to the server!'
        recvSocket.send(message.encode())
        recvSocket.close()
        sock.close()

ex3()
def ex4():
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 443 ))
    message=("hello server!")
    sock.sendall(message.encode())  
    while True:
        print('receving data')
        data=sock.recv(1024)
        print(data)
        if not data:
            break

def ex5():

    gcuip=socket.gethostbyname("www.gcu.ac.uk")
    cnnip=socket.gethostbyname("www.cnn.com")
    bbcip=socket.gethostbyname("www.bbc.com")

    print(gcuip,cnnip,bbcip)

def ex6():
    hostname=input('enter hostname ')
    ip=socket.gethostbyname(hostname)
    print(hostname, ip)

import sys

def ex7(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: \t Open".format(port))
            else:
                print("Port {}: \t Closed".format(port))
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Connection error")
        sys.exit()

#ex7('localhost', [21, 22, 80, 8080, 443])

  





