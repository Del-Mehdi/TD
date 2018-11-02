import socket
import threading

class Server:
    def __init__(self,ip,port,name,cnx=1):
        self.ip = ip
        self.port = port 
        self.cnx = cnx
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((self.ip,self.port))
        self.name  = name
        print 'The {} is  Listening on {}:{}'.format(self.name , self.ip, self.port)

    def run(self):
        while True:
            self.sock.listen(self.cnx)
            self.client, self.address = self.sock.accept()
            print 'The {} is  connected on {}:{}'.format(self.address[0] , self.ip, self.port)
            self.message = self.client.recv(1024)
            print(self.message.upper())


    def close(self):
        self.sock.close()

srvtest = Server('127.0.0.1',1064,"server1",10)
srvtest.run()
srvtest.close()