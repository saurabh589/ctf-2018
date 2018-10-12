#!/usr/bin/env python

import re
h = open('secret.c','r')
lines = h.read().splitlines()  # remove newline char

h.close()

flag = []
for line in lines:
    num =''.join(re.findall(r'\s+', line)).replace('\t','1').replace(' ','0')
    print(num)
    if num:
        try:
            flag.append(chr(int(num,2)))
        except:
            pass

print re.findall(r'CodefestCTF{.*}', ''.join(flag)[::-1])[0]

