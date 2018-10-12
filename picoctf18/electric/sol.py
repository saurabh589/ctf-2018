from pwn import *
import codecs
p = remote('2018shell1.picoctf.com', 36150)
p.recvuntil('Please choose: ')
p.sendline('i')
x = p.recvuntil('Please choose: ').split('\n')
x = x[2][2:-4].replace('_','A')
p.sendline('n')
p.recvuntil('Name of file? ')
p.sendline(x)
p.recvuntil('Data? ')
p.sendline('aaaa')
y = p.recvuntil('Please choose: ').split('\n')[1]



for i in range(256):
    a = y.decode('base64')
    b = a.replace(a[4],chr(i))
    w = b.encode('base64').replace('\n','')
    p.sendline('e')
    p.recvuntil('Share code? ')
    p.sendline(w)
    z = p.recvuntil('Please choose: ')
    if 'picoCTF' in z:
        print(z,i)
        break
    print(z,i)
p.close()