import urllib.request, urllib.parse, urllib.error, sys
import ssl

""" 你的 APPID AK SK """
APP_ID = '10033669'
API_KEY = 'FqQdAifvOsvadi5s8QEEHhXB'
SECRET_KEY = 'Y5jChkCNbSEhjdYZ4OjwGODqoMC7MBvY'


# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print(content)