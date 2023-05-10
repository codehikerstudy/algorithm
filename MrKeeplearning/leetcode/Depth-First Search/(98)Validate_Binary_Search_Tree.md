# Leetcode 98번 validate binary search tree 해설

1. BST의 조건에 부합하는지 확인하는 문제이기 때문에 각 노드는 BST의 성립조건에 맞도록 알맞은 범위 내에 속해 있어야 한다. 예를 들어 root인 `5`는 어떤 숫자이든 와도 상관없는 자리이다. 따라서 왼쪽 서브트리의 루트는 음의 무한대보다 크고 5보다 작은 수가 와야 하고, 오른쪽 서브트리의 루트는 5보다 크고 양의 무한대보다 작은 수가 와야 한다.
2. 재귀를 사용해서 모든 노드들이 BST 조건이 성립할 수 있는 범위 내에 있는 숫자인지 확인한다.

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/231400213-5f5d2fd9-f430-4e62-b9e0-89446dc98629.png"
</p>
