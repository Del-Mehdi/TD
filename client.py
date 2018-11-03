import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost',1001))
print ("Connection on {}".format('1064'))
socket.send("transaction")


socket.close()