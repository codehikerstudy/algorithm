# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            # 최초에 루트의 왼쪽과 오른쪽에 자식노드가 없더라도 대칭구조이다.
            if not left and not right:
                return True
            # 하지만, 한쪽만 없다면 그건 대칭이 아니다.
            if not left or not right:
                return False
            # 대칭구조를 이룬다면 왼쪽과 오른쪽 노드가 동일하고
            # 왼쪽 노드의 왼쪽 자식과 오른쪽 노드의 오른쪽 노드가 서로 같고
            # 왼쪽 노드의 오른쪽 자식과 오른쪽 노드의 왼쪽 자식이 같아야 한다.-
            return (left.val == right.val and
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left))

        return dfs(root.left, root.right)

class Solution2:
    """
    deque을 활용한 풀이
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
            left = queue.popleft()
            right = queue.popleft()

            if not left and not right:
                continue
            elif left and right and (left.val == right.val):
                pass
            else:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

