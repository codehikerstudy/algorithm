from typing import List

"""
시간 복잡도
- 입력된 배열을 정렬하는데 O(nlogn)의 사간 복잡도를 가진다.
- 그리고 정렬된 배열에서 for loop를 돌 때 O(n)의 시간 복잡도를 가진다.
- 따라서, O(nlogn)의 시간 복잡도를 가진다.

공간복잡도
- 결과 배열인 output의 공간이 가장 많이 차지하기 때문에 O(n)의 공간복잡도를 가진다.
"""


class Solution:

    """
    문제의 아이디어
    1. 구간 A와 구간 B가 겹치는가?
    2. 구간 A와 구간 B를 어떻게 병합할까?

    <<아이디어 1>>

    # 두 개의 구간이 겹치지 않는 경우

    A: _____
    B:       _____
    A[1] < B[0]

    A:       _____
    B: _____
    B[1] < A[0]

    # 두 개의 구간이 겹치는 경우 -> 겹치지 않는 경우의 반대

    not (A[1] < B[0] or B[1] < A[0])
    ==  A[1] >= B[0] and B[1] >= A[0]
    ==  A[0] <= B[1] AND B[0] <= A[1]

    위의 조건을 만족하면 구간 A와 구간 B가 겹친다고 할 수 있다.


    <<아이디어 2>>

    병합된 구간의 시작점은 A와 B의 시작점 중 더 작은 값을 선택하고,
    병합된 구간의 종료지점은 A와 B의 종료지점 중 더 큰 값을 선택한다.

    따라서, 병합된 구간은 다음과 같이 작성할 수 있다.

    [min(A[0], B[0]), max(A[1], B[1])]
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        intervals를 정렬한 뒤 최초의 상태는 다음과 같다.

        intervals = [ [1, 3], [2, 6], [8, 10], [15, 18] ]
        output = [ ]

        for loop를 돌면서 intervals의 요소를 output에 넣어준다.
        최초에는 빈 배열이기 때문에 intervals의 첫 요소는 output에 바로 삽입한다.

        intervals = [ [1, 3], [2, 6], [8, 10], [15, 18] ]
        output = [ [1, 3] ]

        [2, 6]에서 2는 output에 담긴 [1, 3]의 3보다 작기 때문에 두 개의 구간은 합칠 수 있다.
        output의 가장 마지막 요소인 [1, 3]의 두 번째 값인 3과
        현재 interval인 [2, 6]의 두 번째 값인 6, 둘 중에서 6이 더 크기 때문에
        output의 가장 마지막 요소인 [1, 3]의 두 번째 값인 3을 6으로 갱신한다.

        이와 같은 식으로 겹치는 구간은 병합하고,
        겹치지 않는 구간은 output에 추가하는 방식으로 output을 완성할 수 있다.
        """

        # 최종적으로 return할 배열.
        output = []
        # 주어진 intervals 배열은 정렬이 된 채로 주어졌지만, 정렬이 되지 않은 배열이 주어질 수도 있다.
        # 요소의 첫번째 값을 기준으로 오름차순으로 정렬되어 있다면 구간을 합치기 위한 조건을 확인하는데 훨씬 수월하다.
        for interval in sorted(intervals):
            # 최초의 output은 비어있는 상태이다. 이 때는 현재 interval을
            # output에 추가해야 하는 상황이기 때문에 not ouput이라는 조건을 추가한다.
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            # 병합할 수 있는 구간인 경우, output의 마지막 요소의 두 번째 값과
            # 현재 interval의 두 번쨰 값을 비교해서 더 큰 값을 output의 마지막 요소의 두번 째 값으로 갱신한다.
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output
