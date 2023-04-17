import collections
from typing import List


class Solution:
    """
    교재를 참고한 풀이

    * 순환 구조인지 판별하는 문제
    * Time Limit Exceeded 발생 (통과x)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프의 노드 간 선수과목 관계를 hashmap형태로 정리
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 순환구조를 판별하기 위해 앞에서 방문한 노드를 traced 변수에 저장.
        # 중복방문할 시 순환구조로 간주하고 False를 리턴하고 종료.
        traced = set()

        # 순환구조를 찾기 위한 탐색
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색이 종료된 뒤 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조인지 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환구조이면 False
            if i in traced:
                return False
            # 이미 방문한 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True



