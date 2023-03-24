"""
- 문제명: 올바른 괄호
- url: https://school.programmers.co.kr/learn/courses/30/lessons/12909

- 문제를 풀기 직전 '파이썬 알고리즘 인터뷰' 책을 통해 스택, 큐 파트를 공부한 상태였고,
  해당 챕터에서 동일한 문제가 이미 나왔었기 때문에 쉽게 풀 수 있었다.

1. 여는 괄호가 나오면 stack이라는 이름의 리스트에 담는다.
2. 닫는 괄호를 key로, 여는 괄호를 value로 가지는 table이라는 딕셔너리를 생성한다.
3. 닫는 괄호가 나왔을 때 닫는 괄호에 맵핑된 value인 여는 괄호가 stack에서 pop한 결과와 일치하지 않는다면 False를 반환한다.
4. 마찬가지로 for문을 돌고 있는 동안 stack이 비어있는 상태라면 False를 반환한다.
5. 최종적으로 정상적으로 입력이 주어진 상태라면 for문은 빈 상태여야 하고 따라서 len(stack) == 0인 상태여야 한다.
6. 만약 비어져 있는 상태가 아니라면 len(stack) == 0은 False를 반환한다.
"""
def solution(s):
    stack = []
    table = {
        ')': '('
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    # 위의 for문을 정상적으로 모두 돌았다면 True를 반환한다. 모두 매칭이 되었기 때문에
    # append되었던 괄호들은 모두 pop이 된 상태이므로 stack은 비어있어야 한다.
    return len(stack) == 0
