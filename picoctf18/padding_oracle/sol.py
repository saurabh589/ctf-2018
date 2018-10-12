from pwn import *


for i in range(256):
    p = remote('2018shell1.picoctf.com', 24933)
    r = p.recvuntil('What is your cookie?').split('\n')[3][25:].decode('hex')
    a = "This is an IV456\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00%s\xc7j\xfe\xbb=\x02\xb9\x04k'b\xa1\xfc\xda\xa3\xb5#\xd3\x85\xf1G{m\xaa\xc1O\xf2Alg"%(chr(i))
    b = a.encode('hex')
    p.sendline(b)
    r = p.recvall()
    if 'invalid' not in r:
        print(r)
        break
    print('......................................................................No',i  )
    p.close()

def strxor(a,b):
    return ''.join(ord(c)^ord(d) for c,d in zip(a,b))


#p6[16] = '~'+'\r'*13