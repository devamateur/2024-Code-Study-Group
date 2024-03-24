# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/
# time : 1tl 48분~

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next : return head

        trigger = 1
        p = ans = ListNode()
        rev = None

        while trigger <= right :
            if trigger < left :
                p.next, head = head, head.next
                p = p.next
            
            else :
                _, head.next = head.next, rev
                rev = head
                head = _

            trigger +=1

        ans = ans.next
        ans.next =rev
        while rev.next :
            rev = rev.next
        rev.next = head

        return ans
    
'''
Solution ::
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next : return head

        p = start = ListNode()
        p.next = head

        for _ in range(left-1):
            start = start.next
        end = start.next

        for _ in range(right-left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return p.next
'''