'''
- 리트코드 해시 문제: longest-substring-without-repeating-characters
- 해당 문제 풀이는 해시와 투 포인터를 활용한 문제 풀이입니다.
- 시간 내에 문제를 풀지 못하여 책을 본 뒤 다시 작성한 풀이입니다. 아직 확실하게 이해하진 못하여 향후 다시 풀어볼 예정입니다.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used = {}
        # 투 포인터를 사용
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            # 최대 부분 문자열 길이 갱신
            else:
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length