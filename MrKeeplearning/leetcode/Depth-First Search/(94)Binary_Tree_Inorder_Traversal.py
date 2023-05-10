from typing import Optional, List

"""
preorder(전위 순회): root -> left -> right
inorder(중위 순회): left -> root -> right
postorder(후위 순회): left -> right -> root
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    재귀함수를 사용한 풀이 방법
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(root):
            # root가 null이라면 아무 것도 할 필요가 없다.
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result


class Solution2:
    """
    참고자료: https://youtu.be/g_S5WuasWUE
    반복문을 사용한 풀이
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root  # 현재 포인터

        # 현재 포인터가 null이 아니고, stack이 비어 있지 않은 상태일 때까지 반복한다.
        while cur or stack:
            # left로 갈 수 없을 때까지 depth를 파고 내려간다.
            while cur:
                stack.append(cur)
                cur = cur.left
            # left가 더 이상 없다면 stack에서 pop을 한다.
            # pop한 것은 result에 넣어준다.
            # 왼쪽으로 계속 파고 내려가는 방식이기 때문에 그 과정에서 left가 root가 되는 과정이 반복된다.
            # 따라서, stack에서 pop을 하는 과정을 거치면 자연스럽게 root도 pop해서 result에 넣기 때문에
            # 중위순회가 이루어지는 것이다.
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result
