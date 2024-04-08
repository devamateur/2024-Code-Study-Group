# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 결과를 저장할 노드 ans
        ans = None

        while head :
            # head.next를 ans로 연결
            # 진짜 head.next는 _로 복사
            _, head.next = head.next, ans
            
            ans = head      # 1-None,   2-1-None,   ...
            head = _

        return ans