'''
- 프로그래머스 87694번: 아이템 줍기
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/87694
- 해당 풀이는 인터넷을 참고하여 풀이하였습니다.
'''
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 직사각형을 나타내는 모든 좌표 값은 1 이상 50 이하. 
    # 필드를 두 배로 늘릴 것이기 때문에 최대 101이라 볼 수 있다.
    field = [[0] * 101 for i in range(101)]

    cX = 2 * characterX # 2배로 늘림
    cY = 2 * characterY # 2배로 늘림
    iX = 2 * itemX      # 2배로 늘림
    iY = 2 * itemY      # 2배로 늘림

    # 상하좌우
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    visited = [[0] * 101 for i in range(101)]
    visited[cX][cY] = 1 # 현재 위치. 현재 위치를 0에서 1로 변경

    queue = deque([(cX, cY)])

    # 사각형 1로 채움
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2, x2*2 + 1):
            for j in range(y1*2, y2*2 + 1):
                field[i][j] = 1


    # 사각형 테두리 0으로 채움
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2 + 1, x2*2):
            for j in range(y1*2 + 1, y2*2):
                field[i][j] = 0

    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 만약 현재 위치와 도착 지점이 같을 경우 종료
        if (x, y) == (iX, iY):
            answer = (field[x][y] - 1) // 2 # 2배를 하였기 때문에 다시 풀어줌
            break

        # 상하좌우 확인
        for i, j in d:
            temp_x = x + i
            temp_y = y + j

            if 0 <= temp_x < 101 and 0 <= temp_y < 101 and field[temp_x][temp_y] != 0 and visited[temp_x][temp_y] == 0:
                field[temp_x][temp_y] = field[x][y] + 1
                visited[temp_x][temp_y] = 1
                queue.append((temp_x, temp_y))

    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)) # 17