import sys
sys.stdin = open("input.txt", "r")
"""
시간 초과로 실패한 풀이
"""

T = int(input())  # 테스트 케이스의 수
for test_case in range(1, T + 1):
    answer = 0
    N, R = map(int, input().split())  # nCr
    numerator = 1  # 분자
    denominator = 1  # 분모
    # 조합 공식의 분자
    # nCr공식의 분자에서 분모의 r! 부분을 제외한 나머지
    for i in range(R + 1, N + 1):
        numerator *= i
    # 조합 공식의 분모
    # (n-r)!만 계산
    for j in range(1, N - R + 1):
        denominator *= j
    
    if numerator // denominator < 1234567891:
        answer = numerator // denominator
    else:
        answer = (numerator // denominator) % 1234567891
    print(f'#{test_case} {answer}')
