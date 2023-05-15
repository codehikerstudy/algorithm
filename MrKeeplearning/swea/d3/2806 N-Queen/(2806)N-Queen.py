import sys
sys.stdin = open("input.txt", "r")

"""
참고자료: https://mungto.tistory.com/168
"""


T = int(input())


def diagonal(idx, c):
    """
    대각선을 확인하는 함수
    :param idx: 행
    :param c:
    :return:
    """
    for i in range(idx):
        # python의 abs 함수를 사용해서 절대값을 사용
        # 행과 열의 차이가 같다면
        if idx - i == abs(c - map_list[i]):
            return True
    return False


def dfs(idx):
    """
    N개의 Queen이 각 행마다 모두 하나씩 있다면 N-Queen이 완성된 것이다.
    따라서 넘겨 받은 행이 N과 같아진다면 Queen을 놓는 방법의 수를 나타내는 answer를 1 증가시킨다.
    :param idx: 행
    :return:
    """
    if idx == N:
        global answer
        answer += 1
        return
    for i in range(N):
        # 이미 사용한 열이라면 pass
        if visit[i]:
            continue
        if diagonal(idx, i):
            continue
        visit[i] = 1
        map_list[idx] = i
        dfs(idx + 1)
        visit[i] = 0


for test_case in range(1, T + 1):
    N = int(input())
    map_list = [0 for _ in range(N)]
    visit = [0 for _ in range(N)]
    answer = 0
    dfs(0)
    print(f'#{test_case} {answer}')
