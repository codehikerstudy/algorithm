import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    tc = int(input())   # 테스트 케이스 번호
    arr = []            # 100 x 100의 2차원 배열을 담을 공간
    max_sum = 0         # 현재 테스트 케이스에서 가장 큰 값

    # 현재 테스트 케이스의 2차원 배열을 생성
    for i in range(100):
        row_list = list(map(int, input().split()))
        arr.append(row_list)

    # 각 행과 열의 합에서 최대값 찾기
    for i in range(100):
        row_sum, col_sum = 0, 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        max_sum = max(row_sum, col_sum, max_sum)
            
    # 대각선에서 최대값 찾기
    for i in range(100):
        diagonal_down, diagonal_up = 0, 0
        # 우하향 대각선
        diagonal_down += arr[i][i]
        # 우상향 대각선
        diagonal_up += arr[i][99 - i]
    max_sum = max(diagonal_up, diagonal_down, max_sum)

    print(f'#{tc} {max_sum}')
