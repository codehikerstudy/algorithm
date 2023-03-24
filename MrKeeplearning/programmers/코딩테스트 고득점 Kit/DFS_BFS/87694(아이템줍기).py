# 참고한 풀이: https://velog.io/@ledcost/프로그래머스-87694-파이썬-아이템-줍기-level-3-BFS
from collections import deque
import copy


def is_in_square(pos_x, pos_y, rec_num, rectangle):
    """
    특정 좌표를 본인이 속한 사각형(rec_num) 외의 모든 사각형(rectangle[:rec_num] + rectangle[rec_num+1:]과
    비교하여, 하나라도 자신 외의 사각형의 내부에 존재하는지 판단한다.

    만약 검사하는 좌표가 자신이 속한 사각형이 아닌 다른 사각형 내부에 존재하면 True를 반환하고,
    다른 사각형 내부에 존재하지 않으면 False를 반환한다.

    if not 구문을 통해서 False일 때 해당 좌표의 값을 1로 변환한다.

    :param pos_x: 유효한지 검사할 좌표의 x좌표
    :param pos_y: 유효한지 검사할 좌표의 y좌표
    :param rec_num: 검사 대상이 속한 사각형의 rectangle에서의 인덱스 번호
    :param rectangle: 문제에서 주어진 지형을 나타내는 직사각형이 담긴 2차원 배열
    :return: 검사할 좌표가 자신을 제외한 사각형 내부에 존재하면 True, 존재하지 않으면 False
    """
    for x1, y1, x2, y2 in rectangle[:rec_num] + rectangle[rec_num+1:]:
        # 검사할 좌표가 다른 사각형의 내부에 위치한다면,
        # 즉 최종 다각형의 외각선이 될 수 없다면 True를 반환.
        if x1 < pos_x < x2 and y1 < pos_y < y2:
            True

    return False


# 인접 노드 생성기
def move(x, y):
    if 1 <= x-1 <= 100:
        yield x-1, y #좌
    if 1 <= x+1 <= 100:
        yield x+1, y  #우
    if 1 <= y-1 <= 100:
        yield x, y-1  #하
    if 1 <= y+1 <= 100:
        yield x, y+1  #상


def solution(rectangle, characterX, characterY, itemX, itemY):
    """
    다각형의 테두리에 해당하는 좌표를 찾아 모드 1을 넣어두고, 출발지로부터 4방향으로 BFS 탐색을 하며
    값이 1이고 visited가 0인 노드로 계속 뻗어 가는 것이 핵심이다.
    이 때, ㄷ자 형태로 지나가는 경로의 경우 실제로는 떨어진 경로이더라도
    배열 상으로는 붙어있는 것처럼 표현되기 때문에 정확한 경로를 찾을 수 있도록
    모든 좌표를 2배로 늘려주고 시작한다.

    :param rectangle: 지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle
    :param characterX: 초기 캐릭터의 위치 x좌표
    :param characterY: 초기 캐릭터의 위치 y좌표
    :param itemX: 아이템의 위치 x좌표
    :param itemY: 아이템의 위치 y좌표
    :return: 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리
    """
    for i in range(len(rectangle)):
        for j in range(4):
            rectangle[i][j] *= 2
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    answer = 0
    # 좌표평면을 2배해서 0으로 채워진 100*100 사이즈의 좌표평면을 생성한다.
    roadmap = [[0]*101 for _ in range(101)]
    visited = copy.deepcopy(roadmap)

    # 다각형의 테두리에 해당하는 좌표를 구하는 작업.
    # 모든 사각형의 테두리에 해당하는 좌표를 순회하면서
    # 그것이 본인을 제외한 다른 모든 사각형의 내부에 속하지 않는다면
    # roadmap에 1로 표기해준다.
    rec_num = 0
    for x1, y1, x2, y2 in rectangle:
        # 가로 변의 모든 좌표들을 대상으로 유효한 좌표인지 검사
        for x in range(x1, x2 + 1):
            if not is_in_square(x, y1, rec_num, rectangle):
                roadmap[x][y1] = 1
            if not is_in_square(x, y2, rec_num, rectangle):
                roadmap[x][y2] = 1

        # 세로 변의 모든 좌표들을 대상으로 유효한 좌표인지 검사한다.
        for y in range(y1, y2+1):
            if not is_in_square(x1, y, rec_num, rectangle):
                roadmap[x1][y] = 1
            if not is_in_square(x2, y, rec_num, rectangle):
                roadmap[x2][y] = 1

        rec_num += 1

    deq = deque([(characterX, characterY)])
    visited[characterX][characterY] = 1

    while deq:
        current_x, current_y = deq.popleft()

        # 만약 현재 좌표가 아이템이 있는 좌표라면 그 때의 visited 값을 반환한다.
        # 좌표를 두 배 해주었기 때문에 정답도 원래의 두 배가 된다.
        # 따라서 2로 나눈 뒤 반환해야 한다.
        if (current_x, current_y) == (itemX, itemY):
            answer = visited[current_x][current_y] // 2
            break

        # 인접한 좌표가 유효한 좌표(roadmap이 1)이고 방문한 적이 없다면
        # 해당 인접 노드로 뻗어나간다(큐에 삽입).
        for adj_x, adj_y in move(current_x, current_y):
            if roadmap[adj_x][adj_y] and visited[adj_x][adj_y] == 0:
                deq.append((adj_x, adj_y))
                # 인접노드로 뻗어갈 때 visited에 뻗어간 인접노드의 값을 기록한다.
                # 이 때, 이전 노드의 visited 값을 누적해서 더한 값을 기록하여
                # 최종적으로 이동한 거리를 반환할 수 있도록 한다.
                visited[adj_x][adj_y] = visited[current_x][current_y] + 1
    return answer
