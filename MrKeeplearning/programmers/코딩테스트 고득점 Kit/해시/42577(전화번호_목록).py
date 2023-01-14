"""
- 문제명: 전화번호 목록
- url: https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""
def solution(phone_book):
    # 전화번호를 오름차순으로 정렬
    phone_book.sort()

    # sort한 전화번호를 비교한다.
    # sort를 했기 때문에 현재 번호는 다음 번호와만 비교하면 된다.
    # -1은 인덱스가 범위 바깥으로 나갔을 때 발생하는 에러를 해결하기 위함이다.
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
