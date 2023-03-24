'''
- 리트코드 94번 문제: binary-tree-inorder-traversal
- 문제 출처: https://leetcode.com/problems/binary-tree-inorder-traversal/
'''

'''
- 해당 문제 풀이는 인터넷을 참고하여 풀이하였습니다.
- 해당 문제는 bfs를 활용하여 풀이하였습니다.
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def dfs(node: Optional[TreeNode]):
            # 종료 조건
            if node is None:
                return
            
            dfs(node.left)
            answer.append(node.val)
            dfs(node.right)

        dfs(root)
        return answer
    
print(Solution.inorderTraversal("", [1,2,3,4,5,6,7]))