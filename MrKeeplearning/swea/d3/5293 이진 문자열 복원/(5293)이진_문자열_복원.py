import sys
sys.stdin = open("sample_input.txt", "r")

"""
01
 10
  00
   00
    01
     11
      10
01000110

- 원래 문자열로 가능한 문자열이 있는지 없는지 판별 -> 길이가 맞는지 확인?
- 있다면 가능한 것 중 하나를 아무거나 출력
- 입력값의 네 정수 A,B,C,D는 각각 00, 01, 10, 11의 개수를 의미
- A + B + C + D >= 1

00 11
"""

T = int(input())    # 테스트 케이스의 수
for test_case in range(1, T + 1):

    pass
