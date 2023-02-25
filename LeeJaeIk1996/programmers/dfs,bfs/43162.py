'''
- 프로그래머스 43162번 문제: 네트워크
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/43162
- 해당 문제는 인터넷을 참고하여 풀었습니다.
    - 문제 풀이는 dfs를 활용하여 풀이하였습니다.
'''
def dfs(x, computers, visited): # x = 노드 번호, 
    visited[x] = True   # 방문 처리
    for index, value in enumerate(computers[x]):    # x번 노드에 연결된 행렬을 순회
        if value == 1 and (not visited[index]):     # 값이 1이고 해당 인덱스를 방문하지 않았을 경우(즉, visited가 False)
            dfs(index, computers, visited)          # 즉, 연결은 되어있으나 방문하지 않았을 경우 연결되어 있는 노드에 대해 방문 처리

def solution(n, computers):
    visited = [False] * n   # visited = [False, False, ...], 방문하지 않았을 경우 False
    cnt = 0     # 네트워크의 개수 초기화

    for i in range(n):  # 컴퓨터의 개수만큼 순회
        if not visited[i]:   # i번째 노드를 아직까지 방문하지 않았다면(즉, visited의 해당 인덱스가 아직 False라면)
            dfs(i, computers, visited)  # 이와 연결된(i번째 노드) 모든 노드에 대해 방문 처리하는 dfs 생성
            cnt += 1    # dfs가 실행되었다는 것 자체가 네트워크가 생성되었다는 것을 의미한다.

    return cnt