'''
310. Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/description/

[time] failed
[문제] Tree의 edge 리스트가 주어지면 그 edge들로 만들 수 있는 모든 minimum-height-trees (MHT)의 root를 출력 하는 문제.(https://velog.io/@lychee/LeetCode-310.-Minimum-Height-Trees)
[Note]
- 양방향 그래프(graph)를 생성하고, 리프노드인 노드를 찾기(leaves)
- 
'''

import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# example2
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:              # 노드수가 1 이하이면 0노드 출력
            return [0]

        # 양방향 그래프 구성
        graph = {i:[] for i in range(n+1)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)          # graph : 0:[3],1:[3],2:[3],3:[0,1,2,4],4:[3,5],5:[4]

        # 첫 번째 리프 노드 추가
        leaves = []                     # 노드가 1개의 리프노드를 갖는 경우에만 leaves에 저장
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)        # leaves : 0,1,2,5

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)            # 6(n) - 4(leaves) = 2
            new_leaves = []
            for leaf in leaves:         # 0,1,2,5
                neighbor = graph[leaf].pop()    # graph[0] : [3]
                graph[neighbor].remove(leaf)    # graph[3].remove(0)  >> 3:[1,2,4] >>>

                if len(graph[neighbor]) == 1:   #(leaf:2) graph[3] : [4] >> 
                    new_leaves.append(neighbor)     # new_leaves : [3]

            leaves = new_leaves             # leaves : 4

        return leaves