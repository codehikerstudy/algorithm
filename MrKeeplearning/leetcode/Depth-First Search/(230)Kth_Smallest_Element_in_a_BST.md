# Leetcode 230. Kth Smallest Element in a BST 풀이

## 1. 기본 아이디어
가장 왼쪽에 있는 BST 내에서 가장 작은 값까지 우선 탐색 후 inorder traversal 순서대로 역으로 탐색하며 k번째로 작은 값을 찾아낸다.

## 2. Line by Line

```python
while current_node:
    stack.append(current_node)
    current_node = current_node.left
```
처음 가장 작은 값을 탐색하기 위해서, 왼쪽 최하단 자식노드까지 탐색한다. 그리고 이 때, 왼쪽 최하단 자식노드가 NULL을 만나게 되면 역순으로 되돌아가면서 k번째로 작은 값을 찾아야 하는데, 이를 위해서 stack에 계속해서 지나간 노드들을 삽입한다.

---

```python
        while current_node or stack:
            # 현재 노드가 null이 아닐 때까지 왼쪽 자식 노드를 탐색한다.
            # k번째로 작은 값을 찾기 위해서는 방문했던 노드로 다시 돌아가야 하기 때문에
            # stack에 방문했던 노드들을 삽입한다.
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            count += 1
            if count == k:
                return current_node.val
            current_node = current_node.right
```

위의 전체 코드의 핵심에 대한 해설은 아래의 필기를 참고하자.

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/232504502-54209fc9-a572-442f-80d4-41e707f85b67.png">
</p>
