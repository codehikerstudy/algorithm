'''
- 리트코드 98번 문제: validate-binary-search-tree
- 문제 출처: https://leetcode.com/problems/validate-binary-search-tree/
'''

'''
- 해당 문제는 직접 풀었씁니다.
- 해당 문제는 dfs로 풀이하였습니다.
    - 98번 문제(Validate Binary Search Tree)를 풀기 전에 94번 문제(Binary Tree Inorder Traversal)를 풀었던 것을 상기하며 풀이하였습니다.
    - 이진 탐색 트리, 즉 BST는 왼쪽 자식이 부모 혹은 루트보다 작고, 오른쪽 자식이 부모 혹은 루트보다 크다는 특징을 지니고 있습니다.
    - 그리고 inorder는 left -> root -> right 순으로 순회합니다.
    - 이를 모두 종합하였을 때, BST를 inorder로 조회하게 되면 정렬된 순서로 결과가 출력된다는 점을 알 수 있습니다.
    - 이러한 점을 고려하여 아래의 코드를 작성하였습니다.
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inorder: list = []

        # inorder
        def dfs(node: Optional[TreeNode]):
            # 종료 조건
            if node is None:
                return

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)

        # 중위 순회를 하였으므로, BST일 경우 inorder: list = [] 배열이 정렬된 배열이어야 한다.
        for i in range(len(inorder)):
            if i+1 < len(inorder) and inorder[i] > inorder[i+1]:
                return False
            
        return True