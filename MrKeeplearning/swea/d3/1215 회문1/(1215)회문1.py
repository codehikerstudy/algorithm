from collections import deque
import sys

sys.stdin = open("input.txt", "r")

T = 10

def is_palindrome(s):
    """
    회문 판별 함수
    :param s:
    :return:
    """
    # palindrome 판별 방법 1
    # l = len(s)
    # for i in range(l // 2):
    #     if s[i] != s[l - i - 1]:
    #         return False
    # return True

    # palindrome 판별 방법 2
    deq = deque(s)
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True


for test_case in range(1, T + 1):
    length = int(input())  # 주어진 회문의 길이
    row_list = []  # 회문을 찾기 위한 행 모음
    col_list = []  # 회문을 찾기 위한 열 모음
    n = 8  # 글자판은 8 x 8 사이즈
    answer = 0

    # 행 모음 리스트 생성
    for i in range(n):
        row_list.append(input())

    # 열 모음 리스트 생성
    for j in range(n):
        temp = ''
        for k in range(n):
            temp += row_list[k][j]
        col_list.append(temp)

    for i in range(n):
        for j in range(n - length + 1):
            # 행 모음 리스트를 대상으로 회문 탐색
            if is_palindrome(row_list[i][j:j + length]):
                answer += 1
            # 열 모음 리스트를 대상으로 회문 탐색
            if is_palindrome(col_list[i][j:j + length]):
                answer += 1

    print(f'#{test_case} {answer}')
