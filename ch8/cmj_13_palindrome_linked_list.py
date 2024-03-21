# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        result = []    # 연결 리스트의 원소를 저장
        
        while head.next:
            result.append(head.val)
            head = head.next
        result.append(head.val)

        if result == result[::-1]:
            return True