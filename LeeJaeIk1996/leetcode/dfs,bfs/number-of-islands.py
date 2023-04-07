'''
- 리트코드 200번 문제: number of islands
- 문제 출처: https://leetcode.com/problems/number-of-islands/
'''

'''
- 해당 문제 풀이는 인터넷을 참고하였으며 dfs의 재귀를 활용하여 풀이하였습니다.
- 자료 출처: https://firsteast.tistory.com/63
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, i, j):    # i: 행, j: 열
            # 종료 조건 (범위를 벗어나거나 육지가 아닌 경우)
            if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or grid[i][j] == "0":
                return
            
            # 방문 처리. 현재 육지(1)를 물(0)로 바꿔서 다시 방문하지 못하도록 한다.
            grid[i][j] = "0"

            # 상하좌우 재귀
            dfs(grid, i-1, j)   # 상
            dfs(grid, i+1, j)   # 하
            dfs(grid, i, j-1)   # 좌
            dfs(grid, i, j+1)   # 우

        # 예외 처리
        if not grid:
            return 0
        
        cnt = 0 # 방문 횟수
        
        # 이중 반복문을 통해 모든 칸을 확인한다.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 육지(1)일 경우 방문
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    cnt += 1    # 방문 횟수 + 1

        return cnt


'''
- 해당 문제 풀이는 인터넷을 참고하였으며, bfs의 queue를 활용하여 풀이하였습니다.
'''
from typing import List
from collections import deque

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:

        a = len(grid)
        b = len(grid[0])
        
        cnt = 0
        visited = [[False] * b for _ in range(a)]
        queue = deque()

        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(a):
            for j in range(b):

                # 땅이 아니라면 무시
                if grid[i][j] == "0":
                    continue

                # 방문했다면 무시
                if visited[i][j] == True:
                    continue
                
                queue.append((i, j))
                visited[i][j] = True
                cnt += 1

                while queue:

                    x, y = queue.popleft()

                    # 상하좌우
                    for k in range(0, 4):
                        
                        # 현재 위치에서의 상하좌우
                        nx = x + dx[k]
                        ny = y + dy[k]

                        # 만약 map을 벗어날 경우 무시
                        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                            continue

                        # 만약 방문했을 경우 무시
                        if visited[nx][ny] == True:
                            continue

                        # 만약 상하좌우가 0인 경우 무시
                        if grid[nx][ny] == "0":
                            continue

                        visited[nx][ny] = True
                        queue.append((nx, ny))

        return cnt
