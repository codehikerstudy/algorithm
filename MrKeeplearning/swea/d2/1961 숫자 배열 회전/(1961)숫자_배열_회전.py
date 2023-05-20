import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def rotate90(init_arr, N):
    """
    90도 회전시켜주는 함수
    :param init_arr: 입력받은 N x N 배열
    :param N: 배열의 사이즈
    :return: 90도 회전한 배열 arr
    """
    arr = [[0] * N for _ in range(N)]   # N x N 빈 배열 생성
    for i in range(N):
        for j in range(N):
            arr[i][j] = init_arr[N-1-j][i]
    return arr


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    arr90 = rotate90(board, N)
    arr180 = rotate90(arr90, N)
    arr270 = rotate90(arr180, N)

    print(f'#{test_case}')
    for i in range(N):
        print("".join(map(str, arr90[i])), end=" ")
        print("".join(map(str, arr180[i])), end=" ")
        print("".join(map(str, arr270[i])), end=" ")
        print()
