"""
문제명: 가장 큰 수
URL: https://school.programmers.co.kr/learn/courses/30/lessons/42746


Solution1 -> 시간초과로 실패
- 이어붙일 때 가장 우선순위는 요소의 가장 첫번째 숫자가 큰 순으로 이어붙여 한다.
  예를 들어, [6, 10, 2]에서 첫 번째 숫자가 큰 순으로 나열하면 6, 2, 10이 된다.
- numbers 배열에는 한 자리 숫자만 담기는 것이 아니라 그 이상의 자릿수를 가지는 숫자들도 담긴다.

- 삽입정렬을 위해 이중 while문을 두었는데 안쪽 while문은 정렬을 한 뒤에 다시 한 번 앞의 숫자들에 대해서도 정렬을 맞춰준다.
- 예를 들어 [6, 10, 2] 가 있을 때 현재 차례에서 10과 2를 비교해서 [6, 2, 10] 순서가 되었다면 6과 2에 대해서도 한 번 더
  비교를 해주는 것이다. -> 삽입정렬에 대해서 완전히 이해를 못해서 그런지 이 부분을 구현하는 아이디어를 얻는 것에 애를 먹었다.
"""


class Solution1:
    @staticmethod
    def to_swap(n1, n2):
        return n1 + n2 < n2 + n1

    def solution(self, numbers):
        # 첫 번째 정렬
        numbers_str = [str(num) for num in numbers]
        i = 1
        while i < len(numbers_str):
            j = i
            while j > 0 and self.to_swap(numbers_str[j - 1], numbers_str[j]):
                numbers_str[j], numbers_str[j - 1] = numbers_str[j - 1], numbers_str[j]
                j -= 1
            i += 1

        answer = str(int(''.join(numbers_str)))
        return answer


"""
Solution2
- 정렬을 두 번 해준다.
- 첫 번째 정렬은 numbers에 담긴 요소를 str로 형 변환을 한 뒤 ascii 값을 기준으로 정렬을 한다.
- 두 번째 정렬은 테스트 케이스로 공개한 [3, 30, 34, 5, 9] 때문에 적용한다.
- 첫 번째 정렬로 한 번 정렬을 하면 [3, 30, 34, 5, 9] 은 [9, 5, 34, 30, 3]이 되는데, 이것을 그대로 이어붙여도 가장 큰 수가 아니다.
- 두 번째 정렬에서 num을 3번 곱하는데 그 이유는 number의 제약조건으로 1000이하의 수만 들어간다고 되어 있었고
  그래서 최대값을 생각해 세자리 수를 만들고 싶어 3을 곱했다고 한다.
- 그렇게 해서 ascii 값으로 정렬을 하면 원하는 순서로 정렬된다고 하는데, 솔직히 납득이 잘 되지 않는다.
- 너무 독특한 풀이 방법이고 이것을 내가 생각해 낼 수 있는 방법은 아닌 것 같다.
"""


class Solution2:
    @staticmethod
    def solution(numbers):
        # 첫 번째 정렬
        numbers_str = [str(num) for num in numbers]
        # 두 번째 정렬
        numbers_str.sort(key=lambda num: num * 3, reverse=True)

        return str(int(''.join(numbers_str)))


"""
Solution3
- functools.cmp_to_key()를 활용한 풀이
- solution2보다는 훨씬 현실적으로 생각해 볼 수 있을 법한 풀이인 것 같다.
"""
import functools


class Solution3:

    @staticmethod
    def compare(n1, n2):
        c1 = int(n1 + n2)
        c2 = int(n2 + n1)
        # c1 > c2 인 경우 양수를 반환
        # c1 < c2 인 경우 음수를 반환
        # c1 == c2 인 경우 0을 반환
        return c1 - c2

    @staticmethod
    def solution(numbers):
        nums_str = [str(x) for x in numbers]
        sorted_nums = sorted(nums_str, key=functools.cmp_to_key(compare), reverse=True)
        answer = str(int(''.join(sorted_nums)))
        return answer
