'''
- 프로그래머스 43164번 문제: 여행 경로
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/43164
'''

'''
- 해당 문제 풀이는 bfs를 활용하여 풀이하였습니다.
- 해당 풀이는 시간 초과 및 TestCase를 실패한 오답입니다.
    - 우선, [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]에서 시간초과가 발생합니다.

    - 또한, [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]] 티켓들이 주어졌을 때,
        알파벳 순이긴 하지만 주어진 항공권을 모두 사용해야 한다는 조건에 걸립니다.

        즉, 알파벳 순이라면 ['ICN', 'A', 'B', 'D']라는 결과가 나오지만, 이는 주어진 항공권을 전부 사용하지 못하게 됩니다.
        결국 ['ICN', 'A', 'C', 'A', 'B', 'D']라는 답을 출력하지 못하게 됩니다.

- 해당 풀이를 통해 깨달은 점은 다음과 같습니다.
    1. "주어진 항공권을 모두 사용"이라는 것을 아예 배제하고 '당연히 모두 사용되겠지'라는 잘못된 생각을 하였다.
        애초에 문제에서 조건들이 주어진 데에는 다 이유가 있다는 것을 망각하였다.
        
    2. 뿐만 아니라 글을 너무 대충 읽었다. 글을 읽어야 풀이가 보일텐데, 너무 풀이에만 집중하였다.
'''
from collections import deque

def bfs(tickets):

    route: list = ["ICN"]    # 최종 여행 경로를 담는 배열. 출발지는 항상 ICN 공항

    queue = deque()
    queue.append("ICN") # 항상 "ICN" 공항에서 출발한다.

    # 큐가 비었을 때까지 반복
    while queue:

        start = queue.popleft() # 현재 위치
        temp = []   # 임시 도착지점들을 담는 배열
        for i in range(len(tickets)):    
            if tickets[i][0] == start:
                temp.append(tickets[i][1])
        
        if temp:
            temp.sort()
            temp_pop = temp.pop(0)
            queue.append(temp_pop)
            route.append(temp_pop)
        
    return route   

def solution(tickets):

    answer = bfs(tickets)

    return answer

'''
- 해당 문제 풀이는 dfs stack을 활용한 풀이입니다.
- 해당 풀이는 인터넷을 참고하여 풀이하였습니다.
- 자료 출처: https://velog.io/@inhwa1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS
'''
from collections import defaultdict

def solution2(tickets):
    path = []

    # {시작점: [도착점들]} 형태로 그래프를 생성
    # 만약 tickets = [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]] 인 경우
    # graph = defaultdict(<class 'list'>, {"ICN": ["A"], "A": ["B", "C"], "C": ["A"], "B": ["D"]})
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    # 리스트로 담긴 도착점들을 역순으로 정렬 (알파벳 순을 요구하기 때문)
    for airport in graph.keys():
        graph[airport].sort(reverse=True)
    
    # stack 생성 및 출발지 "ICN" 삽입
    stack = ["ICN"]

    # 노드 순회
    while stack:
        top = stack.pop()
        print(top)

        # top이 그래프에 없거나 top을 시작으로 하는 티켓이 없는 경우 path에 저장
        if top not in graph or not graph[top]:
            path.append(top)
        # top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장
        else:
            stack.append(top)
            stack.append(graph[top].pop())

        print(path, stack)

    return path[::-1]


print(solution2([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))