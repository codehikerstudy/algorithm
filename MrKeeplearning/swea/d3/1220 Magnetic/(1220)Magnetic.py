import sys

sys.stdin = open("input.txt", "r")
"""
- 하나의 세로 줄 덩어리에 N극과 S극이 같이 붙어 있다면 교착상태 1개 인정
- 만약 n,s,s 또는 s,s,n과 같이 같은 극이 이어진다면 그것까지 포함해서 1개 인정
- 다만, n,s,n,s와 같이 서로 다른 극이 모두 붙어있다면 n,s를 기준으로 개수를 나눔 -> 2개
- 1은 N극, 2는 S극  성질을 가지는 자성체
- 테이블의 윗부분에 N극(1), 아래부분에 S극(2)
- 기본적인 아이디어: 현재 인덱스의 값과 다음 인덱스의 값의 차가 -1인 경우 deadlock을 1 증가시킨다.
- 
"""
T = 10


def check_deadlock(column):
    global deadlock
    for elem in range(len(column)-1):
        if column[elem] - column[elem+1] == -1:
            deadlock += 1


for test_case in range(1, T + 1):
    deadlock = 0
    side = int(input())     # 정사각형 테이블의 한 변의 길이
    square = [list(map(int, input().split())) for _ in range(side)]     # 주어진 정사각형 테이블
    for col in range(side):
        lst = []
        for row in range(side):
            # 정사각형 테이블에서 column만 따로 뽑아서 lst에 담는다.
            # 자성체끼리 서로 붙어 교착상태가 되는 것에 관심이 있기 때문에 0은 제외한다.
            if square[row][col] != 0:
                lst.append(square[row][col])

        # lst[i]와 lst[i+1]의 값이 다르고 모두 0이 아닐 때
        # 교착상태에 빠진 구간이라고 볼 수 있다.
        # len(lst) == 1일 경우 IndexError가 발생할 수 있다.
        if len(lst) > 1:
            check_deadlock(lst)

        # 한 칼럼씩 확인하기 때문에
        # 다음 칼럼을 lst에 담기 위해 초기화

    print(f'#{test_case} {deadlock}')
