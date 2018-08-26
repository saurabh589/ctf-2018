from pwn import *
import time
context.log_level='debug'

p = remote('139.59.30.165', 9100)

print p.recvuntil("(Press Enter)")

p.sendline()
f = ""
out = ""
def play(number, bet):
    p.sendline(str(number))
    p.sendline(str(bet))
    p.recv()

for i in range(1,100000000):
    play(1,10000000)
   
