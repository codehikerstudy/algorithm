'''
- 프로그래머스 42839번 문제: 소수 찾기
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/42839
- 해당 문제는 인터넷을 참고하여 풀이하였습니다.
    이번 문제를 통해 Python permutation(), combination()을 알게 되었으며,
    소수를 어떻게 처리할지 정확하게 공부할 수 있었습니다.
    또한 아직까지는 리스트 내의 for문과 .join()에 미숙하다는 점을 느꼈습니다.
- 문제 풀이 방법:
1. 소수를 판별할 수 있는 함수를 생성한다.
    def is_prime_number(x):
        ...
        if x % i == 0:
            return False
        ...
2. 매개변수 numbers를 순회하며 permutations를 활용해 numbers의 숫자들을 나열한다.
    for i in range(1, len(numbers) + 1):
        nums += list(permutations(numbers, i))
    
    - 예를 들어 numbers가 "17" 이라면, 다음과 같은 결과가 나온다.
    ∴ [('1',), ('7',), ('1', '7'), ('7', '1')]
3. 파이썬의 .join을 활용하여 리스트를 문자열로 변환(여기서는 int로 변환)한 뒤,
    리스트로 저장한다.
    prime_number = [int(''.join(n)) for n in nums]

    - 예를 들어 numbers가 "17" 이라면, 다음과 같은 결과가 나온다.
    ∴ [1, 7, 17, 71]

4. 정리되어 있는 prime_number 리스트에서 소수를 판별하기 위해 순회한다. 
    이 때, 이전에 작성했던 is_prime_number(x) 함수를 활용한다.
    여기서 중요한 점은, set을 활용하여 중복을 방지한다는 점이다.
    만약 매개변수 numbers가 "011" 이라면, 다음과 같은 결과가 출력된다.
    ∴ [0, 1, 1, 1, 1, 10, 11, 10, 11, 11, 11, 101, 110, 101, 110]
    그러므로 set을 활용해 중복을 방지한다.
    
    for j in set(prime_number):
        if is_prime_number(j):
            print(j)
            cnt += 1

5. 소수의 개수(cnt)를 출력한다.
'''
from itertools import permutations

# 소수 판별 함수
def is_prime_number(x):
    # 2 이상의 자연수에 대한 소수 판별
    if x < 2:
        return False

    # 2부터 (x - 1)까지의 모든 수를 확인
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면 소수가 아님
        if x % i == 0:
            return False
    return True

def solution(numbers):

    nums = []
    cnt = 0

    for i in range(1, len(numbers) + 1):
        nums += list(permutations(numbers, i))  # 순열을 활용하여 숫자들을 분리
            
    prime_number = [int(''.join(n)) for n in nums]    # num을 합침

    for j in set(prime_number):
        if is_prime_number(j):
            print(j)
            cnt += 1

    
    return cnt


print(solution("011"))