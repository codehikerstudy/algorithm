from collections import Counter
from typing import List


class Solution1:
    """
    testcase는 통과했지만, 제출했을 때 아래의 예외에서 처리가 안되는 문제가 발생합니다.

    nums = [1, 2]
    k = 2
    Expected: [1, 2]
    Output: []

    주어진 k 조건에 맞지 않는 경우 주어진 nums를 그대로 반환해야 하는 것 같습니다...
    문제에서는 언급되어 있지 않았던 것 같은데 해당 예외조건 때문에 실패했습니다.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        counter_result = Counter(nums).most_common()
        for i in counter_result:
            if i[1] >= k:
                answer.append(i[0])
        return answer


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(Counter(nums).most_common())  # Output: [(1, 3), (2, 2), (3, 1)]

solution1 = Solution1()
print(solution1.topKFrequent(nums, k))

