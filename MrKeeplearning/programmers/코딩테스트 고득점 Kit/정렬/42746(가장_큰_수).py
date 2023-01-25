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
        return str(n1) + str(n2) < str(n2) + str(n1)

    def solution(self, numbers):
        i = 1
        while i < len(numbers):
            j = i
            while j > 0 and self.to_swap(numbers[j - 1], numbers[j]):
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                j -= 1
            i += 1

        answer = str(int(''.join(map(str, numbers))))
        return answer


class Solution2:
    @staticmethod
    def solution(numbers):
        numbers_str = [str(num) for num in numbers]
        numbers_str.sort(key=lambda num: num * 3, reverse=True)

        return str(int(''.join(numbers_str)))
