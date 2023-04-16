from typing import List


class Solution:
    """
    교재를 참고한 풀이
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # 예외 처리
        if not grid:
            return 0

        count = 0

        def dfs(i: int, j: int):
            # 더 이상 땅이 아닌 경우 종료
            # len(grid): 세로 길이
            # len(grid[0]): 가로 길이
            # 인덱스는 0부터 시작,
            # 땅에 해당될 경우 이미 방문한 것을 표시하기 위해서 2로 바꿔준다.
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != "1":
                return
            grid[i][j] = "2"

            # 동서남북 탐색
            dfs(i, j + 1)  # 동
            dfs(i, j - 1)  # 서
            dfs(i + 1, j)  # 남
            dfs(i - 1, j)  # 북

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # 처음 육지를 만난 순간 바로 dfs 탐색을 통해서 연결된 모든 1을 탐색한다.
                    # 탐색이 완료되면 dfs함수를 탈출하게 되는데
                    # 이 때 count값을 1 증가시켜 섬의 개수를 기록한다.
                    dfs(i, j)
                    count += 1
        return count
