def dfs(computers, visited, start):
    """
    현재 노드에서 연결된 노드를 모두 탐색하는 함수

    visited 리스트는 각 노드가 방문되었는지 여부를 나타냄
    visited 리스트의 각 인덱스는 몇 번 컴퓨터인지를 나타냄
    """
    visited[start] = True
    for i in range(len(computers)):
        # 새롭게 연결할 네트워크가 더 없을 때 자연스럽게 루프를 탈출하고
        # answer의 카운트 값을 올린다.
        if computers[start][i] == 1 and not visited[i]:
            dfs(computers, visited, i)


def solution(n, computers):
    """
    네트워크의 개수를 세는 변수인 answer를 초기화한 뒤
    각 노드를 시작점으로 해서 dfs 탐색을 수행

    방문하지 않은 노드만 dfs 탐색을 수행
    """
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1

    return answer
