# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외 처리
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):  ## 이해가 안돼요
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next
    
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 구간 길이가 0인 경우 그냥 리턴
        if left == right:
            return head

        curr = head
        front = head        # 왼쪽 부분의 head
        count = 1
        left_count = 1
        
        while count < left:
            curr = curr.next
            count += 1
            left_count += 1

        # left부터 right reverse
        prev = None
        while count <= right and curr:
            next_node, curr.next = curr.next, prev
            prev, curr = curr, next_node
            count += 1

        result = prev

        # 오른쪽 원소들과 연결
        while prev and prev.next:
            prev = prev.next
        prev.next = next_node

        if left > 1:
            left_front = front
            while left > 2 and front and front.next:
                left -= 1
                front = front.next

            front.next = result        # 왼쪽 원소들과 연결
            return left_front

        return result