import string
a = open('file1','r').read()
b = open('file2','r').read()
flag  = ""
print(len(a),len(b))
#for i in range(7201):
    
flag = a + b
png = open('a.png','w')
png.write(flag)       
