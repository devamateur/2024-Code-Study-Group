'''
148. Sort List
https://leetcode.com/problems/sort-list/

[time] 10m
[문제] 연결리스트를 n log n 정렬하기
[풀이방식]
- 연결리스트를 리스트로 바꾸고 sort함수 사용하여 정렬, 다시 연결리스트로 변환
    - sort(), sorted() : NlogN
    - 퀵, 병합 정렬 : NlogN
- 병렬 정렬 :
    - 런너 기법을 활용하여 연결리스트의 중간을 찾고(half), 두 연결리스트를 비교해서 반환
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        while head :
            nodeList.append(head.val)
            head = head.next
        
        nodeList.sort()
        node = root = ListNode()
        for n in nodeList :
            new = ListNode(n)
            node.next = new
            node = node.next
        
        return root.next
    
# solution
class Solution:
    def mergeTwoLists(self, node1: ListNode, node2: ListNode) -> ListNode:
        if node1 and node2:
            if node1.val > node2.val:
                node1, node2 = node2, node1
            node1.next = self.mergeTwoLists(node1.next, node2)

        return node1 or node2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head and not head.next:
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)