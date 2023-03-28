'''
- 리트코드 101번 문제: symmetric tree
- 리트코드 문제 출처: https://leetcode.com/problems/symmetric-tree/
'''

'''
- 해당 문제 풀이는 인터넷을 참고하여 풀이하였습니다.
- 문제 출처: https://airsbigdata.tistory.com/125
- 해당 문제는 dfs를 활용하여 풀이하였습니다.
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:       
        # 루트가 없을 경우 True
        if root is None:
            return True

        def dfs(leftNode: Optional[TreeNode], rightNode:Optional[TreeNode]):
            
            # left와 right가 모두 없을 경우 True
            if leftNode is None and rightNode is None:
                return True
            
            # left 혹은 right 둘 중 하나가 없을 경우 False
            if leftNode is None or rightNode is None:
                return False
            
            # left와 right가 다를 경우 False
            if leftNode.val != rightNode.val:
                return False
            
            # 왼쪽 값과 오른쪽 값을 비교
            left_right = dfs(leftNode.left, rightNode.right)

            # 오른쪽 값과 왼쪽 값을 비교
            right_left = dfs(leftNode.right, rightNode.left)

            # bool 타입. 둘 중 하나라도 False가 나온다면 False 값을 반환
            return left_right and right_left
        
        return dfs(root.left, root.right)
    
'''
- 해당 문제 풀이는 직접 푼 풀이입니다.
- 해당 풀이는 bfs를 활용한 풀이입니다.
'''
from collections import deque

class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 루트가 없을 경우 True
        if root is None:
            return True

        queue = deque()

        queue.append(root.left)
        queue.append(root.right)

        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()

            # 왼쪽과 오른쪽 모두 비었을 경우 
            if leftNode is None and rightNode is None:
                continue
            
            # 왼쪽 혹은 오른쪽 하나만 비었을 경우 
            if leftNode is None or rightNode is None:
                return False
            
            # 왼쪽 값과 오른쪽 값이 다른 경우
            if leftNode.val != rightNode.val:
                return False
            
            # 왼쪽 노드의 왼쪽 값과 오른쪽 노드의 오른쪽 값을 비교하기 위해 queue에 삽입
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            
            # 왼쪽 노드의 오른쪽 값과 오른쪽 노드의 왼쪽 값을 비교하기 위해 queue에 삽입
            queue.append(leftNode.right)
            queue.append(rightNode.left)

        # 아무 이상 없을 경우 True를 반환
        return True

