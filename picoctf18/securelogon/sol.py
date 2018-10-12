import requests,base64,codecs
import urllib
import httplib2

http = httplib2.Http()

url = "http://2018shell1.picoctf.com:43731/login"
body = {'user': 'dr3dd', 'password': '123'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))
print(response['set-cookie'])


for i in range(256):
    res = response
    k = codecs.decode(res['set-cookie'][7:-8],'base64')
    s = codecs.encode(k.replace(k[31], chr(i) ),'base64')
    res['set-cookie'] = ("cookie=%s; Path=/"%(s)).replace('\n','')

    headers = {'Cookie': res['set-cookie']}


    url = "http://2018shell1.picoctf.com:43731/flag"
    res, content = http.request(url, 'GET', headers=headers)
    if 'picoCTF' in content:
        print('YES.....................................................')
        print(content)
        print(headers)
    print(i,'.............................NO')