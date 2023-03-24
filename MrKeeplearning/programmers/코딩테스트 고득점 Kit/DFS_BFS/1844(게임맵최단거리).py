from collections import deque

def solution(maps):
    """
    1. 대부분의 DFS, BFS 문제들이 그러하듯 visited 배열을 따로 두어 다음 노드로 이동했을 때 해당 노드가
       방문을 한 상태인지 아닌지 확인한다. 또한 n과 m이라는 변수를 두어 각각 세로와 가로 길이를 초기화한다.
    2. directions는 각각 오른쪽, 왼쪽, 위, 아래 4개의 방향으로 1칸씩 움직이는 것을 나타낸다.
       3x3 크기의 좌표가 있다고 생각했을 때 가장 최상단 좌측 첫 번째 좌표가 (0, 0)이라고 생각해보자.
       이 때, 가운데의 좌표는 (1, 1)이 된다. 이 위치에서 오른쪽으로 이동을 했을 때 좌표는 (2, 1)이 된다.
       이것은 directions의 요소 중 (1,0)의 값을 (1,1)에 더한 것과 같이 생각해볼 수 있다.
    3. BFS 탐색의 시작점으로 (0, 0, 1)을 큐에 삽입하고 해당 위치를 방문한 것으로 처리해둔다.
    4. queue에서 popleft로 값을 추출하여 최종도착지에 도착을 했는지 확인하고 도착을 했다면 거리를 반환한다.
       그렇지 못한 경우, 상하좌우 전 방향으로 탐색을 시도하고 아직 방문하지 않은 노드를 queue에 넣으면서
       현재까지의 거리를 업데이트한다.
    """
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # 오른쪽, 왼쪽, 위, 아래 1칸씩 이동
    queue = deque([(0, 0, 1)])  # x, y, 거리
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 최종 도착지에 도달하면 현재까지의 거리를 반환
        if x == n - 1 and y == m - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # nx와 ny가 최대 범위 내에 있는지
            # 0이 아닌 1인 노드가 맞는지
            # 아직 방문하지 않은 노드인지 확인한다.
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    
    return -1   # 예외처리(도달하지 못한 경우)