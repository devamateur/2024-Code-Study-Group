'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/submissions/1229940676/

[문제] k개의 정렬된 연결리스트를 1개의 정렬된 연결리스트로 병합하라
time : 10m
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        tmp = []
        for listnode in lists :

            while listnode :
                tmp.append(listnode.val)
                listnode = listnode.next
        
        tmp.sort()
        tail = head = ListNode()

        for component in tmp:
            tail.next = ListNode(component)
            tail = tail.next

        return head.next
    
    
#----------------------------------------------------------------------------------------
# Solution

import heapq
from typing import List
## 파이썬에 내장된 자료구조에 대한 타입을 명시해야 할 때가 있다.
## 이 때 typing 모듈에서 제공하는 List, Dict, Tuple, Set를 사용하면 원소의 타입까지 명시해줄 수 있다.
# ex) nums: List[int] = [1, 2, 3]
# ex) user: Tuple[int, str, bool] = (3, "Dale", True)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):                                     # i : 0,1,2
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))   # heapq.heappush(원소를 추가할 대상, 추가할 원소)
                                                                    # heapq.heappush(리스트:heap, 튜플:추가할 원소)
        while heap:
            node = heapq.heappop(heap)                              # node : 튜플:(값, 인덱스, 노드)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next