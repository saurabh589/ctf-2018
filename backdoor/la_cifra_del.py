#!/usr/bin/python3

# from secret import m,k,decrypt

# assert len(k) == 54

# def encrypt(m,k):
# 	return ''.join([chr(ord(m[i])*ord(k[i%len(k)]) % 256) for i in xrange(len(m))])

# flag_enc = encrypt(m,k)

# assert m == decrypt(flag_enc,k)
import string
import time
import binascii
import gmpy2
from collections import Counter

enc_flag_hex = "d408e36062955531862d6e11e0214b30a803166077413851ebbde0cf27c7a055825d8b1caba420ea6be0abdd7438a39f9114fd1b557f2ea00ee43395f931a004cba08a432519de031687a0830aa007866ca8e0f7f14214eda6db3220d4082fe0fac5e76f42c7d2cda0fb559068395e60d52df9a0b5040fb0cc176ca069e5609ba0fcc54535d4e08702a024d84d20111c6fcee465569ce037e16f45dbd2203f91b09885bae0bc3da0163134bded11e0fcb819200372028141dc455abde26da5c7a0291620d0df2e464f3a471722cb20b2dec7a15d291e07672025c25b0465f9a5af202136e0fcb81920038a918a3350a43344e00427247d82203478dfe0538930381bfea0e1e9d515ddf05c91d79885ffe0bcb895f9a0596b8736c960b3a0140368bca0f1dcaa0ffec120180e13de205d28132370ec7984e017a0f70dde0cd92055aba07f20d7e3e344a085c85ddb18a0673160c4a8038a6051f14fd4e03679c2e05413bf5e8f6013e0ce15a1261bfea0efb2e0dbacf08849fafbf4a005f8cbaedc4748895cd467fc4b8bde5f6055d660dcc83320104c272576ac4db87caa1633d45e71095870dfdfecb32417f01e7d67bf97f9d1dc163d9a6f37bba1bd4c8dbeb09ebdb2356d79b675e21545"
enc_flag = enc_flag_hex.decode('hex')
arr = []
arr1 = "" 
a =0
fl = ""
for i in range(8):
    arr.append(enc_flag[a:a+54])
    if i==8:
        a += 28
    else:
        a += 54    

for i in range(8):
    arr1 += arr[i][0]

for i in range(1,256,2):
    for c in arr1:
        d = ord(c)*gmpy2.invert(i,256)%256
        if chr(d) in string.printable:
            fl += chr(d)
            m = max(Counter(fl))




print("Max : ", m)   






