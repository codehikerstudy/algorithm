# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
- Floyd's Tortoise & Hare 알고리즘 활용
- 느린포인터 s와 빠른 포인터 f를 가진다.
- 느린 포인터 s는 1씩 이동하고, 빠른 포인터 f는 2씩 이동한다. 이렇게 이동할 경우 빠른 포인터가 느린 포인터보다 먼저
  링크드리스트의 끝자락에 도달하게 된다.
- 그런데 만약 사이클이 있을 경우 f와 s는 같은 위치에서 만나게 된다. 이렇게 만나는 것이 확인된다면 사이클이 있다는 것을 의미한다.
"""
class Solution:
    def hasCycle(self, head) -> bool:
        # 처음에는 느린 포인터와 빠른 포인터 둘 다 같은 위치에서 시작한다.
        tortoise = head
        hare = head

        # 빠른 포인터가 2씩 더 앞서가기 때문에 먼저 링크드리스트의 끝에 도달한다.
        # 따라서 hare과 hare.next가 False라면 loop가 없다는 뜻이다.
        while hare and hare.next:
            # tortoise(느린 포인터)가 1씩 움질일 때
            # hare(빠른 포인터)는 2씩 움직인다.
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True

        return False

    # dictionary를 사용한 풀이 방법
    # 링크드리스트를 계속해서 순회를 한다. 만약 temp.next가 비어있다면(True가 아닐 때)
    # while문을 탈출하고 False를 반환한다.
    # 딕셔너리 안에는 현재 값과 True를 맵핑을 해서 while문을 도는 동안
    # 현재 값이 딕셔너리 안에 있다면 True를, 기존에 없던 새로운 값이면 딕셔너리에 추가를 해준다.
    def hasCycle(self, head) -> bool:
        dictionary = {}
        temp = head
        while temp:
            if temp in dictionary:
                return True
            else:
                dictionary[temp] = True
            temp = temp.next
        return False