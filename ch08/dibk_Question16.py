# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_function(self, head: Optional[ListNode]):
        '''
        ListNode를 string값으로 저장해서 역순하고 정수화해서 반환하기
        
        example :
        - head = 2-4-3
        '''
        out = ''

        while head :
            out += str(head.val)        # int 2,    int 4,  int 3
            head = head.next

        return int(out[::-1])   # int : 342

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        int_out1 = self.reverse_function(l1)
        int_out2 = self.reverse_function(l2)

        list_out =list(str(int_out1+int_out2))
        
        p = result = ListNode()

        for comp in list_out[::-1] :
            p.next = ListNode(comp)
            p = p.next

        return result.next


