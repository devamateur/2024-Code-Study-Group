# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursive_merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.recursive_merge(list1.next, list2)
        return list1        # list1에 merge
    
    def iterative_merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()         # 새로운 연결리스트 new_node, 값을 리턴하는 역할
        current = new_node            # new_node를 가리키는 current, 값을 조작하는 역할

        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1      # head값이 더 작은 연결 리스트와 연결
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 남아있는 원소들을 추가
        if list1:
            current.next = list1
        else:
            current.next = list2
    
        return new_node.next      # new_node를 0으로 초기화했으므로 0을 제외한 next부터 리턴