import math

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4,8 ,5, 7]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
SB0 = ['01', '00', '11', '10', '11', '10', '01', '00', '00', '10', '01', '11', '11', '01', '11', '10']
SB1 = ['00', '01', '10', '11', '10', '00', '01', '11', '11', '00', '01', '00', '10', '01', '00', '11']
P4 = [2, 4, 3, 1]
IPI = [4, 1, 3, 5, 7, 2, 8, 6]

key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]

def permutation(inp, type_perm, output_size):
    arr = [0]*output_size
    for i in range(output_size):
        arr[i] = inp[type_perm[i]-1]
    return arr

def split_2(inp):
    sz = len(inp)
    sz = sz//2
    arr1 = inp[:sz]
    arr2 = inp[sz:]
    return arr1,arr2

def shift_bits(inp, val):
    inp = inp[val:] + inp[:val]
    return inp

def join_2(inp1, inp2):
    sz = len(inp1)+len(inp2)
    arr = [0]*sz
    arr[:len(inp1)] = inp1
    arr[len(inp1):] = inp2
    return arr

def xor_bits(inp1, inp2):
    arr = [0]*len(inp1)
    for i in range(len(inp1)):
        arr[i]=inp1[i]^inp2[i]
    return arr

def get_sbox_ind(inp):
    row = inp[0]*2+inp[3]
    col = inp[1]*2+inp[2]

    return row*4+col

def sbox(inp,sbox_type):
    ind = get_sbox_ind(inp)
    arr = [0]*2
    arr[0] = int(sbox_type[ind][0])
    arr[1] = int(sbox_type[ind][1])
    return arr

#Key calculation

key_temp = permutation(key,P10,10)

key_half1, key_half2 = split_2(key_temp)

key_half1 = shift_bits(key_half1,1)
key_half2 = shift_bits(key_half2,1)

key1 = permutation(join_2(key_half1,key_half2),P8,8)

key_half1 = shift_bits(key_half1,2)
key_half2 = shift_bits(key_half2,2)

key2 = permutation(join_2(key_half1,key_half2),P8,8)

print()
print("Key1 is",key1,"and Key2 is",key2)

#Now begins the real deal
# ENCRYPTION
def do_all(inp,key,rnd):
    phase2_1, phase2_2 = split_2(inp)

    phase3 = permutation(phase2_2,EP,8)

    phase4 = xor_bits(phase3,key)

    phase5_1, phase5_2 = split_2(phase4)

    phase6_1 = sbox(phase5_1,SB0)
    phase6_2 = sbox(phase5_2,SB1)

    phase7 = permutation(join_2(phase6_1,phase6_2),P4,4)

    phase8 = xor_bits(phase7,phase2_1)

    if rnd == 1:
        phase9 = join_2(phase2_2,phase8)
    else:
        phase9 = join_2(phase8,phase2_2)

    return phase9

def encrypt(inp):
    phase1 = permutation(inp,IP,8)

    phase9 = do_all(phase1,key1,1)

    nearly_done = do_all(phase9,key2,2)

    fin_enc = permutation(nearly_done,IPI,8)

    return fin_enc

def decrypt(inp):
    phase1 = permutation(inp,IP,8)

    phase9 = do_all(phase1,key2,1)

    nearly_done = do_all(phase9,key1,2)

    fin_text = permutation(nearly_done,IPI,8)

    return fin_text

inp_bits = [0, 1, 1, 0, 1, 1, 0, 1]

print()
print("Plain Text is:",inp_bits)


fin_enc = encrypt(inp_bits)

print()
print("Encrypted value:",fin_enc)

#DECRYPTION

fin_text = decrypt(fin_enc)

print()
print("Plain Text value:",fin_text)
print()
