from typing import List
from collections import Counter

class Solution:

    """
    각 element 별 등장 횟수를 저장하는 것이 가장 빠른 방법이 될 것이라고 생각
    결국 hash table의 개념을 사용할 수 밖에 없다고 생각함
    대신, hash table의 개념을 사용하는 대신 key 값을 기준으로 정렬을 한 뒤
    절반을 나눴을 때 해당 key의 value의 등장횟수가 전체 길이의 절반보다 긴지 검사를 하고
    만약 더 짧다면 오른쪽을 탐색한다.
    """
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums).most_common()
        n = len(nums)

        return count


class Solution2:

    pass


solution = Solution()
solution2 = Solution2()

nums = [2, 2, 1, 1, 1, 2, 2, 4, 4, 5, 4, 6, 7, 4, 5, 4]
print(solution.majorityElement(nums))
