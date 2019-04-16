import socket
import sys
import random
import time

g = random.randint(2,100)

primes = []
primes_bool = [1]*10000

for i in range(2,1000):
    if(primes_bool[i]==1):
        primes.append(i)
        j = 2*i
        while(j<=1000):
            primes_bool[j] = 0
            j+=i
#primes stores all the primes between 2 and 1000

n_index = random.randint(10,len(primes)-1)

n = primes[n_index]

print("Public Generator g:",g)
print("Public Prime n:",n)

HOST = "localhost"
PORT = 12785

server_socket = socket.socket()
server_socket.bind((HOST,PORT))
server_socket.listen(5)
client, address = server_socket.accept()

print ("Connected to:",address)

client.send(str(g).encode())

client.send(str(n).encode())

a = random.randint(2,100)

print("Private number a:",a)

A = (g**a)%n

print("Public key A = g^a:",A)

client.send(str(A).encode())

B = int(client.recv(1024).decode())

print("B's Public key:",B)

AB = (B**a)%n

print("Shared Private Key:",AB)

num = 123 #msg to be encrypted using xor

enc_num = num^AB

print("Encrypted value is:",enc_num)

client.send(str(enc_num).encode())

time.sleep(3) #done so that socket errors are not faced. Server program should always end after the client program
