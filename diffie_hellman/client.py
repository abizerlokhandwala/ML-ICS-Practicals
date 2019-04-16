import socket
import sys
import random
import time

HOST = "localhost"
PORT = 12785

client_socket = socket.socket()
client_socket.connect((HOST,PORT))

g = int(client_socket.recv(1024).decode())
print("Received Public Generator g:",g)

n = int(client_socket.recv(1024).decode())
print("Received Public Prime n:",n)


b = random.randint(2,100)

print("Private number b:",b)

B = (g**b)%n

print("Public key B = g^b:",B)

A = int(client_socket.recv(1024).decode())

client_socket.send(str(B).encode())

print("A's Public key:",A)

AB = (A**b)%n

print("Shared Private Key:",AB)

enc_num = int(client_socket.recv(1024).decode())

print("Received Encrypted Value:",enc_num)

num = enc_num^AB

print("Plain text:",num)
