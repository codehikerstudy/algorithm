# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root

        while current_node:
            # p와 q 노드의 값이 현재 root보다 크다면 오른쪽을 탐색
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            # p와 q 노드의 값이 현재 root보다 작다면 왼쪽을 탐색
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            # p와 q 둘 중 하나라도 현재 root와 같다면 해당 값이 current_node가 되는 것이다.
            else:
                return current_node.val
