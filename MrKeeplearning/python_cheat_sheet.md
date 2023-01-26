# 목차

* [functools.cmp_to_key](#sorted---함수의-정렬-기준--functoolscmptokey)

# sorted() 함수의 정렬 기준: functools.cmp_to_key

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

<br/>
<br/>

### Ref.
* [How does the functools cmp_to_key function works in Python?](https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/)