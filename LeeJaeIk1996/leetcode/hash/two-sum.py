from typing import List
'''
- 리트코드 해시 문제: two-sum
- 해당 문제 풀이는 for문과 in을 사용하여 문제를 풀었습니다.

- 문제 풀이 방법
1. 구하고자 하는 target은 nums[x] + nums[y]로 이루어져 있습니다.
    이 말은 즉, target - nums[x]를 구하면 된다는 말입니다.
    그러므로 nums를 순회하는 for문 안에 sol = target - i 를 넣어주었습니다.

2. in을 통해 sol이 현재 배열의 위치 뒤에 존재하는지 존재하지 않는지 확인하였습니다.
    if sol in nums[nums.index(i)+1:]

3. 만약 현재 배열의 위치 뒤에 존재한다면 각각의 nums[x]와 nums[y]의 index를 배열 형태로 출력하도록 구현하였습니다. 

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            sol = target - i    
            if sol in nums[nums.index(i)+1:]:
                return [nums.index(i), nums.index(sol, nums.index(i)+1)]


'''
- 리트코드 해시 문제: two-sum
- 해당 문제 풀이는 해시를 사용하여 풀었습니다.
- 문제 풀이 방법을 몰라 과거에 풀었던 문제 풀이 과정을 복습하여 재작성하였습니다.

- 문제 풀이
1. 하나의 hash table을 만든다. 해당 해시 테이블에는 
    key: 배열의 요소 , value: 배열 요소들의 인덱스
    가 들어갈 예정이다.

2. enumerate를 활용하여 index, 원소를 동시에 접근한다.

3. target - n 값이 hash_table의 key에 있는지 확인하여 있을 경우 
    return [hash_table[target - n], i] 를 반환한다.
    
4. hash_table에 
    key: 배열의 요소 / value: 배열 요소들의 인덱스
    를 저장한다.
'''
class Solution2:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}

        for i, n in enumerate(nums):
            if target - n in hash_table:
                return [hash_table[target - n], i]
            hash_table[n] = i  