"""
- 문제명: 위장
- url: https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""
def solution(clothes):
    # 옷 종류 별로 구분
    freqs = {}  # key: 옷의 종류, value: 가짓수 를 가지는 dictionary
    for clothes, type in clothes:
        freqs[type] = freqs.get(type, 0) + 1

    # 특정 종류의 아이템을 입지 않는 경우를 추가하여 모든 경우의 수 계산
    answer = 1
    for type in freqs:
        answer *= (freqs[type] + 1)

    # 아무 종류의 옷을 입지 않는 경우 제외
    return answer - 1