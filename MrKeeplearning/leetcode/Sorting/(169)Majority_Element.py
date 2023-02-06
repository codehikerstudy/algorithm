from typing import List
from collections import Counter


class Solution1:

    """
    most_common()함수를 사용하면 각 요소의 등장횟수가 가장 많은 순으로 정렬하게 된다.
    따라서 과반수에 해당하는 요소는 가장 자주 등장한 요소이기 때문에
    리스트의 0번째 요소에서 0번째 값을 return하면 된다.
    """
    def majorityElement(self, nums: List[int]) -> int:
        result = Counter(nums).most_common()
        return result[0][0]


class Solution2:
    """
    분할정복과 백트레킹을 활용한 문제풀이
    """
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        a = self.majorityElement(nums[:len(nums) // 2])
        b = self.majorityElement(nums[len(nums) // 2:])

        return [b, a][nums.count(a) > len(nums) // 2]


class Solution3:
    """
    Boyer-Moore 알고리즘을 응용한 풀이

    이 풀이는 문제에서 과반수를 차지하는 요소가 항상 존재한다는 조건이 있기 때문에 가능한 풀이다.
    먼저 정답으로 반환할 result와 카운팅을 진행할 count 변수를 0으로 초기화한다.
    주어진 nums리스트를 순회하는 n이라는 변수를 둔다.

    count가 0일 때만 result의 값을 변환한다.
    nums 리스트를 순회하는 포인터인 n이 가리키는 값과 현재 result의 값이 같을 때
    count의 값을 1만큼 더하고, 다를 때는 -1을 하게 된다.

    대부분의 경우 n == result인 경우가 적기 때문에 반드시 count가 0이 되는 순간이 오게 되고
    이 때 result의 값을 바꾸게 된다.
    과반수가 항상 존재하기 때문에 결과적으로 과반수인 수를 출력하게 된다.

    가장 좋은 이해 방법은 아래의 코드를 종이에 직접 그려가면서 이해하는 것이다...

    """
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0

        for n in nums:
            if count == 0:
                result = n
            count += (1 if n == result else -1)
        return result


solution1 = Solution1()
solution2 = Solution2()
solution3 = Solution3()

nums = [2, 2, 1, 1, 1, 2, 2, 4, 4, 5, 4, 6, 7, 4, 5, 4]
example1 = [3, 2, 3]
example2 = [2, 2, 1, 1, 1, 2, 2]

print(len(nums))                            # Output is 16
print(Counter(nums).most_common())          # Output is [(4, 5), (2, 4), (1, 3), (5, 2), (6, 1), (7, 1)]

print(solution1.majorityElement(nums))      # Output is 4
print(solution2.majorityElement(nums))      # Output is 4
print(solution3.majorityElement(nums))      # Output is 5   예시로 사용한 nums 리스트에는 과반수인 수가 없기 때문에 다른 값이 나온다.
print(solution3.majorityElement(example1))  # Output is 3
print(solution3.majorityElement(example2))  # Output is 2
