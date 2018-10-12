from pwn import *

p = remote('34.216.132.109',9093)
a = p.recv(1024)
print(a)
print(a[19],a[22:25],a[45],a[48:51])
payload = a[19]*int(a[22:25]) + a[45]*int(a[48:51]) + str(ord(a[19])+ord(a[45]))
print(payload)
p.sendline(payload)
print(p.recv(1024))
p.interactive()