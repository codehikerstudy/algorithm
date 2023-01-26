'''
- 프로그래머스 42746번 문제: 가장 큰 수
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/42746
- 해당 문제 풀이는 sort를 활용하였습니다. 문제 풀이 방법은 인터넷을 참고하였습니다.
- 개인적으로 해당 문제의 핵심은 sort의 key를 얼마나 활용할 수 있는지 인 것 같습니다. 
    해당 문제는 numbers 요소의 길이가 최대 1000 이하라는 점이 들어가 있는데, 이를 정렬의 기준으로 사용하여 문제를 푼다는 점이 인상깊었습니다.
- 그리고 단순히 .join을 활용해 반환하는 것이 아니라, .join으로 나오는 문자열을 int로 바꿔준 뒤, 다시 str로 바꿔줘야 된다는 것을 새롭게 알게 되었습니다.

- 문제 풀이:
1. 매개변수 numbers의 요소들을 string형태로 변환해준다.
    numbers = list(map(str, numbers))
2. 매개변수 numbers를 정렬해준다.
    - 이 때, sort의 key 함수를 lambda로 작성하여 key= lambda x: x*3으로 한다.
    - 여기서 x*3인 이유는, 문제에서 numbers의 요소들이 1000 이하이기 때문에 요소들을 다 같이 세 자리로 통일하여 비교해야 되기 때문이다.
    - 예를 들어 numbers = ["3", "30", "34", "5", "9"]라면 숫자가 아닌 문자열이기 때문에, 333, 303030, 343434, 555, 999가 된다.
        그러므로 303030 -> 333 -> 343434 -> 555 -> 999의 순서가 된다.
    - sort의 디폴트가 오름차순이므로, 내림차순으로 바꿔주기 위해 reverse=True를 작성한다.
        그러면 위에서의 303030 -> 333 -> 343434 -> 555 -> 999가 999 -> 555 -> 343434 -> 333 -> 303030이 되며,
        결국 9534330이 return된다.
3. 마지막으로 str(int(''.join(numbers)))를 활용하여 문자열로 반환한다. 
    이때 중요한 점은 .join으로 나오는 문자열을 int로 바꿔준 뒤, 다시 문자열로 반환해줘야 한다는 점이다.
    왜냐하면 numbers = [0, 0, 0]일 경우, 단순히 return ''.join(numbers) 로 반환할 경우 "0000" 의 결과가 나오게 된다.
    하지만 str(int(''.join(numbers)))로 반환할 경우 "0"의 결과가 나오므로, 이렇게 int로 바꿔준 뒤 다시 문자열로 반환해줘야 한다.
'''
def solution(numbers):

    numbers = list(map(str, numbers))   # 매개변수 numbers의 요소들을 string형태로 변환
    numbers.sort(key= lambda x: x*3, reverse= True) # 매개변수 numbers의 요소의 길이는 1000 이하이므로, 
                                                    # x*3을 통해 모든 요소들을 같은 길이로 통일하여 비교한 뒤 정렬한다.

    return str(int(''.join(numbers)))   # join()의 결과로 나오는 문자열을 int로 변환한 뒤, 다시 문자열로 변환하여 return한다.

print(solution([0, 0, 0]))