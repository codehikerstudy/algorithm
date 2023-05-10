"""
max와 슬라이싱을 활용한 풀이
"""
import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    apt_height = list(map(int, input().split()))
    answer = 0
    # 처음 시작과 끝 2자리는 제외하고 순회한다.
    for i in range(2, N-2):
        # 아파트 최대 높이
        cur_max_height = max(apt_height[i-2:i] + apt_height[i+1:i+3])
        # 범위 내에서 최대값이 현재 위치의 아파트보다 작다면 그 둘의 차이는
        # 현재 위치 아파트의 조망권이 확보된 층수가 된다.
        if cur_max_height < apt_height[i]:
            answer += (apt_height[i] - cur_max_height)

    print(f'#{test_case} {answer}')
