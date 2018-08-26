encrypt=' +0W\x1e\x1e\x08\x1a6\x18\x04\x142\x1c\x1d\x02.\x1d\x1c\x1b*\x0e\x0f\x00\x04'
keyy = "abcdefghijklmnopqrstuvwxy"

print(len(encrypt),len(keyy))

flag = ""
for i in range(25):
    d = ord(keyy[i])^ord(encrypt[i]) 
    flag += chr(d)

print(flag)    