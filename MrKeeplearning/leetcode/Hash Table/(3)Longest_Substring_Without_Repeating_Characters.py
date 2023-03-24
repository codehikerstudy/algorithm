"""
첫 번째 풀이 방법은 test case 3에서 실패를 했다.
디버깅을 해보니 substring이 아닌 subsequence를 구하는 문제였다면 괜찮았다.

문자열이 이어지지 않고 주어진 문자열에서 단순히 중복이 없는
가장 긴 문자열을 구하는 문제의 풀이에 적합했다.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        result = 0

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[i])
            substring.add(s[i])
            result = max(result, len(substring))
        return result


"""
두 번째 풀이 방법은 첫 번째 풀이와 아이디어는 동일하게 가져갔지만,
substring을 구할 수 있도록 while문 부분을 수정했다.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 최초에는 단순히 중복을 허용하지 않는 점 때문에 set을 사용했으나
        # set을 사용했을 때(엄밀히 말하자면 HashSet에서) contains() 기능(파이썬에서 "in")이 O(1)으로 동작한다는 장점도 있었다.
        # 반면, 리스트에서 contains() 기능은 O(n)의 시간복잡도를 가진다.
        substring = set()
        result = 0
        j = 0

        for i in range(len(s)):
            # 만약 substring 안에 이미 해당 요소가 있다면
            # substring의 첫 글자를 삭제한다.
            # 이후 while문을 나온 뒤 현재 요소를 substring에 삽입한다.
            while s[i] in substring:
                substring.remove(s[j])
                j += 1
            # while문을 돌지 않을 경우 현재 값이 substring에 없다는 뜻이므로
            # 해당값을 substring에 넣어준다.
            substring.add(s[i])
            # 가장 긴 substring의 문자열 자체를 반환하는 것이 아닌
            # 단순히 해당 substring의 길이만 반환하는 것이기 때문에
            # 굳이 문자열을 저장하는 공간을 마련할 필요가 없이 매순간 길이만 확인하면 된다.
            # max(result, len(substring))에서 len(substring)은 현재 위치에서 substring의 길이를 말한다.
            # 그리고 result에는 for문 전체를 도는 동안 가장 긴 substring의 길이만 기록된다.
            result = max(result, len(substring))
        return result