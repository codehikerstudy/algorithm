'''
- 프로그래머스 1844번: 게임 맵 최단거리
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/1844
- 해당 풀이는 bfs를 활용한 풀이이며, 인터넷을 참고하여 풀이하였습니다.
    - 해당 문제를 보면 n과 m은 각각 1 이상 100 이하의 자연수라 하였으며, 이를 통해
        dfs로 접근할 경우 런타임 에러가 날 것이라고 추측됩니다.
'''
from collections import deque
def bfs(maps, x, y):

    # 상하좌우. 이차원 배열임을 고려
    dx = [-1, 1, 0, 0]  # 행, 가로
    dy = [0, 0, -1, 1]  # 열, 세로

    queue = deque()
    queue.append((x, y))    # [0, 0]

    # queue가 빌 때까지 반복
    while queue:
        
        print((x, y), maps)
        
        x, y = queue.popleft()

        # 상하좌우를 확인하며 길을 확인
        # 즉 i = 0 = 상, i = 1 = 하, i = 2 = 좌, i = 3 = 우
        for i in range(0, 4):
            # maps[nx][ny]
            nx = x + dx[i]
            ny = y + dy[i]

            # 만약 상하좌우가 맵을 벗어날 경우 무시
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue

            # 만약 길이 막혀 있을 경우 무시
            if maps[nx][ny] == 0:
                continue

            # 길이 열려 있는 경우
            if maps[nx][ny] == 1:
                # 현재의 길에 있는 값(maps[x][y])과 열려 있는 길(+1)을 더함
                maps[nx][ny] = maps[x][y] + 1
                # (nx, ny), 즉 열려 있는 길을 queue에 저장하여 다음에 확인
                # 즉, 현재 queue에 저장하여 다음에 popleft()를 통해 x,y에 저장한 뒤 길이 있는지 검사
                queue.append((nx, ny))


    # 상대 팀 진영까지의 거리 반환
    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):

    answer = bfs(maps, 0, 0)
    
    if answer == 1: # 만약 상대 팀 진영에 갈 수 없을 경우
        return -1
    else:
        return answer

print(solution([[1, 0, 0], [1, 1, 1], [0, 1, 1]]))