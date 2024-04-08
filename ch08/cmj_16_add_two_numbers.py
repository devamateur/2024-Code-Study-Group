# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        quo = 0         # 몫
            
        next_node = l1
        
        while p or q or quo:
            sum_ = 0
            x = p.val if p else 0
            y = q.val if q else 0

            sum_ = x+y + quo
            quo = (x+y+quo)//10

            if quo > 0:        # 몫이 있으면 현재 노드의 val을 나머지값으로 갱신
                next_node.val = sum_%10
            else:
                next_node.val = sum_

            p = p.next if p else None
            q = q.next if q else None
            
            if p==None and q==None and quo==0:      # 연결 리스트가 모두 None인데 몫도 없으면 break
                break
            next_node.next = ListNode(quo)         # 몫이 있거나, 연결 리스트가 둘 중 하나라도 존재하는 경우
            next_node = next_node.next

        return l1