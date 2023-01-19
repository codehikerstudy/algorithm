# 문제명: Two_Sum
# url: https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hash_table = {}

        # target이 되기 위한 값의 인덱스를 담은 리스트
        result = []

        # enumerate을 사용해서 입력으로 주어진 nums 배열에 인덱스를 부여
        for i, val in enumerate(nums):
            if target-val in hash_table:
                result.extend(hash_table[target-val] + [i])
            if val not in hash_table:
                hash_table[val] = [i]
            else:
                hash_table[val].append(i)
        return result