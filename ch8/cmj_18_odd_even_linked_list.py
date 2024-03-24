# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd_pointer = head
        even_pointer = head.next

        even_head = head.next        #### 짝수번째 노드의 헤드를 기억

        while even_pointer and even_pointer.next:
            odd_pointer.next, even_pointer.next = odd_pointer.next.next, even_pointer.next.next
            odd_pointer = odd_pointer.next
            even_pointer = even_pointer.next
        
        # 홀수번째 노드와 연결
        odd_pointer.next = even_head

        return head