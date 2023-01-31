'''
- 리트코드 215번 문제: kth-largest-element-in-an-array
- 문제 출처: https://leetcode.com/problems/kth-largest-element-in-an-array/
- Solution은 직접 풀었으며, Solution2, Solution3은 책을 참고하여 풀이하였습니다.
'''

'''
- 해당 풀이는 파이썬의 sort를 활용하여 풀이하였습니다.

- 문제 풀이 방법:
1. 매개변수 num 배열을 내림차순으로 정렬한다.(k번째로 큰 수를 찾기 위해 거꾸로 정렬)
    nums.sort(reverse=True)
2. 매개변수 num을 순회한다. 여기서 만약 k-1이 index와 같다면, sol 변수에 해당 인덱스를 저장한다.
    for index in range(len(nums)):
        if index == k - 1:
            sol = nums[index]
3. sol을 반환한다. 
'''
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 매개변수 num 배열을 내림차순으로 정렬
        nums.sort(reverse=True)   

        for index in range(len(nums)):

            if index == k - 1:
                sol = nums[index]

        return sol
                 
'''
- 해당 풀이는 책을 참고하였으며, Solution과 유사하지만 코드가 매우 간결하여 참고하였습니다.
'''
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

'''
- 해당 풀이는 책을 참고하였습니다,
- Solution, Solution2와 다르게 해당 풀이는 파이썬의 heapq 모듈을 활용하였습니다.
'''
from heapq import *

class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)    # 파이썬의 heaq는 min heap만 지원하므로 음수로 저장하여 역순으로 바꿔줌.
        
        for _ in range(1, k):
            heappop(heap)   # 정답이 나올 수 있도록 매개변수 k의 이전까지는 pop을 하여 heap 배열을 재배치한다.
        
        return -heappop(heap)   # 이전에 역순으로 바꿔주기 위하여 음수로 저장하였으므로 다시 음수를 넣어 양수로 바꿔준 뒤 반환한다.