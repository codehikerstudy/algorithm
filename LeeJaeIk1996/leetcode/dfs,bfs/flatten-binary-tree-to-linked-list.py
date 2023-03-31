'''
- 리트코드 114번 문제: flatten binary tree to linked list
- 문제 출처: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''

'''
- 해당 풀이는 bfs를 활용한 풀이이며, 인터넷을 참고하여 풀이하였습니다.
- 참고 출처: https://j-e-n-n-y.tistory.com/14
- 개인적으로 이 문제를 제대로 접근하지 못했던 이유는 다음과 같습니다.
    "외부 변수를 선언하여 반환하지 말고, 루트 자체를 수정할 것."
    이를 어떻게 처리할지 한참을 고민하다가 인터넷을 참고하였으며,
    인터넷을 참고한 뒤 어느정도 이해하여 주석과 함께 풀이를 올렸습니다.
- 시간 복잡도: O(n)
    이진 트리의 모든 노드를 한 번씩 방문하므로 시간복잡도는 O(n)이다.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # 현재 노드의 이전 노드를 가리키는 변수. 시작은 None으로 설정
    tmp = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 종료 조건
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.tmp   # 오른쪽에 이전 값(tmp)을 넣는다
        root.left = None        # 왼쪽은 null로 처리
        self.tmp = root         # tmp를 현재 값으로 설정