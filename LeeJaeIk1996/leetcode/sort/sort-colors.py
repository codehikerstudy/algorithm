'''
- 리트코드 75번 문제: sor-colors
- 문제 출처: https://leetcode.com/problems/sort-colors/
- 해당 문제 풀이는 포인터를 활용한 풀이입니다.
- Solution은 책을 참고한 풀이이고, Solution2는 책을 참고하기 전 스스로 풀다가 실패한 풀이입니다.
    Solution2는 투 포인터를 활용하였는데, 투 포인터로는 처리할 수 없었습니다.
    예를 들어 input이 [2, 0, 2, 1, 1, 0]이라면
    결과값이 [0, 0, 2, 1, 1, 2]라는 잘못된 결과가 출력되었습니다.
    개인적으로 두 개의 포인터로는 해결할 수 없고 하나의 포인터가 더 필요하다고 생각하였지만
    어느 기준으로 포인터를 하나 더 두어야 할지 몰라 결국 책을 참고하였습니다.
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3개의 포인터를 둔다.
        # red와 white는 0부터 시작하며, blue는 nums 배열 범위 밖에서 시작한다.
        red, white, blue = 0, 0, len(nums)

        # white가 blue에 다다를 때까지 반복한다.
        # 개인적으로 white를 기준(white=1)으로 red와 blue를 고려하는 것이 해당 풀이의 핵심이라고 생각한다.
        while white < blue:
            # white가 1보다 작다면(참고로 white는 1이어야 한다.)
            if nums[white] < 1:
                # red 위치의 숫자와 white 위치의 숫자를 swap해준 뒤 white와 red를 한 칸 앞으로 이동
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # white가 1보다 크다면
            elif nums[white] > 1:
                # blue를 한 칸 뒤로 이동하면서 white와 blue를 swap한다.
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            # white가 1이라면 맞는 위치이므로 white를 한 칸 앞으로 이동
            else:
                white += 1


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1

        while left > right:
            if nums[left] > nums[right]:
                nums[left] = nums[right]
                nums[right] = nums[left]
                left += 1

            if nums[left] < nums[right]:
                right -= 1

                





       
        