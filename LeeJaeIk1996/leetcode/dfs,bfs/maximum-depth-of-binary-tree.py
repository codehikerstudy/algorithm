'''
- 리트코드 104번 문제: maximum depth of binary tree
- 문제 출처: https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
- 해당 문제 풀이는 직접 푼 풀이입니다.
- bfs의 재귀를 활용하여 풀이하였습니다.
    - 루트부터 출발하여 왼쪽과 오른쪽 따로 따로 dfs를 호출합니다.
    - 만약 노드를 밑으로 내려가면서 끝까지 도달하였을 경우 max_depth을 depth 배열에 저장합니다.
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 루트가 비었을 경우 0
        if root is None:
            return 0
        
        max_depth = 1   # 루트부터 시작하므로 깊이(max_depth)는 1부터 시작
        depth = []   # 깊이를 저장하는 배열
        
        def dfs(node: Optional[TreeNode], max_depth):

            # 왼쪽 노드가 존재할 경우 해당 node.left를 탐색
            if node.left:
               dfs(node.left, max_depth + 1)

            # 오른쪽 노드가 존재할 경우 해당 node.right를 탐색
            if node.right:
                dfs(node.right, max_depth + 1)

            depth.append(max_depth) # dfs로 내려간 만큼을 depth 배열에 저장

        dfs(root, max_depth)    # root node부터 출발

        return max(depth)   # 저장된 깊이들 중 최댓값을 반환
    
'''
- 해당 문제 풀이는 책(파이썬 알고리즘 인터뷰)을 참고하여 풀이하였습니다.
- bfs의 queue를 활용한 풀이입니다.
'''
from collections import deque

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 루트가 비었을 경우 0
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)  # 우선, root node를 queue에 저장
        
        depth = 0

        # 큐가 빌 때까지 반복
        while queue:

            depth += 1  # 반복된 횟수 = 깊이

            # 큐에 들어 있는 노드들의 개수만큼 순회
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                # 왼쪽 노드가 존재한다면 큐에 삽입
                if cur_node.left:
                    queue.append(cur_node.left)
                # 오른쪽 노드가 존재한다면 큐에 삽입
                if cur_node.right:
                    queue.append(cur_node.right)

        # while문이 돌아간 만큼 = 노드 -> 자식노드.. 내려간 만큼
        return depth

