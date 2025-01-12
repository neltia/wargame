import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php"
cookies = {'PHPSESSID': session_id}

params = {
    'id': "aadmindmin"
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
