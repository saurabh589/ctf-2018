#!/usr/bin/python2 -u
from pwn import * 
flag = "picoCTF{"

for j in range(1,14):
    print(".................................................",j)
    p = remote('2018shell1.picoctf.com', 37131)
    p.recvuntil('Please enter your situation report: ')
    my_msg = "A"*11+"B"*(25-j)
    p.sendline(my_msg)
    enc_msg = p.recv(1024).decode('hex')
    p.close()

    for i in range(32,128):
        q = remote('2018shell1.picoctf.com', 37131)
        q.recvuntil('Please enter your situation report: ')
        msg = "A"*11+"B"*(14-j) + flag + chr(i)

        q.sendline(msg)
        y = q.recv(1024).decode('hex')
        q.close()
        if y[80:96] == enc_msg[128:144]:
            print('yes...................................................................................yes')
            flag += chr(i)
            print(flag)
            break

            #picoCTF{@g3nt6_1$_th3_c00l3$t_2432504}
