'''
- 프로그래머스 84021번 문제: 퍼즐 조각 채우기
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/84021
'''

'''
- bfs를 활용하여 풀이하였습니다.
- 해당 문제 풀이는 인터넷을 참고하여 풀이하였습니다.
- 자료 출처: https://backtony.github.io/algorithm/2022-03-16-algorithm-programmers-level3-24/

- 다음 코드의 구성은 크게 다음과 같이 이루어져 있습니다.
    1. game_board에 비어있는 부분(= 0)들을 탐색한다. 
        이 때, 비어있는 부분(= 0)을 발견하면 bfs를 활용해 상하좌우를 확인하며 
        다른 부분에도 비어있는 부분들이 있는지 확인한다.
        즉, 비어 있는 부분이 있는 현재의 위치에서 상하좌우를 확인하며 0이 안보이는 곳까지 깊이 탐색하는 것이다.
        그리고 bfs를 활용하여 비어 있는 부분들을 탐색한 뒤 빈 배열 blank에 저장한다.

    2. table 자체를 총 4회전 시킨다. (개인적으로 회전을 어떻게 해야 되나 고민하였는데, table 자체를 회전시키면서 파악하면 됐었다..)
        이 때, 회전시킨 테이블에서 조각이 있는 부분(= 1)이 발견되면 bfs를 활용해 조각의 마지막 부분까지 탐색한다.
        그리고 퍼즐 조각이 이전에 만들었던 blank에 존재하는지 파악한 뒤, 존재한다면 answer에 조각의 칸 수만큼 +1시켜 저장한다.

- 문제를 통해 깨달은 점, 인상 깊었던 점 (문제 풀이를 보면서 즉흥적으로 생각하는 것이라 글의 정리가 제대로 안되어 있습니다.)
    
    1. bfs를 활용해 상하좌우를 파악하며 0이 더이상 존재하지 않는 곳까지 탐색한다는 것이 인상깊었다.
        현재 위치한 0(부모 노드) -> 자식 노드(0) -> 자식의 자식 노드(0) - > ... 끝까지 파고 드는 것이 매우 인상깊었다.

        다음에 이러한 문제가 비슷하게 나온다면 바로 떠올릴 수 있을 정도로 매우 인상깊었다.
        물론 bfs에 들어가는 매개변수를 정확히 설정할 자신까지는 없다. 이는 더 많은 문제들을 접하면서 bfs에 들어가는 매개변수에 대한 감을 익히도록 노력하자.

    2. 이 문제를 보면서 '회전을 대체 어떻게 처리해야되지?'라는 생각을 계속 하였는데, table 전체를 회전시키면 된다는 것이 인상깊었다.
        '그냥 인상깊었다' 정도가 아니라, '고민을 많이 함과 동시에 최대한 단순하게(효율적으로) 문제를 접근해보자고 생각해보는 계기'가 되었다.

        문제 풀이를 보기 전까지 나는 조각 하나하나를 회전시켜 회전된 위치의 인덱스들을 따로 저장해두려 했다.
        하지만 애초에 table에 존재하는 조각 하나 하나를 회전시키자는 생각은 매우 어리석은 생각이였으며, 
        코드를 짤 수 있다고 하더라도 매우 비효율적이였을 것이다.

        그렇다면 간단하면서도 효율적인 방법이 뭐가 있을까? -> 바로 테이블 전부를 회전시킨다는 것이다.
'''
import copy

def solution(game_board, table):
    n = len(game_board)
    answer = 0
    
    # game_board의 빈칸 좌표 0이 발견될 경우 빈 배열 blank에 조각 그대로를 옮기기
    # 💡 여기서 중요한건 0이 발견될 경우 bfs를 통해 다른 곳에도 0이 있는지를 검사하는 것이다.
    blank = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blank.append(dfs(game_board, i, j, [0, 0], n, 0))
                print(blank)

    # 회전이므로 총 4바퀴.
    for k in range(4):
        # 매개변수 table을 회전시킨다.
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if copy_table[i][j] == 1:
                    block = dfs(copy_table, i, j, [0, 0], n, 1)
                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = copy.deepcopy(copy_table)
                    else:
                        copy_table = copy.deepcopy(table)
    return answer

# position은 기준이 되는 좌표 -> 0,0으로 옮기기 위한 기준이 되는 좌표
def dfs(board, x, y, position: list, n, num):

    # 상하좌우 검사. 
    # 이를 통해 현재의 위치 x, y를 기준으로 상하좌우에 num과 같은 값이 있는지를 검사
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = [position]

    board[x][y] = 2  # 방문처리

    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]

        # 동서남북으로 구할 때 범위를 벗아나지 않는 경우 
        if 0 <= px and px < n and 0 <= py and py < n:
            # 만약 상,하,좌,우에 num과 같은 값이 있다면 그 곳을 탐색(bfs)
            if board[px][py] == num:
                result += dfs(board, px, py, [position[0] + dx[i], position[1] + dy[i]], n, num)
                
    return result

# 회전
def rotate(table):
    n = len(table)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = table[i][j]

    return rotated

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
               [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))