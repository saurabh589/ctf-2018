from base64 import *
(a,b,c,d) = (2,3,4,5)

def F(x):
	return (a*x*x + b*x + c)%d

def G(message):
	n = len(message)
	L = message[0:(n/2)]
	R = message[(n/2):n]

	L = int(L.encode("hex"), 16)
	R = int(R.encode("hex"), 16)

	return (L,R)

def fiestel(L, R):
	rounds = 4
	for i in xrange(rounds):
		(L,R) = (R, L^F(R))

	L = hex(L).replace("0x", "").replace("L", "")
	R = hex(R).replace("0x", "").replace("L", "")

	return R+L


FLAG = "CCCCDDDFAAAABBBB"	# REDACT THIS THING

(L, R) = G(FLAG)
print fiestel(L, R).decode("hex")