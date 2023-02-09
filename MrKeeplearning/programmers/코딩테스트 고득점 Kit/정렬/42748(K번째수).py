"""
- 문제명: K번째 수
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/42748

- i번째, j번째에 사용되는 i,j는 인덱스 번호와는 다르다. 실제 인덱스보다 1많은 수이다.
- i번째부터 j번째까지 자르면 i, j번째 숫자는 모두 포함된다.
- k는 자른 구간에서만 사용되는 순서이며, i와 j처럼 실제 인덱스보다 1 많은 수를 가리킨다.
"""


def solution1(array, commands):
    answer = []
    for i in commands:
        k = i[2]
        sorted_array = sorted(array[i[0] - 1: i[1]])
        answer.append(sorted_array[k - 1])
    return answer


"""
- solution2의 경우 최초에 푼 나의 풀이와 동일한 풀이지만 변수를 조금 다르게 할당한 것이 인상 깊어 가져왔다.
- 주어진 array 안의 요소의 길이가 3으로 고정되어 있기 때문에 i, j, k = command가 가능하다.
- 심사자 입장에서 좀 더 풀이를 직관적으로 이해하기에 좋은 코드라고 생각된다.
"""


def solution2(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
