# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return -1   # null tree의 height은 -1
            left = dfs(root.left)   # left subtree의 height
            right = dfs(root.right) # right subtree의 height

            # Diameter = left subtree height + right subtree height + 2
            result[0] = max(result[0], 2 + left + right)

            return 1 + max(left, right) # Height = 1 + max(left subtree height, right subtree height)

        dfs(root)
        return result[0]
