# yield 키워드

* 일반적으로 어떤 결과 값을 `return`키워드를 이용해서 반환을 하는 것과 달리 `yield`키워드를 사용하면 조금 다르게 결과 값을 제공할 수 있다.
* `return` 키워드는 결과값을 단 한 번만 제공할 수 있는 반면, `yield`를 사용하면 결과값을 여러 번 나누어서 제공할 수 있다.

```python
def return_abc():
  return list("ABC")

def yield_abc():
  yield "A"
  yield "B"
  yield "C"
```

* 둘 다 for문을 사용해서 하나씩 출력하도록 하면 결과값은 동일하지만 각 함수는 반환하는 것이 다르다.
* `return_abc()`는 리스트를 반환하는 반면, `yield_abc()`는 제너레이터를 반환한다.

```
>>> print(return_abc())
['A', 'B', 'C']
>>> print(yield_abc())
<generator object yield_abc at 0x7f4ed03e6040>
```

## Reference

[DaleSeo - 파이썬의 yield 키워드와 제너레이터](https://www.daleseo.com/python-yield/)