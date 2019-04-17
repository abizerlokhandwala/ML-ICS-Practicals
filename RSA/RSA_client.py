import socket
import random
import math

client_socket = socket.socket()
client_socket.connect(("localhost",5650))

pube = int(client_socket.recv(1024).decode())

pubn = int(client_socket.recv(1024).decode())

print("Received Public Key is: {",pube,",",pubn,"}")

print("Enter string to send")
s = str(input())

arr = []
enc_str = ""

for i in s:
    arr.append((ord(i)**pube)%pubn)

print("Encrypted String: ",end="")
for i in arr:
    print(i,end="")

print()

client_socket.send(str(arr).encode())
