'''
- 프로그래머스 43162번 문제: 네트워크
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/43162
- 해당 문제는 인터넷을 참고하여 풀었습니다.
    - 아직 제대로 이해하지 못하여 추후 다시 풀어볼 예정입니다.
'''

# def dfs(n, computers, start, visited):
#     visited[start] = True

#     for i in range(0, n):
#         if visited[i] == False and computers[start][i] == 1:
#             visited = dfs(n, computers, i, visited)
#     return visited

# def solution(n, computers):
#     visited = [False] * n
#     answer = 0

#     for i in range(0, n):
#         if(visited[i] == False):
#             dfs(n, computers, i, visited)
#             answer += 1
#     return answer