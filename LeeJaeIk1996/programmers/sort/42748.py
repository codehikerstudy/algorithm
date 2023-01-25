'''
- 프로그래머스 42748번 문제: K번째 수
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/42748
- 해당 문제 풀이는 배열과 sort를 활용하여 풀이하였습니다.
- 첫 번째 답안은 직접 푼 답안이고, 두 번째 답안은 인터넷 서치를 통해 작성한 코드입니다.
- 첫 번째 답안의 이중 for문이 마음에 들지 않아 두 번째 답안을 보고 공부하였습니다.

- 첫 번째 답안 문제 풀이:
1. commands[0] - 1 ~ command[1]의 범위에서 나올 수 있는 array들을 담을 tmp 배열을 준비
    tmp = []
2. 답안을 담을 answer 배열을 준비
    answer = []
3. 이중 for문을 작성
    - 2차원 배열이 항상 3자리로 통일되었다는 것을 고려하여 commands를 담을 x,y,z 변수를 준비하여 for문 작성
    - command[0]-1 ~ command[1] 의 범위를 순회할 for문 작성
    for x,y,z in commands:
        for j in range(x - 1, y):
4. command[0]-1 ~ command[1] 범위에 존재하는 array 배열의 요소들을 tmp에 추가
    tmp.append(array[j])
5. tmp를 정렬한 뒤, command[2] - 1 번째 숫자를 answer에 추가
    tmp.sort()
    answer.append(tmp.pop(z - 1))
6. tmp 초기화 하여 commands의 다음 배열을 준비
    tmp = []
'''
def solution(array, commands):
    tmp = []    # 주어진 범위까지 자른 뒤 임시로 넣을 배열
    answer = [] # 값이 들어갈 배열

    for x,y,z in commands:
        for j in range(x - 1, y):
            tmp.append(array[j])

        tmp.sort()
        answer.append(tmp.pop(z - 1))
        tmp = []


    return answer

'''
- 개인적으로 두 번째 답안에서의 핵심은 슬라이싱과 sorted인 것 같습니다. 
    commands에서 나오는 범위를 array에 슬라이싱해서 sorted를 통해 정렬하는 것이 인상깊었습니다.
- 두 번째 답안 문제 풀이:
1. 답안을 담을 answer 배열을 준비
2. 이차원 배열 commands를 순회한다.
3. commands를 순회할 때 하나의 배열의 요소들을 x,y,z 변수로 담는다.
    예를 들어 commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]일 경우, 첫 번째 순회는 [2, 5, 3]이 될 것이다.
    이를 x,y,z = command를 통해 x= 2, y= 5, z= 3으로 담는다.
    이게 가능한 이유는 해당 문제의 배열 개수가 통일되어 있기 때문이다.
4. 매개변수 array 배열에서 x-1 ~ y 까지에 해당하는 요소들을 정렬한 뒤, z-1의 인덱스에 해당하는 값을 answer 배열에 넣는다.
5. answer를 반환한다.
'''
def solution2(array, commands):
    answer = []
    for command in commands:
        x,y,z = command # 이차원 배열 commands의 요소들을 x, y, z에 담는다.

        answer.append(sorted(array[x-1:y])[z-1])    # x, y의 범위를 array에 슬라이싱한 뒤, 이를 정렬하여 z에 해당하는 값을 answer 배열에 넣는다.

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

print(solution2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))