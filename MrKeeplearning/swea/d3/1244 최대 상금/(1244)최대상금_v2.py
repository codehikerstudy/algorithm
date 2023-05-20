import sys
sys.stdin = open("input.txt", "r")

def dfs(count):
    global max_value

    # 스왑 횟수를 모두 사용한 경우
    if not count:
        tmp = int(''.join(values))
        if tmp > max_value:
            max_value = tmp
        return

    for i in range(length):
        for j in range(i+1, length):
            values[i], values[j] = values[j], values[i]
            temp_key = ''.join(values)
            if visited.get((temp_key, count-1), 1):
                visited[(temp_key, count-1)] = 0
                dfs(count - 1)
            values[i], values[j] = values[j], values[i]


T = int(input())

for test_case in range(1, T + 1):
    max_value = 0
    num, s = input().split()
    values = list(num)
    swap = int(s)
    length = len(values)
    visited = {}
    dfs(swap)

    print(f'#{test_case} {max_value}')
