import requests
import re


url = 'http://34.216.132.109:8083'
page = '/fp/'
s = requests.Session()


counter = 1
while ( 1 ):
    r = s.get(url + page)

    prompt = r.text
    print prompt

    page = re.findall('action="(.*?)"', prompt)[0]
    print page, counter
    counter += 1
