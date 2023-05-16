import sys
sys.stdin = open("input.txt", "r")
"""
- 초기값: 모든 비트가 0으로 이루어진 상태
- 특정 자리에 값을 설정하면 해당 값으로 뒤에 오는 비트들이 설정된다.

- 첫 번째 값은 0이라면 체크할 필요가 없지만 첫 번째 값이 1이라면 answer += 1
- 첫 번째 값 이후부터는 앞의 값과 현재의 값이 다르면 answer +=1 
"""
T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    memory = list(map(int, list(input())))

    # 인덱스가 음수가 되는 상황을 방지하기 위해 첫 번째 값은 따로 검사
    if memory[0] == 1:
        answer += 1

    for i in range(1, len(memory)):
        if memory[i-1] != memory[i]:
            answer += 1

    print(f'#{test_case} {answer}')
