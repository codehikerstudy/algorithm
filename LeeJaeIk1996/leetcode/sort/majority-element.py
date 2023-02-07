'''
- 리트코드 169번 문제: majority-element
- 문제 출처: https://leetcode.com/problems/majority-element/
- Solution은 직접 풀었고, Solution2, Solution3은 책을 참고하였습니다.
    Solution에서 유사 딕셔너리 Counter를 활용하여 문제를 풀이하였지만,
    Sort 태그인 문제이기 때문에 Sort와 관련된 풀이를 배우기 위해 책을 참고하였습니다.
'''


'''
- Solution은 직접 풀었습니다.
- 해당 문제 풀이는 collections.Counter를 활용하여 풀이하였습니다.

- 문제 풀이 방법:
1. 절반을 초과하는 수를 구하기 위해 half 변수를 선언한다
    half = len(nums) / 2
2. 매개변수 nums 배열 요소들의 수를 구하기 위해 collections.Counter()를 활용한다.
    num_count = Counter(nums)
3. num_count의 key, value를 순회한다.
    for num, value in num_count.items():
4. 만약 value(num_count key의 개수)가 이전에 선언한 half보다 크거나 같을 경우
    이를 sol 변수에 저장한다.
    if value >= half:
        sol = num
5. sol 변수를 반환한다.
    return sol
'''
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        half = len(nums) / 2
        
        num_count = Counter(nums)

        for num, value in num_count.items():
            if value >= half:
                sol = num
        
        return sol

'''
- Solution2는 책을 참고하여 풀이하였습니다.
- 해당 문제 풀이는 분할 정복을 활용하여 문제를 풀이하였습니다.
- 아직까지 분할 정복과 재귀 함수가 서툴러서 이전에 풀어봤던 문제들과 함께 계속
    봐야 될 필요가 있을 것 같습니다.
'''
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2

        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

'''
- Solution3은 책을 참고하여 풀이하였습니다.
- 해당 문제 풀이는 파이썬의 sorted()를 활용하여 풀이하였습니다.
- 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트일 것이라는 점을 고려하여 
    sorted로 풀 수 있다는 것이 인상깊었으며, 이런 생각을 할 수 있도록 노력해야겠습니다..
'''
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

print(Solution.majorityElement('', [3,2,3]))
print(Solution2.majorityElement('', [3,2,3]))
print(Solution3.majorityElement('', [3,2,3]))
