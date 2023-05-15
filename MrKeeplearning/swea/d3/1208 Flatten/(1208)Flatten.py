import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    answer = 0
    dump = int(input())
    arr = sorted(map(int, input().split()))
    arr_length = len(arr)

    for i in range(dump):
        # 주어진 문제에 따라서 가장 높은 곳의 상자를 가장 낮은 곳으로 옮겨야 하므로
        # 최댓값에서 1을 빼고, 최솟값에서 1을 더한다.
        # 최댓값과 최솟값에 max와 min함수를 사용하지 않고 시작과 끝의 인덱스를 바로 넣어
        # max와 min을 구하기 위한 추가적인 정렬 연산 과정을 줄였다.
        arr[arr_length - 1] -= 1
        arr[0] += 1
        # sorted()를 사용하면 정렬된 새로운 리스트를 반환하기 때문에 sort()로 기존 arr을 정렬한다.
        arr.sort()

    answer = arr[arr_length - 1] - arr[0]

    print(f'#{test_case} {answer}')
