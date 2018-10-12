from pwn import *

# p = process('./be-quick-or-be-dead-1')


# # p.recvuntil('Calculating key...')
# print p.recv()

key = 3752393848

def decrypt_flag(key):
    res = 0
    for i in range()