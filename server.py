import socket
import threading

class Server():
    def __init__(self,ip,port,name,cnx=1):
        self.ip = ip
        self.port = port 
        self.cnx = cnx
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((self.ip,self.port))
        self.name  = name
        print 'The {} is  Listening on {}:{}'.format(self.name , self.ip, self.port)

    def listen(self):
        while True:
            try:
                self.sock.listen(self.cnx)
                self.client, self.address = self.sock.accept()
                print 'The {} is  connected on {}:{}'.format(self.address[0] , self.ip, self.port)
                self.message = self.client.recv(8192)
            except:
                print("error in openning connection on {}  on port {}".format(self.ip,self.port))


    def run(self):
        self.t = threading.Thread(target=self.listen,name=self.name)
        self.t.start()
    #connect to the other server 
    def connect(self,ipsrv,portsrv):
        try:
            self.con  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.con.connect((ipsrv,portsrv))
            print("connected to {} on port {}".format(ipsrv,portsrv))
        except:
            print ("error in connection to server")

    def close(self):
        self.sock.close()

srvtest = Server('127.0.0.1',1005,"server1",10)
srvtest.run()
srvtest.connect('127.0.0.1',2001)
srvtest.close()