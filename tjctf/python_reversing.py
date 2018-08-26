#import numpy as np

# flag = 'REDACTED'

# np.random.seed(12345)
# arr = np.array([ord(c) for c in flag])

# other = np.random.randint(1,5,(len(flag)))
# print(other)
# arr = np.multiply(arr,other)

# b = [x for x in arr]
# lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
# c = [b[i]^lmao[i] for i,j in enumerate(b)]

# print(c)
# binary_arr = [bin(x)[2:].zfill(8) for x in c]
# print(binary_arr)

# original_output was 1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101

flag_binary = "1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101"
key_mult = [3, 2, 2, 2, 1, 2, 3, 3, 2, 3, 2, 2, 3, 2, 4, 3, 2, 4, 4, 3, 1, 3, 2, 4, 2, 3, 2, 3, 3, 4, 4, 4, 4, 2, 1, 4, 4, 2, 2, 4, 4, 1, 1, 4, 4, 1, 1, 2, 4, 4, 4, 3, 4, 2, 4, 2, 3, 2, 4, 1, 2, 3, 1]
arr = []
count = 0
for i in range(24):
    if (key_mult[i] >= 3):
        arr.append(int(flag_binary[count:count+9],2))
        count += 9
    else:
        arr.append(int(flag_binary[count:count+8],2))
        count +=8

print(arr)

b = [x for x in arr]
lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
c = [b[i]^lmao[i] for i,j in enumerate(b)]

#print(c)
print(key_mult[:24])
#print(other[:24])
d = []
for i in range(len(c)):
    d.append(chr(c[i]/key_mult[i]))

print(''.join(d))    




         ##  flag = tjctf{pYth0n_1s_tr1v14l}
