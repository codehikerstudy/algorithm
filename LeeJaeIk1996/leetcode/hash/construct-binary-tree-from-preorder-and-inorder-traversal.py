'''
- 리트코드 105번 문제: construct-binary-tree-from-preorder-and-inorder-traversal
- 문제 출처: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- 해당 문제 풀이는 분할 정복을 활용하여 풀이하였습니다.
'''
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if inorder:
            # preorder의 순회 결과는 inorder의 순회 분할 인덱스
            # pop(0)은 시간복잡도가 O(n)
            index = inorder.index(preorder.pop(0))

            # inorder 순회 결과 분할 정복
            node = TreeNode(inorder[index]) # 1
            # 재귀를 활용하여 각 left와 right를 구한다
            # index를 기준으로 left, right를 나눴으므로 left는 inorder[0:index], right는 inorder[index+1:]
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

        return node