# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # count == k가 되면 해당 값을 반환한다.
        count = 0
        stack = []
        current_node = root

        while current_node or stack:
            # 현재 노드가 null이 아닐 때까지 왼쪽 자식 노드를 탐색한다.
            # k번째로 작은 값을 찾기 위해서는 방문했던 노드로 다시 돌아가야 하기 때문에
            # stack에 방문했던 노드들을 삽입한다.
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            count += 1
            if count == k:
                return current_node.val
            current_node = current_node.right
