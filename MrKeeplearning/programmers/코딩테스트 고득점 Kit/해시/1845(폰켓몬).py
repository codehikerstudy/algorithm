"""
- 문제명: 폰켓몬
- url: https://school.programmers.co.kr/learn/courses/30/lessons/1845

접근 사고 과정
1. 전체 폰켓못의 종류를 확인한다.
2. 최대로 가져갈 수 있는 폰켓몬은 전체의 반
3. 항상 내가 챙길 수 있는 수보다 홍박사가 가지고 있는 폰켓몬의 전체 수량은 2배 많다.
4. 구해야 하는 것은 챙길 수 있는 폰켓몬의 종류 수이다.
5. 내가 챙길 수 있는 전체 수보다 만약 종류가 많다면 챙길 수 있는 수량에 맞게 빼면 되고
   내가 챙길 수 있는 전체 수보다 종류가 적다면 부족분은 어떤 종류에서 더 가져오든 상관없기 때문에
   전체 종류 수만 리턴하면 된다.

단순히 최소값을 구하면 된다는 점을 알고 있었다면 min과 set을 사용해서 한 줄로 해결도 가능하다.

def solution(ls):
    return min(len(ls)/2, len(set(ls)))
"""
import collections


def solution(nums):
    max_take = len(nums) // 2
    freq = collections.Counter(nums)

    if len(freq) > max_take:
        return max_take
    else:
        return len(freq)
