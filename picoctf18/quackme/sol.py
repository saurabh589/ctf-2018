a = "You have now entered the Duck Web, and you're in for a honkin' good time."
enc = ")\006\026O+50\036Q\033[\024K\b]+\\\020\006\006\030" + "EQ" + "\00" "]"

x = ""
for i in range(25):
     x += chr(ord(a[i]) ^ ord(str(enc[i])))

print(x)

# flag = "picoCTF{qu4ckm3_9bcb819e}"                  