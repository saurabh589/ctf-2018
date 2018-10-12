#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from pwn import *

#import user_functions
def user(usr_name):
    user = raw_input("Enter your name: ")


        # generate a code

    count_ = random.randint(1,1000)	#User ID/ UID in the table is always positive

    generator = "xorshift"
    random.seed(generator)
    count = 0

    for ch in user:
        ra = random.randint(1, ord(ch))
        rb = (ord(ch) * random.randint(1, len(user))) ^ random.randint(1, ord(ch))

        count += (ra + rb)/2


    code = 1

    for i in range(1,count+count_):
        code = (code + random.randint(1, i) ) % 1000000

    final = random.randint(1,9) * 1000000 + code

    #store it in the database
    return final



p = remote('34.216.132.109' ,9094)
p.recvuntil("name: ")
payld = "aaa"
p.sendline(payld)
p.recvuntil("code: ")
a = str(user('aaa'))
print(a)
p.send(a)
p.recv(1024)
p.interactive()    

# else
# 	#if user already exists, fetch access code
# 	final = user_functions.get_code(user)

# code = raw_input("Enter your access code: ").strip()


# while True:
	
# 	if code.isdigit():
# 		if (int(code) == final):
# 			print "The flag is " + user_functions.get_flag(user)
# 			exit()
# 		else:
# 			print "Incorrect access code"
# 	else:
# 		print "The code must be an integer"

# 	code = (raw_input("\nPlease enter the code: "))

# 	print "\n###############################################"