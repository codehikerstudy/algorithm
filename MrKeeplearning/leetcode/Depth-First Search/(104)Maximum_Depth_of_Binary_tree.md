# Leetcode 104. Maximum Depth of Binary Tree 풀이

## 1. 트리 예시를 통한 DFS 과정 살펴보기

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/231770246-25595253-e15d-4004-9497-4b2462f72b12.png">
</p>

스택에 삽입되는 요소는 `(현재 노드의 value, 현재 depth)` 가 된다.

### Step1.

* stack: [(3, 1)]
* max_depth = 1

### Step2.

stack: [(9, 2), (20, 2)]
* pop() -> (3, 1)
* max_depth = 2

### Step3.

* stack: [(9, 2), (15, 3), (7, 3)]
* pop() -> (20, 2)
* max_depth = 3

### Step4.

* stack: [(9, 2), (15, 3)]
* pop() -> (7, 3)
* max_depth = 3

### Step5.

* stack: [(9, 2), (4, 4)]
* pop() -> (15, 3)
* max_depth = 4

### Step6.

* stack: [(9, 2)]
* pop() -> (4, 4)
* max_depth = 4

### Step7.

* stack: []
* pop() -> (9, 2)
* max_depth = 4

## 2. Solution2 관련

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/231775508-6f51b683-101f-4a68-a537-4504e9920d86.png">
</p>

현재 노드가 루트 노드인 3일 때, 왼쪽 서브트리의 최대 깊이는 1이고 오른쪽 서브트리의 최대 깊이는 3이다.

왼쪽 서브트리와 오른쪽 서브트리 중 가장 큰 값은 오른쪽 서브트리의 depth인 3이고 현재 노드인 3의 depth는 1이기 때문에 이 둘을 더한 4가 주어진 트리의 최대 깊이가 된다.
