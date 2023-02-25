# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 기본적인 아이디어는 두 개의 리스트를 연결했을 때
    # a+b와 b+a의 길이는 같아지기 때문에 비교를 하기 편해진다.
    # 또한 이렇게 둘을 연결했을 때 어디서 교차지점이 생기는지 확인하기 편하다.
    # 
    # 예시1
    # A + B : 41845561845
    # B + A : 56184541845
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # a와 b는 리스트의 시작점
        a = headA
        b = headB

        # a == b일 경우 둘 다 같은 노드에 있다는 것
        #  1. 해당 위치가 교차지점임을 의미. 해당 위치를 반환한다. (a 또는 b 둘 다 가능)
        #  2. 둘 다 null값을 가지는 경우로 교차지점을 찾지 못하고 마지막 노드까지 왔다는 것을 의미.
        #     이 경우 a 또는 b는 null 값을 보유하고 있기 때문에 해당 값을 return하면 된다.
        while a != b:
            # 만약 a가 null이라면(a의 끝에 도달했다면) b의 시작점을 가리켜야 한다.
            # 그렇지 않다면 그 다음을 가리킨다.
            if a != None:
                a = a.next
            else:
                a = headB

            if b != None:
                b = b.next
            else:
                b = headA

        return a

    # Hash table 개념을 활용하지만 딕셔너리가 아닌 set을 활용한 풀이(Hash Set)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        hash_set = set()

        while headA != None:
            hash_set.add(headA)
            headA = headA.next
        while headB != None:
            if headB in hash_set:
                return headB
            headB = headB.next
        return None
