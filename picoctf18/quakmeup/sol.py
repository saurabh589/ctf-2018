# enc_buf = ['0x11', '0x80', '0x20', '0xE0', '0x22', '0x53', '0x72', '0xA1', '0x01', '0x41', '0x55', '0x20', '0xA0', '0xC0', '0x25', '0xE3', '0x45', '0x20', '0x35', '0x05', '0x70', '0x20'] 
from pwn import *
import string

# def rotl(num, bits):
#     bit = num & (1 << (bits-1))
#     num <<= 1
#     if(bit):
#         num |= 1
#     num &= (2**bits-1)

#     return num

# def rotr(num, bits):
#     num &= (2**bits-1)
#     bit = num & 1
#     num >>= 1
#     if(bit):
#         num |= (1 << (bits-1))

#     return num


# flag = ""
# for d in enc_buf:
#     for c in range(32,128):
#         v = rotl(c,4)
#         x = rotr(v^0x16,8)
#         if x == int(d,16):
#             flag += chr(c)

flag = "picoCTF{qu4ckm3_5c21fc8d}"
count = 40
for i in range(17):
    for j in range(32,128):

        p = process('./main')
        x = flag + chr(j)
        p.sendline(x)
        y = p.recv(1024).split('\n')
        # print(y[1][-2:],y[2][count:count+2])
        if y[1][-2:] == y[2][count:count+2]:
            flag += chr(j)
            count += 3
            p.close()
            break
        p.close()
    print(flag)
print(flag)