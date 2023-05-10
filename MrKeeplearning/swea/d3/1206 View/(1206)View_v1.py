# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    apt_height = list(map(int, input().split()))
    answer = 0
    # 처음 시작과 끝 2자리는 제외하고 순회한다.
    for i in range(2, N-2):
        # 아파트 최대 높이 초기화
        cur_max_height = apt_height[i-2]
        # 현재 위치를 기준으로 왼쪽 2칸, 오른쪽 2칸의 범위에서 최대값을 구하기
        for j in range(i-2, i+3):
            if i == j:
                continue
            if cur_max_height < apt_height[j]:
                cur_max_height = apt_height[j]
        # 범위 내에서 최대값이 현재 위치의 아파트보다 작다면 그 둘의 차이는
        # 현재 위치 아파트의 조망권이 확보된 층수가 된다.
        if cur_max_height < apt_height[i]:
            answer += (apt_height[i] - cur_max_height)

    print(f'#{test_case} {answer}')
