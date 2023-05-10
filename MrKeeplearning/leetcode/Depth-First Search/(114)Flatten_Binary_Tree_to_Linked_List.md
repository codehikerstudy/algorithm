# Leetcode 114. Flatten Binary Tree to Linked List 풀이

<p align="center">
<img src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" width="600">
</p>

## 1. 핵심 아이디어

주어진 트리를 연결리스트로 만들 때 만약 왼쪽과 오른쪽 서브트리가 둘 다 비어 있다면 아무런 조치를 취하지 않아도 좋다.

왜냐하면, 단 하나의 루트노드만으로 이미 연결리스트가 만들어진 상태이기 때문이다.

그리고 오른쪽 서브트리만 비어 있다면 왼쪽 서브트리의 모든 노드들을 prorder traversal에 맞게 연결리스트로 만들어준 뒤 그대로 오른쪽 서브트리로 옮겨주어야 한다.

반면, 왼쪽 서브트리만 비어 있고 오른쪽 서브트리만 있다면 특별히 조치할 일이 없다(단, 위의 그림 기준이고 오른쪽 서브트리의 왼쪽 자식 포인터가 모두 null인 경우에만 특별히 조치할 일이 없는 것).

## 2. if문 이해하기

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/232210706-4d4e81bf-1a99-44b3-b236-bd7478aa9fea.png">
</p>

```python
if root.left:
    left_tail.right = root.right
    root.right = root.left
    root.left = None
```

주어진 트리의 왼쪽 서브트리에 해당하는 위의 이미지를 기준으로 위의 코드를 살펴보자.

`root`는 2를 가리키고 있고, 현재 빈 노드가 아니다. 이 때 `left_tail`은 3을 가리키고 있고 연결리스트로 만들기 위해서는 오른쪽 자식 포인터(`left_tail.right`)는 기존 `root`의 오른쪽 노드와 연결되어야 한다.

그리고 `root`의 오른쪽 포인터는 기존에 4를 가리키고 있지만 연결리스트 형태로 바꾸는 중이기 때문에 기존 `root`의 왼쪽 자식노드(`root.left`)를 가리켜야 한다.

마지막으로 위의 일련의 작업들을 거친 뒤 `root`의 왼쪽 포인터는 null을 가리켜야 하기 때문에 `root.left = None`으로 처리해준다.
