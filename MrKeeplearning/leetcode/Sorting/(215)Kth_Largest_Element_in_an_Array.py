import heapq
from typing import List


class Solution1:

    """
    파이썬의 내장함수를 활용한 풀이
    빠르고 간단하게 풀 수 있지만, 정렬 알고리즘을 활용해서 설명해야 하는 상황에서는 좋은 풀이가 아니다.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_list = sorted(nums)
        return sorted_list[-k]


class Solution2:
    """
    파이썬의 heapq 모듈을 활용한 풀이

    heapq 모듈은 최소힙만 지원한다.
    따라서 음수로 저장을 하게 되면 기존에 인수로 전달 받은 nums 리스트에서
    가장 큰 값이 가장 작은 값이 되어 트리의 루트에 오게 된다.

    또한 heapq.heappop()을 사용하면 가장 작은 값을 삭제하고 해당 값을 반환한다.
    이렇게 반환 받은 값에 음수 부호를 붙인다면 최대힙과 동일하게 작동할 수 있다.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 원소를 추가할 리스트
        heap = []

        # heapq 모듈은 최소힙만 지원하기 때문에
        # 가장 큰 값이 루트에 오게 하고 싶다면 음수로 저장하면 된다.
        for n in nums:
            heapq.heappush(heap, -n)

        # k번째로 큰 값을 구해야 하기 때문에 k-1번째 값까지 삭제를 하고
        # 그 다음으로 heappop을 했을 때 나오는 값이 k번째로 큰 값이 된다.
        # 모든 값은 음수로 저장되어 있기 때문에 pop을 한 뒤 얻은 값에
        # 마이너스르 붙여주어야 원하는 값을 얻을 수 있다.
        for _ in range(1, k):
            heapq.heappop(heap)
        return -heapq.heappop(heap)


class Solution3:
    """
    heapq모듈의 heapify를 활용한 풀이

    heapify()를 사용하면 주어진 자료구조를 힙의 특성에 맞게 변환해주는 기능을 한다.
    일회성으로 변경을 하는 것이기 때문에 만약 heapify를 한 상태에서
    새로운 원소를 추가하게 되면 heap의 특성이 깨진다.

    현재 문제에서는 새로운 원소를 추가하는 상황이 없기 때문에 큰 문제가 없다.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        # k번째로 큰 요소를 return해야 하기 때문에
        # k+1번째로 큰 수까지 삭제한 다음
        # k번째로 큰 수를 return하도록 만든다.
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


class Solution4:
    """
    heapq 모듈의 nlargest를 사용

    nlargest를 사용하면 heapq.nlargest(k, nums)를 했을 때
    nums 리스트를 heapify하여 heap 형태로 만든 뒤
    1번째부터 k번째까지 큰 수를 순서대로 리스트에 담아 반환한다.

    예를 들어 nums = [3, 2, 1, 5, 6, 4]이고 k = 2일 때
    heapq.nlargest(k, nums)는 [6, 5]를 반환한다.

    결과적으로 k번째로 큰 값을 원한다면 인덱싱을 통해 가장 마지막 원소를 추출하면 된다.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]



example1 = [3, 2, 1, 5, 6, 4]
example2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]

k1 = 2
k2 = 4

solution1 = Solution1()
print(solution1.findKthLargest(example1, k1))
print(solution1.findKthLargest(example2, k2))

print("----------")

solution2 = Solution2()
print(solution2.findKthLargest(example1, k1))
print(solution2.findKthLargest(example2, k2))

print("----------")

solution4 = Solution4()
print(solution4.findKthLargest(example1, k1))
print(solution4.findKthLargest(example2, k2))
