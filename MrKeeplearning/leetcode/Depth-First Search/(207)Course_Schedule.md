# Leetcode 207. Course Schedule 풀이

# 1. 기본 아이디어

주어진 그래프가 순환구조인지 판별하는 문제이다. A라는 과목의 선수과목이 B라면, B의 선수과목이 A인 상황은 발생하면 안된다. 따라서, 순환구조가 아닐 경우 모든 코스를 완료할 수 있는 상황이다.

# 2. 코드별 해설

## Solution 1

```python
graph = collections.defaultdict(list)
for x, y in prerequisites:
    graph[x].append(y)
```

예를 들어 `prerequisites`가 다음과 같이 값을 가지고 있다고 가정해보자.

```python
prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
```

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/232379409-972ce3ff-18fe-48fd-b4cb-7dc9c85bbd48.png" width="500">
</p>

예시로 사용한 `prerequisites`의 선수과목 관계를 그래프로 시각화하면 훨씬 더 순환구조인지 판별하기 쉽고, 예시는 순환구조가 아님을 확인할 수 있다. 그리고 위의 코드는 각 과목 간의 선수과목 관계를 hashmap 형태로 정리해준다.

| **course** | **prerequisites** |
|:----------:|:-----------------:|
| 0          | [1, 2]            |
| 1          | [3, 4]            |
| 2          | [ ]               |
| 3          | [4]               |
| 4          | [ ]               |
