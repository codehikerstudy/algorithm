import sys
sys.stdin = open("sample_input.txt", "r")
"""
재귀호출을 사용한 풀이
- 현재 인덱스의 값을 더하는 경우
- 현재 인덱스의 값을 더하지 않는 경우
"""


def sum_nums(index, sum):
    global answer
    if index == N:
        return
    temp = sum + nums[index]
    if temp == K:
        answer += 1
    sum_nums(index+1, sum)
    sum_nums(index+1, temp)


T = int(input())    # 테스트 케이스의 수
for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # N: nums의 길이, K: 부분 수열의 합
    nums = sorted(list(map(int, input().split())))
    answer = 0  # 최종적으로 반환해야 하는 경우의 수

    sum_nums(0, 0)

    print(f'#{test_case} {answer}')
