# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    풀이 참고자료: https://youtu.be/meKRO8w6KT8

    직접 풀이 x
    <DFS 알고리즘과 반복을 활용한 풀이>

    DFS를 사용해서 트리의 모든 노드를 한 번씩 방문하기 때문에
    time complexity: O(n)

    최악의 경우 왼쪽 또는 오른쪽 한 방향으로만 트리가 이어질 경우
    스택의 길이가 노드의 길이와 같아지기 때문에
    space complexity: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        stack = [(root, 1)]
        # stack에 비어 있지 않다면 계속 루프를 돈다.
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            # 왼쪽 또는 오른쪽 노드가 존재한다면
            # 새로운 노드의 값과 갱신한 깊이를
            # 함께 스택에 삽입해준다.
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth


class Solution2:
    """
    직접 풀이 x
    <재귀 알고리즘을 적용한 풀이>

    현재 노드를 기준으로 최대 높이는 좌측 자식 트리와 우측 자식 트리 중
    최대 길이가 큰 값을 선택한 뒤에 1을 더하는 것이다.

    DFS를 스택이 아닌 재귀 알고리즘으로 구현한 것. 따라서...
    time complexity: O(n)

    공간복잡도를 구할 때 재귀 알고리즘은 최대 call stack(함수 호출 몇 번 했나?)의 크기를 고려해야 한다.
    이진트리가 linkedlist처럼 한 방향으로만 노드가 존재할 경우 call stack의 크기는
    노드의 총 개수와 동일해진다. 따라서...
    space complexity: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        """
        maxDepth를 재귀함수로 해서 좌측 서브트리와 우측 서브트리를 상대로 maxDepth를 재귀 호출한다.
        현재 노드와 왼쪽과 오른쪽 중 가장 긴 depth를 더했을 때 최대 depth가 나온다. 따라서 1을 더한다. 
        """
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
