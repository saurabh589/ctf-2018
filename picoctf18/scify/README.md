<h2>PicoCTF18 Scify (400 pt)</h2>

In this challange they use AES-ECB mode which we know it is quite vulnerable.

If you dont know how AES-ECB works i would suggest to read about first.
[AES-ECB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_(ECB))

**ECB Encryption && Decryption flow chart**


![alt text](https://github.com/saurabh589/ctf-2018/blob/master/picoctf18/scify/601px-ECB_encryption.svg.png)


![alt text](https://github.com/saurabh589/ctf-2018/blob/master/picoctf18/scify/601px-ECB_decryption.svg.png)


```python
#!/usr/bin/python2 -u
from Crypto.Cipher import AES

agent_code = """flag"""

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )    #block-size = 16
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    return cipher.encrypt(plain).encode('hex')

welcome = "Welcome, Agent 006!"
print welcome

sitrep = raw_input("Please enter your situation report: ")
message = '''Agent,
Greetings. My situation report is as follows:
{0}                                                     #here is our input message
My agent identifying code is: {1}.                      #flag
Down with the Soviets,
006'''.format(sitrep,agent_code)

message = pad(message)
print encrypt( """key""", message )
```
**Lets devide message in blocks of 16**



