'''
- 리트코드 128번 문제: longest-consecutive-sequence
- 문제 출처: https://leetcode.com/problems/longest-consecutive-sequence/
- 해당 문제 풀이는 sorted()와 max(), 배열을 활용하여 풀이하였습니다.

- 문제 풀이
1. input으로 들어오는 배열이 순서대로 있을 경우 cnt 값을 하나씩 늘려준다.(초기 cnt값은 1. why? 숫자의 갯수를 세기 위해선 0,1,2..로 세는 것이 아니라 1,2,3..으로 순서를 세기 때문)
    cnt = 1
2. cnt값을 넣어 줄 배열을 준비한다.
    sequence = []
3. input으로 들어오는 nums 배열을 정렬해준다.
    sorted_nums = sorted(nums)
4. 정렬된 input을 순회한다. 순회하면서 
    - 만약 현재 위치의 숫자 + 1이 다음 위치의 숫자와 같다면 cnt 값을 늘려주고,
        if i+1 < len(sorted_nums) and sorted_nums[i] + 1 == sorted_nums[i+1]:
                cnt += 1
    - 만약 현재 위치의 숫자가 다음 위치의 숫자와 같다면 cnt 값을 동일하게 한다.
        elif i+1 < len(sorted_nums) and sorted_nums[i] == sorted_nums[i+1]:
                cnt += 0
    - 위의 두 경우가 아니라면 현재까지 축적된 cnt값을 sequence 배열에 넣어준 뒤, cnt값을 초기화한다.
5. cnt값이 들어있는 sequence배열에서 가장 큰 값을 return한다.
    return max(sequence, default= 0)
'''
from typing import List

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = 1
        sequence = []
    
        # input으로 들어오는 nums를 정렬해준다.
        sorted_nums = sorted(nums)

        # 예외처리
        if sorted_nums is None:
            return 0

        for i in range(len(sorted_nums)):
            # 현재 위치의 숫자 +1과 다음 위치의 숫자가 같다면 cnt를 1 늘려준다.
            if i+1 < len(sorted_nums) and sorted_nums[i] + 1 == sorted_nums[i+1]:
                cnt += 1
            # 현재 위치의 숫자와 다음 위치의 숫자가 같다면 cnt 값을 그대로 둔다.
            elif i+1 < len(sorted_nums) and sorted_nums[i] == sorted_nums[i+1]:
                cnt += 0
            # 그 외에는 cnt값을 sequence 배열에 넣어준 뒤, cnt값을 초기화한다.
            else:
                sequence.append(cnt)
                cnt = 0

        # cnt 값이 모인 sequence에서 가장 큰 값을 return한다
        return max(sequence, default= 0)
                

             
        
        