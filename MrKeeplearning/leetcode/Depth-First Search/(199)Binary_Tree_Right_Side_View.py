# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        if not root:
            return stack

        def dfs(root):
            if root.right:
                stack.append(root.right.val)
                dfs(root.right)
            return stack

        dfs(root)


class Solution2:
    """
    BFS를 활용한 풀이
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            pass


class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def selection(root):
            if root
