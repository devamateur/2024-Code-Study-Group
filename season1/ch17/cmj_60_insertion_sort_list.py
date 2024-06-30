# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 리스트 변환
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        result = node
        to_list = []

        while head:
            to_list.append(head.val)
            head = head.next

        # 삽입정렬
        for i in range(1, len(to_list)):
            for j in range(i, 0, -1):
                if to_list[j-1] > to_list[j]:
                    to_list[j-1], to_list[j] = to_list[j], to_list[j-1]
        
        for num in to_list:
            node.next = ListNode(num)
            node = node.next

        return result.next

    # 연결 리스트 자체 정렬
    def insertionSortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        back = head 
        front = head.next 

        head_size = 0    # 연결 리스트 사이즈 -1

        # 큰 값 하나를 뒤로 이동
        while front:
            if back.val > front.val:
                back.val, front.val = front.val, back.val 
            back = back.next 
            front = front.next 
            head_size += 1

        # 삽입정렬
        for _ in range(head_size): 
            back = head 
            front = head.next 

            while front:
                if back.val > front.val:
                    back.val, front.val = front.val, back.val 
                back = back.next 
                front = front.next

        return head