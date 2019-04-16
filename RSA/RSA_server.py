import socket
import random
import math
import time
import ast

primes = []
is_prime = [1]*101

for i in range(2,100):
    if(is_prime[i]==1):
        primes.append(i)
        ind = 2*i
        while ind<=100:
            is_prime[ind] = 0
            ind+=i

p = primes[random.randint(4,len(primes)-1)]
q = primes[random.randint(4,len(primes)-1)]

while p==q:
    q = primes[random.randint(4,len(primes)-1)] #p and q cannot be equal

n = p*q

phin = (p-1)*(q-1)

print("Secret Primes are:",p,q)

print("Mod value n is:",n)

print("Totient function value of n is:",phin)

while True:
    e = random.randint(2,phin-1)
    if math.gcd(e,phin) == 1:
        break

print("Public Key is: {",e,",",n,"}")

d = 2

while True:
    if((e*d)%phin!=1):
        d+=1
    else:
        break

print("Private Key is: {",d,",",n,"}")

server_socket = socket.socket()
server_socket.bind(("localhost",5650))
server_socket.listen(5)
client, address = server_socket.accept()

print("Connected to ",address)

client.send(str(e).encode())
time.sleep(1)
client.send(str(n).encode())

arr = client.recv(1024).decode()

arr = ast.literal_eval(arr)

print("Received Encrypted String: ",end="")
for i in arr:
    print(i,end="")

print()

s = ""

for i in arr:
    c = (i**d)%n
    s+=str(chr(c))

print("Plain Text:",s)

time.sleep(3)
