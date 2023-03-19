from collections import defaultdict


def solution(tickets):

    # stack에 마지막으로 담긴 값을 시작점으로 하는 티켓이 없을 때
    # stack의 마지막으로 담긴 값을 path에 넣어준다.
    path = []

    # 주어진 tickets에서 출발지를 key로, 목적지를 value로 가지는 해시맵 생성
    routes = defaultdict(list)
    for (start, end) in tickets:
        routes[start].append(end)

    # routes에서 출발지에 대응하는 도착지를 역순으로 정렬한다.
    for airport in routes.keys():
        routes[airport].sort(reverse=True)

    # 출발지는 항상 ICN부터 출발한다.
    stack = ["ICN"]

    # DFS로 모든 노드를 순회한다.
    while stack:
        # 스택에서 최상단 값을 꺼낸다.
        # 스택에는 현재 top이 없는 상태가 된다.
        top = stack.pop()

        # 만약 top을 출발지로 하는 티켓이 없을 경우 path에 저장한다.
        if not routes[top]:
            path.append(top)
        # top을 출발지로 하는 티켓이 있을 경우
        # 앞서 stack.pop()을 통해서 top을 stack에서 제거한 상태이기 때문에
        # 우선, top을 다시 stack에 저장해준다.
        # 그리고 routes에서 key가 top인 value 중에서 가장 마지막에 위치한 값을 꺼내어 stack에 저장한다.
        else:
            stack.append(top)
            stack.append(routes[top].pop())

    # stack에는 최종 경로가 뒤집혀서 들어가 있는 상태이기 때문에 뒤집어서 값을 반환한다.
    # 참고: list[<start>:<stop>:<step>]
    # start와 stop이 아무 것도 없는 상태라면 처음부터 끝까지를 의미. step이 -1이기 때문에 역순으로 출력하게 된다.
    return path[::-1]