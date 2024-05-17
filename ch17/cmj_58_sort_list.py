# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        to_list = []

        while head:
            to_list.append(head.val)
            head = head.next

        to_list.sort()
        sorted_nodes = ListNode(None)
        result = sorted_nodes

        for item in to_list:
            sorted_nodes.next = ListNode(item)
            sorted_nodes = sorted_nodes.next

        return result.next