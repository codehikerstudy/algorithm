import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# N = int(input())
# test = [list(map(int, list(input()))) for _ in range(N)]
#
# print(N)
# print(test)
# print(5//2)

for test_case in range(1, T + 1):
    N = int(input())    # N x N 사이즈의 농장
    tc_list = [list(map(int, list(input()))) for _ in range(N)]     # 현재 테스트 케이스의 농작물 가치 정보
    answer = 0

    # 한 행씩 내려가면서 농작물의 value를 확인한다.
    # 이 때 start와 end는 한 행에서 농작물의 value를 확인할 범위의 시작점과 끝점이다.
    start, end = N // 2, N // 2
    for i in range(N):
        for j in range(start, end + 1):
            answer += tc_list[i][j]

        # 수확할 수 있는 범위는 정사각형 마름모 형태이므로
        # 중간지점까지는 value를 확인하는 범위(start부터 end까지)가 늘어나지만
        # 중간지점 이후부터는 그 범위가 줄어든다.
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f'#{test_case} {answer}')
