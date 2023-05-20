import sys
from collections import deque

sys.stdin = open("input.txt", "r")
"""
- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료
- 1사이클 = 5회
"""
T = 10
for test_case in range(1, T + 1):
    tc = input()                            # 테스트 케이스 번호
    pw = deque(map(int, input().split()))   # 암호 배열
    count = 1                               # 현재 값에서 뺄 값

    while True:
        num = pw.popleft() - count
        # count만큼 감소했을 때 0보다 작거나 0일 경우
        # 0으로 저장된다.
        if num < 0:
            num = 0
        pw.append(num)
        # 숫자가 감소하면서 0보다 작아질 경우
        # 프로그램은 종료한다.
        if num <= 0:
            break

        count += 1
        # 1사이클은 5회 감소이다.
        # 1사이클을 모두 돌았다면 count = 1로 초기화한다.
        if count > 5:
            count = 1

    print(f'#{tc} ', end='')
    print(*pw)
