'''
- 리트코드 124번 문제: binary tree maximum path sum
- 문제 출처: https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

'''
- 해당 문제는 인터넷을 참고하여 풀이하였으며, dfs의 재귀를 활용하였습니다.
- 자료 출처: https://www.dalecoding.com/problems/binary-tree-maximum-path-sum

- 개인적으로 해당 문제의 핵심은 '현재 노드를 기준으로 최대 경로를 구하는 것' 이라고 생각한다.
    그렇기 때문에 이 문제는 현재 노드를 기준으로 왼쪽 자식 노드와 오른쪽 자식 노드로 나누어 재귀적으로 풀어야 한다.
    예를 들어 다음과 같은 트리가 있다고 가정해보자.

        -10
        /   \
       9    20
            / \
           15  7

    우선, -10(루트 노드)을 시작으로 왼쪽 자식 노드(9)와 오른쪽 자식 노드(20)을 탐색한다.
    1. 왼쪽 자식 노드(9) 탐색
        - 왼쪽 자식 노드인 9에는 왼쪽 자식 노드, 오른쪽 자식 노드가 없으므로 최댓값은 9 + 0 + 0 = 9일 것이다.
        - 즉 현재 노드의 최댓값, max_path_sum = 9, max_path = 9이다.
        - 탐색을 끝냈으므로 9를 return한다. 여기서 9는 -10의 left_max값이다.
    2. 오른쪽 자식 노드(20) 탐색
        2.1. 오른쪽 자식 노드 20에서 다시 왼쪽 자식 15를 탐색한다.
            - 15의 자식 노드에는 왼쪽 자식 노드, 오른쪽 자식 노드가 없으므로 최댓값은 15 + 0 + 0 = 15이다.
            - 즉 현재 노드의 최댓값, max_path_sum = 15, max_path = 15이다.
            - 탐색을 끝냈으므로 15를 return한다. 여기서 15는 20의 left_max 값이다.
        2.2. 오른쪽 자식 노드 20에서 다시 오른쪽 자식 7을 탐색한다.
            - 7의 자식 노드에는 왼쪽 자식 노드, 오른쪽 자식 노드가 없으므로 최댓값은 7 + 0 + 0 = 7이다.
            - - 즉 현재 노드의 최댓값, max_path_sum = 7이지만, 아직 max_path = 15이다.
            - 탐색을 끝냈으므로 7을 return한다. 여기서 7은 20의 right_max 값이다.
        - 현재 노드, 즉 node.val = 20
        - 왼쪽 최댓값, 즉 left_max = 15
        - 오른쪽 최댓값, 즉 right_max = 7. 이들을 더한 것이 현재 경로의 최댓값이다.
        - 즉, max_path_sum = 42, max_path = 42이며, 현재까지 경로의 최댓값은 42이다.
        - 탐색을 끝냈으므로 현재의 노드(20)과 왼쪽 노드, 오른쪽 노드 중 큰 값(15)를 합한 값을 return한다.
    3. 루트 노드 탐색
        - 현재 노드, 즉 node.val = -10
        - 왼쪽의 최댓값, 즉 left_max = 9이다.
        - 오른쪽의 최댓값, 즉 right_max = 20+15 = 35이다.
        - 이를 합하면 max_path_sum = 34이며, max_path는 이전에 구한 42이다.
    이러한 순서로 42라는 결과가 나온다.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path = root.val

        def dfs(node: Optional[TreeNode]):
            nonlocal max_path
            # 종료 조건
            if not node:
                return
            
            # 현재 노드를 기준으로 왼쪽의 최대값과 오른쪽의 최대값을 구한다.
            left_max = dfs(node.left) or 0
            right_max = dfs(node.right) or 0

            # 현재 노드를 포함하는 경로의 최대값. 즉, 현재 노드를 기준으로 하는 경로의 최대값
            max_path_sum = node.val + max(left_max, 0) + max(right_max, 0)

            # 전체 트리에서 최대 경로 합을 갱신. 
            # 즉, 현재 노드를 기준으로 하는 경로의 최대값과 이전에 구했던 최대값을 비교
            max_path = max(max_path, max_path_sum)

            # 현재 노드를 루트로 하는 서브트리에서의 최대 경로 합
            return node.val + max(left_max, right_max, 0)
        
        dfs(root)

        return max_path



        
        