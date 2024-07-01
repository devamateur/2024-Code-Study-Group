# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next : return True
        
        # 앞뒤 비교를 위한 노드
        new_nodes = None
        # 움직이는 포인터
        left,right = head, head
        
        # new_nodes에 역순을 넣기 위한 작업
        # 러너 기법 : 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법으로, 한 포인터(right)가 앞서게 나아가 맨 끝에 도달할 때 다른 포인터(left)가 중간 위치에 도달함
        
        while right and right.next:
            # right은 여기서 이동하는 역할에 불과함.
            right = right.next.next
            
            # 노드를 항상 앞에 추가하기 때문에 먼저 입력된 노드는 점점 뒤에 위치하게 됨
            # left는 new_nodes와 같이 이동
            new_nodes, new_nodes.next, left = left, new_nodes, left.next

        # 입력된 연결리스트가 홀수인 경우, left를 한 번 더 움직이기
        if right :
            left = left.next
        
        # 펠린드롬 비교하기 : left와 비교했을 때, new_node가 끝까지 이동했다면, new_node에 빈값이 남아서 True
        while new_nodes and new_nodes.val == left.val :
            left, new_nodes = left.next, new_nodes.next
        
        return not new_nodes
    
'''
#solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next : return True

        node_dque : Deque = collections.deque() 
    
        while head :
            node_dque.append(head.val)
            head =head.next
        
        while len(node_dque) > 1 :              # while node_deque : ---> 홀수일 경우, 문제가 됨.
            if node_dque.pop() != node_dque.popleft():
                return False
        
        return True
'''