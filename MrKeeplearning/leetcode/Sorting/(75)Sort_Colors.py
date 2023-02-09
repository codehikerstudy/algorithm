from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)

    def partition(self, array, low, high):
        # 중간 값을 피봇으로 설정
        pivot = array[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while array[i] < pivot:
                i += 1

            j -= 1
            while array[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Swap
            array[i], array[j] = array[j], array[i]

    def quick_sort(self, items, low, high):
        if low < high:
            split_point = self.partition(items, low, high)
            self.quick_sort(items, low, split_point)
            self.quick_sort(items, split_point + 1, high)
