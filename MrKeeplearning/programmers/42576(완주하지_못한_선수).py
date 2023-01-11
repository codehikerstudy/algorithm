"""
- 문제명: 폰켓몬
- url: https://school.programmers.co.kr/learn/courses/30/lessons/42576

- 파이썬 collections 모듈의 Counter는 산술연산자를 활용할 수 있다.
- 2개의 카운터 객체가 있을 때 두 객체를 더할 수도 있고, 두 객체를 뺄 수도 있다.
- 뺄셈의 결과로 0이나 음수가 나올 경우 최종 카운터 객체에서 제외가 된다.
- 이러한 원리를 사용해서 카운터 객체에서 key만 뽑아낸 다음
  list 형태로 만든 뒤 가장 첫 번째 값만 추출한다.
- 문제에서 "단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주했다"라고 언급했기에
  list(answer.keys())[0]와 같이 [0]을 추가해도 상관이 없다.

- Counter 객체에 대한 이해가 부족한 상태에서 혹시나 하는 마음에 시도한 방법이었으나
  문제가 풀렸기 때문에 추가적으로 Counter 객체에 대한 학습이 필요하다.
"""

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
