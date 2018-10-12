#!/usr/bin/env python

import random
from pwn import *

context.log_level = 'critical'

# nc 34.216.132.109 9094

host = '34.216.132.109'
port = 9094

user = 'admin'

s = remote(host, port)
s.recv()
s.sendline(user)
s.recv()

# count_ needs to be bruteforced from 0 to 1000
for count_ in range(1000):


    random.seed('xorshift')

    count = 0
    for ch in user:
            ra = random.randint(1, ord(ch))
            rb = (ord(ch) * random.randint(1, len(user))) ^ random.randint(1, ord(ch))

            count += (ra + rb)/2

    code = 1

    for i in range(1,count+count_):
        code = (code + random.randint(1, i) ) % 1000000

    final = random.randint(1,9) * 1000000 + code
    
    s.sendline(str(final))
    
    prompt = s.recv()
    
    print final, prompt
    if ( 'Incorrect' not in prompt):
        print "Got something new???"
        prompt =  s.recv()
        if ( 'Incorrect' not in prompt):
            # This is an extra test for random hiccups...
            print prompt
            prompt =  s.recv()
            exit()
