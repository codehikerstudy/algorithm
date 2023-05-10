# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, low, high):
            # 트리에 아무 것도 없어도 valid한 BST이다.
            if not node:
                return True
            # BST의 조건을 만족하기 위함
            if not (low < node.val < high):
                return False

            """
            첫 번째 node.val은 node.left의 parent로 작동한다.
            node.left는 parent보다 작아야 하며 오른쪽 서브트리의 모든 값들보다도 작아야 한다.

            두 번째 node.val은 node.right의 parent로 작동한다.
            node.right는 parent보다 커야 하며 왼쪽 서브트리의 모든 값들보다도 커야 한다.
            """
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        # root에는 어떤 값이 오든 상관없다.
        # root는 음의 무한대와 양의 무한대 사이에 있기 때문에
        # left는 float("-inf"), right는 float("inf")가 오게 된다.
        return valid(root, float("-inf"), float("inf"))

