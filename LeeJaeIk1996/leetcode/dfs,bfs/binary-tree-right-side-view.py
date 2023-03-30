'''
- 리트코드 199번 문제: binary tree right side view
- 문제 출처: https://leetcode.com/problems/binary-tree-right-side-view/
'''

'''
- 해당 풀이는 직접 푼 풀이이며, bfs를 활용하여 풀었습니다.
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        max_depth, depth = 0, 1     # 최대 깊이와 현재의 깊이
        answer = []                 # 반환값. 즉, 우측에서 보았을 때 보이는 노드들을 담는 배열

        # 예외 처리
        if root is None:
            return answer

        def dfs(node: Optional[TreeNode], depth):
            
            nonlocal max_depth

            # 종료 조건
            if not node:
                return
            
            if depth > max_depth:
                answer.append(node.val)
                max_depth = depth

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, depth)

        return answer