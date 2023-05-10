# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            """
            트리를 연결리스트로 만들고 해당 연결리스트의 tail을 반환한다.
            :param root: 주어진 트리
            :return: tail
            """
            # 트리가 비어있거나 null 노드를 만날 경우
            # 트리를 연결리스트로 만들 수 없는 상태이기 때문에
            # 이 때의 tail은 null이다.
            if not root:
                return None

            left_tail = dfs(root.left)
            right_tail = dfs(root.right)

            # 왼쪽과 오른쪽 서브트리가 비어 있다면 아무런 조치를 취하지 않아도 좋다.
            # 만약 오른쪽 서브트리가 비어 있다면 왼쪽 서브트리의 모든 노드들을
            # 오른쪽 서브트리쪽으로 옮겨주어야 한다.
            # 반면, 왼쪽 서브트리는 비어 있고 오른쪽 서브트리만 내용이 담겨 있다면 특별히 할 일이 없다.

            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None

            # 기본적으로 right_tail은 완성된 링크드리스트의 마지막 노드가 된다.
            # 그런데 만약 오른쪽 서브트리가 비어 있다면 어떻게 될까?
            # 이 때는 left_tail이 전체 링크드리스트의 tail이 된다.
            # 그렇다면, 오른쪽과 왼쪽 서브트리가 모두 null이라면 어떻게 될까?
            # 이러한 경우 root가 tail이 된다.
            # 한편 파이썬에서 아래와 같이 or를 사용하게 되면
            # 셋 중에서 null이 아닌 값을 찾아가게 된다.
            # 즉, right_tail이 null이면 left_tail을 살펴보고, left_tail도 null이면 root를 살펴보는 구조이다.
            last = right_tail or left_tail or root
            return last

        dfs(root)