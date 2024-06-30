# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 리스트로 바꿔서 sort()를 이용하는 꼼수
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        to_list = []

        # 연결 리스트를 리스트로 변환
        while head:
            to_list.append(head.val)
            head = head.next

        # 오름차순 정렬
        to_list.sort()

        sorted_nodes = ListNode(None)
        result = sorted_nodes

        # 정렬된 리스트를 다시 연결리스트로 변환
        for item in to_list:
            sorted_nodes.next = ListNode(item)
            sorted_nodes = sorted_nodes.next

        return result.next