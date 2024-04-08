# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val         # 앞 뒤 값을 교체
            node = node.next.next           # 두 칸씩 뜀

        return head