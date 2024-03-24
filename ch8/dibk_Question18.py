# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/description/
# time : 20m

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head
        
        odd = result = ListNode()       # 홀수값만 저장하며 나중에 결과값을 만들 변수
        even = tmp = ListNode()         # 짝수값만 저장

        # head = 1-2-3-4-5
        while head and head.next :
            odd.next, even.next = head, head.next       # odd.next : 1-{2-3-4-5}, even.next : 2-{3-4-5}
            head = head.next.next                       # head : 3-{4-5}
            odd, even = odd.next, even.next             # odd : 1-{2-3-4-5}, even : 2-{3-4-5}           -> result : 0-1-{2-3-4-5}, tmp : 0-2-{3-4-5}
                                                        # while문 :
                                                            # odd.next : 3-{4-5}, even.next : 4-{5}
                                                            # head : 5-None
                                                            # odd : 3-{4-5}, even : 4-{5}           -> result : 0-1-3-{4-5}, tmp = 0-2-4-{5}
                                                        # break --> head가 5-None
        # head가 홀수인 경우 마지막 노드가 남음
        if head :
            odd.next = head                             # odd : 3-{4-5}, odd.next : {4-5} ---> odd.next = {5-None}, odd = 3-{5-None}
            even.next = None                            # even : 4-{5-None} --> even : 4-None
            odd = odd.next                              # odd 움직이기 : odd : 5-{None}

        odd.next = tmp.next                             # odd = 5-{None} --> odd = 5-{2-4-None}

        return result.next
