from typing import List
'''
- 리트코드 해시 문제: first-missing-positive
- 해당 문제 풀이는 배열과 정렬을 활용하여 문제를 풀이하였습니다.
- Test case에서는 Accepted가 나오지만 제출 시 Runtime Error가 나오는 틀린 답안입니다.
- 해당 문제는 아직 해결하지 못하여 추후 답안을 제출할 예정입니다.

'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        # 예외 처리
        if not nums:
            return 1
        
        # 음수 및 0 제거
        for i in sorted_nums:
            if i <= 0: 
                sorted_nums.pop(sorted_nums.index(i))
        
        
        for i in sorted_nums:
            # 음수를 전부 제거하였으므로 가장 최소값은 1이다.
            if not 1 in sorted_nums:
                return 1
            # 정렬된 값들 중 가장 최소인 i가 이전 값을 갖고 있지 않은 경우 최소는 i-1이다.
            # 1이 있을 경우 i-1은 0이므로 이를 고려해줌
            elif i -1 > 0 and i - 1 not in sorted_nums:
                return i - 1
            elif i + 1 not in sorted_nums:
                return i + 1