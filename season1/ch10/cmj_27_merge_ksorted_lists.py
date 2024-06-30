# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_list = []
        result = []
        for node in lists:
            while node:
                heapq.heappush(my_list, node.val)
                node = node.next

        ### heappop은 heapq에서 가장 작은 값을 가져오므로 이 값을 append하면 오름차순 정렬
        while my_list:
            result.append(heapq.heappop(my_list))

        result_node = ListNode()
        result_head = result_node

        while result:
            left = ListNode(result.pop(0))
            result_node.next = left
            result_node = result_node.next
            
        return result_head.next