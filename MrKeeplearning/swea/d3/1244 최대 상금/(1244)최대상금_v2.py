import sys
sys.stdin = open("input.txt", "r")

T = int(input())
answer = 0
visited = []


def dfs(n):
    global answer
    # 최대 스왑 가능한 횟수까지 도달했다면
    # answer를 최대값으로 갱신한다.
    if n == swap:
        answer = max(answer, int("".join(lst)))
        return

    # length개에서 2개를 뽑는 모든 조합
    # 뽑은 인덱스 값을 서로 swap한다.
    for i in range(length-1):
        for j in range(i+1, length):
            lst[i], lst[j] = lst[j], lst[i]     # 스왑

            # 스왑한 결과물이 이전에 나오지 않았다면 DFS탐색을 계속하고
            # 이전에 이미 만났던 결과물이면 넘어간다.
            check = int("".join(lst))*10 + n
            if check not in visited:
                dfs(n+1)
                visited.append(check)

            # 원상 복구를 해야 처음 인덱스 순서를 유지한 상태에서 조합을 구할 수 있다.
            lst[i], lst[j] = lst[j], lst[i]


for test_case in range(1, T + 1):
    nums, s = input().split()
    swap = int(s)
    lst = []
    for num in nums:
        lst.append(num)
    length = len(lst)
    dfs(0)
    print(f'#{test_case} {answer}')
