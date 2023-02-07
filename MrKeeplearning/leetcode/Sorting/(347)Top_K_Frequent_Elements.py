import collections
import heapq
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


class Solution2:
    """
    Solution1의 경우 예외처리의 문제가 아니라 문제 자체를 잘못 이해해서 오답처리가 되었다.

    주어진 문제에서 요구하는 것은 가장 자주 등장하는 상위 k개의 요소를 찾는 것이다.
    따라서 1이 3번, 2가 2번, 3이 1번 등장하는 상황에서 k=2라면 [1, 2]가 return 되어야 하는 것이다.

    collections 모듈의 Counter 클래스는 주어진 nums 리스트의 각 요소가 몇 번씩 등장하는지 알려준다.
    또한, Counter 클래스에는 most_common()이라는 메서드가 있는데, 이를 사용하면 각 요소의 등장 횟수를 기준으로
    Counter결과에 대해서 내림차순 정렬을 해준다.

    nums1 = [1, 1, 1, 2, 2, 3] 일 때 most_common()을 적용한 결과는 아래와 같이 된다.
    [(1, 3), (2, 2), (3, 1)]

    자주 등장하는 수 중에서 상위 k개의 수를 리스트로 만들어 반환해야 한다.

    자주 등장하는 횟수에 따라 요소를 정렬하면 [1, 2, 3]이 된다.
    따라서 k=2일 때, [1, 2]가 반환되어야 한다.

    위의 반환값을 얻기 위해 most_common()결과를 인덱싱해서 answer라는 리스트에 필요한 값만 담아준다.

    최종적으로 answer를 return한다.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        counter_result = Counter(nums).most_common()
        for i in counter_result[:k]:
            answer.append(i[0])
        return answer


class Solution3:
    """
    파이썬의 heapq 모듈을 활용한 풀이
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)   # nums = nums1, Output: Counter({1: 3, 2: 2, 3: 1})
        freqs_heap = []

        print(freqs)
        # 파이썬의 heap은 기본적으로 최소힙이라는 점을 고려하여
        # 가장 큰 값이 루트에 올 수 있도록 음수로 만들어 삽입
        for f in freqs:
            # freqs는 딕셔너리 타입이기 때문에 key를 입력하면 value를 얻게 된다.
            # (freqs[f], f)는 (nums 리스트의 숫자 f의 빈도수, 숫자 f)를 의미하고 freqs[f]를 음수로 만들어
            # 가장 큰 빈도수가 루트에 올 수 있도록 만든다.
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = []
        # k번 만큼 추출한다.
        # 튜플로 빈도수와 해당 숫자를 묶어서 저장했고, 현재 필요한 것은 "해당 숫자"만이다.
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


class Solution4:
    """
    zip함수와 asterisk를 활용한 pythonic한 풀이
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


nums1 = [1, 1, 1, 2, 2, 3]
nums2 = [1]
nums3 = [1, 2]
k1 = 2
k2 = 1
k3 = 2

sol2 = Solution2()
print(sol2.topKFrequent(nums3, k3))     # Output is [1, 2]

sol3 = Solution3()
print(sol3.topKFrequent(nums1, k1))     # Output is [1, 2]
