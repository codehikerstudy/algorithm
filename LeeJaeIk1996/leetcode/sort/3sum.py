'''
- 리트코드 15번 문제: 3sum
- 문제 출처: https://leetcode.com/problems/3sum/
- Solution은 직접 풀었지만 Wrong Answer이고, Solution2는 책을 참고한 풀이입니다.
'''
from typing import List

'''
- 해당 풀이가 문제 접근을 제대로 못한 이유: 두 수가 붙어있을 경우만 고려한 풀이이기 때문.
    예를 들어 input이 [-2,0,1,1,2]일 때, 정답은 [[-2,0,2],[-2,1,1]]일 것이다.
    하지만 해당 풀이로 접근할 경우 [-2,0,2]의 결과만 출력할 수 있다.
- 즉, 하나의 값을 기준으로 두 값을 따로따로 찾을 수 있는 코드를 작성해야 되는데, 해당 코드는
    하나의 값과 바로 옆에 있는 값 두 개를 기준으로 하나의 값만 찾는 코드인 것이다...
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # 매개변수 nums를 정렬

        start = 1
        sol : List[List[int]] = []    # output

        for index in range(0, len(nums)):

            if start < len(nums):
                three = nums[index] + nums[start]   # 세 번째 숫자

            if start < len(nums) and -three in nums[start+1:]:
                if sorted([nums[start], nums[index], -three]) not in sol:
                    sol.append(sorted([nums[start], nums[index], -three]))                               
        
            start += 1
            
        return sol

'''
- 해당 풀이는 책을 참고한 풀이입니다.
- 개인적으로 어떻게 동작하는지는 이해하였으나, 실전에서 사용하게 된다면 아직까진
    # left와 right 양 옆에 동일한 값이 있을 수 있으므로 left +=1, right -= 1을 반복해서 스킵하도록 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
    와 같은 코드를 제대로 작성할 자신이 없습니다. 앞으로 코드를 작성할 때 세세한 부분들을 모두 고려하여 작성할 수 있도록 항상 염두해야겠습니다.

- 문제 풀이 방법:
1. nums를 0부터 len(nums) -2 까지 순회한다.
    왜냐하면 # index를 기준으로 나머지 두 수는 뒤에서 찾을 것이기 때문에 len(nums) - 2의 범위까지 순회한다.
2. 순회 시작 지점(index) 다음부터 마지막 지점까지 각각 left와 right를 두어 index를 기준으로 값을 찾는다.
    left, right = index + 1, len(nums) - 1
3. 왼쪽과(index의 바로 다음부터 + 1씩 증가) 오른쪽(nums의 끝부터 - 1씩 감소)이 같아질 때까지 반복한다.
    while left < right:
4. sum = nums[index] + nums[left] + nums[right] 변수 작성
    - sum이 0보다 작을 경우 left를 1씩 증가
    - sum이 0보다 클 경우 right를 1씩 감소
    - sum이 0일 경우 result에 [nums[index], nums[left], nums[right]]를 추가
5. left와 right 양 옆에 동일한 값이 있을 수 있으므로 left +=1, right -= 1을 반복해서 스킵하도록 처리한다.
    while left < right and nums[left] == nums[left + 1]:
        left += 1
    while left < right and nums[right] == nums[right - 1]:
        right -= 1
6. left가 right와 같아질 때 까지 포인터를 이동하면서 값을 찾는다.
    left += 1
    right -= 1
'''
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # 매개변수를 정렬

        for index in range(len(nums) - 2):  # index를 기준으로 나머지 두 수는 뒤에서 찾을 것이기 때문에 len(nums) - 2의 범위까지 순회한다.
            # 중복된 값 건너뛰기
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # 간격을 좁혀가며 합(sum) 계산
            left, right = index + 1, len(nums) - 1
            while left < right: # 왼쪽과(index의 바로 다음부터 + 1씩 증가) 오른쪽(nums의 끝부터 - 1씩 감소)이 같아질 때까지 반복
                sum = nums[index] + nums[left] + nums[right]    # x + y + Z = 0이 될 경우 result에 추가
                if sum < 0:     # nums를 정렬하였으므로 left를 이동해야 sum의 값이 커지게 된다.
                    left += 1
                elif sum > 0:   # nums를 정렬하였으므로 right를 이동해야 sum의 값이 작아지게 된다.
                    right -= 1
                else:   # sum이 0이라는 뜻이기도 하다.
                    result.append([nums[index], nums[left], nums[right]])   # result에 추가
                
                    # left와 right 양 옆에 동일한 값이 있을 수 있으므로 left +=1, right -= 1을 반복해서 스킵하도록 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # left가 right와 같아질 때 까지 포인터를 이동하면서 값을 찾는다.
                    left += 1
                    right -= 1


        return result


print(Solution.threeSum("", [-1,0,1,0]))
                

        