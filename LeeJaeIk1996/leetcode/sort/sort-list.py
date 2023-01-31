'''
- 리트코드 148번 문제: sort-list
- 문제 출처: https://leetcode.com/problems/sort-list/
- 해당 문제 풀이는 책을 참고한 풀이입니다. 
    현재 문제 풀이는 답만 적어놓은 상태이고, 아직까지 풀이를 제대로 이해하지 못했습니다.
    빠른 시일 내에 문제를 제대로 이해하여 이전에 못풀었던 merge-intervals 문제와 함께 commit하겠습니다. ㅠ
'''
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head

print(Solution.sortList('', [4,2,1,3]))