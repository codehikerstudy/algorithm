'''
프로그래머스 스택/큐 12909번: 올바른 괄호

1. "(" 괄호가 들어올 경우 arr 배열에 "("를 push
2. ")" 괄호가 들어올 경우 arr 배열을 pop. 
    만약 arr 배열이 비어있다면, 즉 "("가 더이상 없다면 False를 반환
'''
def solution(s):
    arr = []
    for bracket in s:
        if bracket is "(":      # "(" 괄호가 들어올 경우 arr 배열에 push
            arr.append(bracket)
        elif bracket is ")":
            if not arr:         # arr 배열에 더이상 "(" 괄호가 없다면 False를 반환
                return False
            else:               # arr 배열에 "(" 괄호가 있다면 "("를 pop
                arr.pop()
                
    if not arr:                 # arr 배열에 "("에 맞는 ")"가 등장하여 모두가 정상적으로 pop 되었을 경우 True를 반환
        return True
    else:                       # arr 배열에 "("가 남아있다면 False를 반환
        return False
        