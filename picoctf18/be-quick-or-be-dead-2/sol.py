

a = "2#\v\257\036.\273\060\"\r\237##\n\257(+\v\243.\025\033\245\071?\r\256*/7\243+$7\242.\025\f\257\"/7\246,9\034\237vr\016\363~,\\\370-"
# print(hex(len(a)))
flag = "picoCTF{"

key1 = [66, 74, 104, 192, 93, 122, 253, 75]
# i =0
# key=[]
# for j in range(4):
#     for c in range(256): 
#         x = int(a[i+4],16)^c
#         if  x==ord(flag[i]):
#             i += 1
#             key.append(c)
#             break

# print(key)

# flg = []
# for i in range(8):
#     flg.append(ord(str(a[i]))^ord(flag[i]))

# print(flg)
yo = ""
for i in range(4):
    print(chr(ord(str(a[i]))^ord(flag[i])))

