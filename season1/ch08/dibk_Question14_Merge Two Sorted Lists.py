# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2 : return list1 if list1 else list2

        # ans 노드를 움직일 pointer
        pointer = ans = ListNode()

        while list1 and list2 :
            if list1.val < list2.val :
                pointer.next,list1 = list1,list1.next

            else :
                # list1.val >= list2.val 
                pointer.next,list2 = list2,list2.next

            # pointer 움직이기
            pointer = pointer.next
            
        # 마지막 남은 값 입력
        pointer.next = list1 or list2
        
        # ans 노드 생성시, 초기값 val = 0 
        return ans.next
        
