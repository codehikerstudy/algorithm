# 목차

- [sorted() 함수의 정렬 기준: functools.cmp_to_key](#--sorted--------------functoolscmp-to-key)
- [Tenary Operator](#--tenary-operator)
- [DFS로 완전탐색 접근 방법](#--dfs------------)
- [파이썬에서 전역 변수 사용하기: nonlocal, global](#--------------------nonlocal--global)

<br/>
<br/>

# ✅ sorted() 함수의 정렬 기준: functools.cmp_to_key

* 파이썬의 `sorted()`함수에는 3개의 매개변수를 가진다. 반복가능한 객체, key, reverse.
* 그리고 이 key는 반복가능한 객체를 정렬하는 기준으로 작용한다.
* 파이썬에는 두 개의 값을 비교하고 1, -1, 0을 반환하는 `cmp()`라는 함수가 존재했지만 파이썬 3.0 이후부터는 더 이상 사용되지 않고 그 대신 `cmp_to_key`가 등장했다.

## 1. `cmp_to_key()` 정의

* `cmp_to_key()`는 비교대상이 되는 요소들을 비교하기 위해 key를 사용한다.
* `functools` 모듈에 내장된 함수이기 때문에 반드시 `import functools`가 선행되어야 한다.
* 혼자 사용되지는 않고 `cmp_to_key()`에서 반환하는 키값을 사용할 수 있는 함수와 함께 사용된다. e.g., `min()`, `max()`, `sorted()`
* 하나의 argument만 받을 수 있는데 반드시 호출 가능한 객체가 와야 한다.
* 요소들을 비교하는데 사용할 수 있는 특별한 키를 반환한다.

## 2. 사용법

```python
import functools

functools.cmp_to_key(callable)
```

* 각 요소는 정렬된 리스트를 얻기 전까지 계속 서로 비교한다.
* 이 때 계속해서 `mycmp()` 함수를 비교할 때마다 호출한다. (아래 예시 참고)
* `mycmp()` 함수는 각 요소를 비교한 뒤에 key를 반환하고, 이 key는 `sorted()`함수가 오름차순으로 정렬하는 것을 돕는다.

### 예시1

```python
import functools


def mycmp(a, b):
	print("comparing ", a, " and ", b)
	if a > b:
		return 1
	elif a < b:
		return -1
	else:
		return 0


print(sorted([1, 2, 4, 2], key=functools.cmp_to_key(mycmp)))
```
**결과**
```
comparing  2  and  1
comparing  4  and  2
comparing  2  and  4
comparing  2  and  2
comparing  2  and  4
[1, 2, 2, 4]
```

### 예시2

```python
import functools


def mycmp(a, b):
	print("comparing ", a, " and ", b)
	if a > b:
		return 1
	elif a < b:
		return -1
	else:
		return 0


print(min([45, 78, 813], key=functools.cmp_to_key(mycmp)))
print(max([45, 78, 813], key=functools.cmp_to_key(mycmp)))
```
**결과**
```
comparing  78  and  45
comparing  813  and  45
45
comparing  78  and  45
comparing  813  and  78
813
```

## 3. 참고사항

* 위의 예시를 든 것처럼 `cmp_to_key()`에서 받는 호출 가능한 객체는 반드시 이름이 mycmp일 필요는 없다.
* mycmp에서 반환하는 key에 해당하는 1, 0, -1 또한 반드시 반환값이 1, 0, -1일 필요가 없다. 대신, **비교 대상에 해당하는 a, b가 있을 때 a > b 이면 양수를, a < b 이면 음수를, a == b 이면 0을 반환하기만 하면 된다.**

### Ref.
* [How does the functools cmp_to_key function works in Python?](https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/)

<br/>
<br/>

# ✅ Tenary Operator

삼항연산자는 파이썬 2.4부터 추가된 기능으로 조건의 참, 거짓에 따라서 판별하는 연산자이다.

## 1. 일반적인 삼항연산자

가장 기본적이면서 한 줄로 코드를 간소화하는 삼항연산자는 다음과 같다.

```python
# 문법
value_if_true if conditions else value_if_false

# 적용 사례
is_nice = True
state = "nice" if is_nice else "not nice"
```

## 2. 튜플을 적용한 삼항연산자

또 다른 방법으로는 튜플을 활용한 방법이 있다. 하지만, pythonic하지 않고 어디에 true 또는 false를 두어야 하는지 헷갈리는 방법이기 때문에 잘 사용되지 않는다.

참고로 튜플 대신 리스트가 올 수도 있다.

```python
#문법
(if_test_is_false, if_test_is_true)[test]

# 적용 사례
nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)
# Output: The cat is nice
```

또한, 튜플 삼항연산자(tupled tenary technique)를 사용할 경우 다음과 같은 오류가 발생하기도 한다.

```python
condition = True
print(2 if condition else 1/0)
#Output is 2

print((1/0, 2)[condition])
#ZeroDivisionError is raised
```

`condition = True`이기 때문에 `True`에 해당하는 값만 판별할 것 같지만 실행결과를 보면 `if-else`를 사용한 방법과 달리 튜플 삼항연산자는 zero division error가 발생하는 `False` 조건까지 확인한 것을 볼 수 있다.

튜플 삼항연산자를 사용하는 경우 튜플이 먼저 빌드된 뒤에 각 항목에 대해서 인덱스가 적용되기 때문에 위와 같은 오류가 발생한다. 반면, if-else 삼항연산자를 사용한 경우 if-else 구문의 논리구조에 따라서 실행되기 때문에 **zero division error**가 발생하지 않는다. 

따라서 True와 False 두 가지 경우 중 하나라도 예외를 발생시킬 수 있거나, 두 가지 경우 모두 계산이 복잡한 메서드를 사용한다면 가급적 튜플을 사용하는 방식은 피하는 것이 좋다.

## 3. ShortHand Tenary

일반적인 삼항연산자보다 훨씬 더 축약된 형태의 삼항연산자도 사용할 수 있다.

이 문법은 파이썬 2.5부터 소개되었고 파이썬 2.5 이상부터 모두 사용가능하다.

```python
# 활용 방법

True or "Some"
# Output is True

False or "Some"
# Output is "Some"
```

활용방법에서도 확인할 수 있듯이 `or`를 기준으로 왼쪽에 오는 값이 True일 경우에는 `True`를 반환하고 False 또는 None일 경우에는 `or`를 기준으로 오른쪽에 있는 값을 출력하게 된다.

구문이 매우 간단한 만큼 빠르게 함수의 출력을 확인해보고 싶을 때 사용하기에 좋다.

```python
# 적용 사례1

output = None
msg = output or "No data returned"
print(msg)
# Output is "No data returned"


# 적용 사례2: 함수의 매개변수로 활용

def my_func(real_name, optional_display=None):
    optional_display = optional_display or real_name
    print(optional_display)

my_func("Arthur")
# Output is "Arthur"
my_func("Arthur Morgan", "Arthur Callahan")
# Output is "Arthur Callahan"
```

위의 `my_func`함수처럼 간단하게 사용자가 자산의 본명과 닉네임을 둘 다 입력했을 때 본명이 아닌 닉네임이 출력되도록 할 때 활용할 수 있다.

### Ref.
* [Tenary Operators](https://book.pythontips.com/en/latest/ternary_operators.html)

<br/>
<br/>

# ✅ DFS로 완전탐색 접근 방법

* 어떤 문제를 DFS로 완전탐색을 해도 괜찮을지 확인하고 싶다면 시간복잡도를 계산해야 한다.
* 테스트케이스의 최악의 경우에 몇 번의 연산을 해야 하는지 확인해보고 그것이 5백만 번 미만이라면 완전탐색으로 해결하는 것이 충분히 가능하다고 생각하고 풀이해도 좋다.

> 단계별 접근 TIP
> 1. 수행동작을 먼저 구현한다. -> 현재 재귀함수에서 내가 무엇을 수행해야 하는지 정확하게 이해하고 정의한다.
> 2. 재귀함수를 더 이상 call하지 않는 탈출조건을 구현한다.
> 3. 재귀함수를 자세하게 그려보고 현재 코드에 대해 이해해본다.

### Ref.

* [프로그래머스 타겟넘버 풀이 영상](https://youtu.be/S2JDw9oNNDk)

<br/>
<br/>

# ✅ 파이썬에서 전역 변수 사용하기: nonlocal, global

현재 위치보다 더 넓은 범위에서 선언된 변수에 대해서 '읽기' 작업이 가능하다.

```python
n = 0
def func():
    print(n)    # Output is 0
func()
```
```python
def func1():
    n = 1
    def func2():
        print(n)    # Output is 1
    func2()

func1()
```

현재 위치보다 더 넓은 범위에서 선언된 변수에 대해서 '수정' 작업은 불가능하다.

```python
n = 0 
def func(): 
	n += 1  # UnboundLocalError: local variable 'n' referenced before assignment
	print(n) 
func()

def func1(): 
  n = 1 
  def func2(): 
  	n += 1  # UnboundLocalError: local variable 'n' referenced before assignment 
  	print(n) 
  func2() 
func1()
```

## 해결책1: global 사용하기

전역변수가 선언되어 있고 함수 내부에서 전역변수를 수정하고 싶다면 `global`을 사용해서 함수 내부에서 전역변수를 사용한다고 명시해주면 된다.

```python
n = 1 
def func1(): 
  def func2(): 
    global n 
    n += 1 
    print(n)    # Output is 2
  func2() 
func1()
```

## 해결책2: nonlocal 사용하기

전역변수가 아니고 현재 scope 내의 지역변수도 아닌 변수를 수정하기 위해서는 `global`이 아닌 `nonlocal`을 사용한다.

```python
def func1(): 
  n = 1
  def func2(): 
    nonlocal n
    n += 1
    print(n)    # Output is 2
  func2()
func1()
```

### Ref.

* [nonlocal, global로 변수의 scope 변경하기](https://juhi.tistory.com/6)

<br/>
<br/>
