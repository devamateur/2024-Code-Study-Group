# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Linked List는 len()함수를 못쓰는구나

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head

        pointer = output = ListNode()
        
        # head = [1,2,3,4]
        while head and head.next :
            prve,after = None,None
            
            after, _, head.next = head.next, head.next.next, prve       # after : 2-3-4,    _ : 3-4,    head.next : None -> head : 1-None
            prve =  head                                                # prve : 1-None
            after.next =  prve                                          # after.next = 1-None,  after : 2-1-None
            head = _

            pointer.next = after                                        # pointer.next : 2-1-None --> pointer : 0-2-1-None
            pointer = pointer.next.next                                 # pointer 움직여서, 1-None

        # head가 홀수인 경우 마지막 값을 넣어줌
        pointer.next = head if head else None                           # if head : [1,2,3]인 경우, while문에서 head는 3-None이 되는 순간 break
                                                                        # head는 값이 남아있고, 마지막 노드를 pointer에 저장
        
        return output.next
        
