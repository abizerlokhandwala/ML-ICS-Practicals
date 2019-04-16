import random
import math

a = 0
b = 7
p = 199
#Assuming curve as y^2 = x^3 + ax + b => y^2 = x^3 + 7

x = 0
while True:
    ysq = (x**3 + 7)%p
    y = int(math.sqrt(ysq))
    if y*y == (x**3 + 7)%p:
        break
    else:
        x+=1

g = [x,y]
a = random.randint(1,1000)
b = random.randint(1,1000)

Pa = [a*x, a*y]
Pb = [b*x, b*y]

print("Public key A:",Pa)
print("Public key B:",Pb)

plain_text = int(input("Enter any integer: ")) #smaller than p

k = b*(Pa[0]+Pa[1])
#k = a*(Pb[0]+Pb[1]) happens on A's side

cipher_text = [(k*(g[0]+g[1]))%p,(plain_text+k*(Pa[0]+Pa[1]))%p]    #B uses A's public key to encrypt

print("Encrypted Text:",cipher_text)

decrypted_text = (cipher_text[1]-cipher_text[0]*a+p)%p  #A uses it's private key to decrypt

print("Decrypted Text:",decrypted_text)
