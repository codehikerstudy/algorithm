'''
프로그래머스 스택/큐 12906번: 같은 숫자는 싫어

1. arr 배열의 숫자를 출력하려는 answer 배열에 push
2. arr 배열에서 앞의 숫자와 비교하여 수가 같을 경우 pop 
'''
def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])   # arr 배열의 숫자를 answer 배열에 push
        if i > 0 and arr[i] == arr[i-1]:
            answer.pop()        # 현재 배열이 가리키는 수와 이전의 수가 같을 경우 push하였던 answer의 수를 pop
            
    return answer