import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"
cookies = {'PHPSESSID': session_id}

params = {
    'id': "Admin"
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
