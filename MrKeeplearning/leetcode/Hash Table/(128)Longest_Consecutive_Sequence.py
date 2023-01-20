from typing import List


class Solution:

    """
    기본적으로 현재 풀이에서 정의한 consecutive sequence는
    하나의 숫자로 이루어져도 consecutive sequence로 본다.

    따라서 consecutive sequence의 조건은 첫 시작 번호의 왼쪽으로
    자신보다 1만큼 작은 숫자가 존재하지 않는 것이다.

    [100, 4, 200, 1, 3, 2]가 있을 때
    consecutive sequence는 [1, 2, 3, 4], [100], [200]이 될 수 있다.
    """
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        # 가장 긴 sequence의 길이
        longest = 0

        for n in nums:
            # 시퀀스의 조건: 시퀀스의 시작번호는 왼쪽에 자신보다 1 만큼 작은 숫자가 없다.
            # 시퀀스의 시작이 될 수 있는 경우
            if (n - 1) not in num_set:
                # num_set 안에서 여러 개의 시퀀스가 나올 수 있기 때문에
                # 새로운 시퀀스를 발견하게 되면 length를 초기화한다.
                length = 0

                # 현재 번호가 num_set에 들어있다면
                # 현재 번호를 기준으로 1씩 증가시키고
                # 동시에 현재의 sequence의 길이를 length에 저장한다.
                while (n + length) in num_set:
                    length += 1
                # max를 활용해서 가장 긴 길이만 남긴다.
                longest = max(length, longest)
        return longest
