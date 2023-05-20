import sys
sys.stdin = open("input.txt", "r")
"""
- 파스칼의 삼각형을 미리 생성한다.
- N의 최댓값은 10이기 때문에 미리 만들어도 메모리나 시간 복잡도 상으로 큰 문제는 없을 것으로 판단된다.
- 각 테스트 케이스에서 주어지는 수에 따라서 필요한 만큼 출력해주는 방식을 택했다.
"""

T = int(input())

# N = 10일 때 파스칼의 삼각형을 담을 배열 생성
pascal = [[0 for _ in range(10)] for _ in range(10)]
# 10 x 10 사이즈의 행렬에서 항상 첫 번째 열은 값이 1이다.
# 파스칼의 삼각형을 만들기 위해 1을 채워준다.
for i in range(10):
    for j in range(i+1):
        if j == 0:
            pascal[i][j] = 1
        else:
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j], end=' ')
        print()
