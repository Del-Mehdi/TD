import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost',1064))
print ("Connection on {}".format('1064'))
for i in range(300):
    socket.send(u"AAAA\n")


socket.close()