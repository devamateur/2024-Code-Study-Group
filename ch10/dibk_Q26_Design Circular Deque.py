'''
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/description/
[문제] 원형 데크 디자인

time : failed
'''

# Solution01 :
class MyCircularDeque:
    
    def __init__(self, size: int):
        self.deque = []
        self.size = size

    def insertFront(self, value: int) -> bool:
        if len(self.deque) != self.size:
            self.deque.insert(0, value)         # index 0에 value값 추가
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) != self.size:
            self.deque.append(value)            # 뒤에 추가
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.deque) != 0:
            self.deque.pop(0)                   # 0인덱스 값 pop
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.deque) != 0:
            self.deque.pop()                    # 맨뒤값 pop
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.deque) != 0:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.deque) != 0:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.size
    
#-------------------------------------------------------------------------------------------    
# Solution 02 
# 교재 답
class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None
        
class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.size = k
        self.count = 0
        self.head.prev, self.tail.next = self.tail, self.head       # head의 앞을 tail과 연결하고, tail의 뒤를 head와 연결하여 원형모양 생성

    # 앞에 추가        
    def insertFront(self, value: int) -> bool:
        if self.count == self.size: return False
        self.count += 1
        
        node = ListNode(value)          # 추가할 노드
        tmp_node = self.head.prev       # head의 앞 정보를 임시 저장하는 tmp노드
        
        self.head.prev = node           # head앞에 노드 추가
        node.next, node.prev = self.head, tmp_node  # 노드의 뒤는 head, 노드의 앞은 tmp 설정
        tmp_node.next = node                        # 연결
        
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.size: return False
        self.count += 1
        
        node = ListNode(value)          # 추가할 노드
        tmp_node = self.tail.next       # tail 뒤 정보를 임시 저장하는 tmp노드
        
        self.tail.next = node           
        node.prev, node.next = self.tail, tmp_node  
        tmp_node.prev = node                       
        
        return True

    def deleteFront(self) -> bool:
        if self.count == 0: return False
        self.count -= 1
        
        tmp = self.head.prev.prev           # tmp head의 앞의 앞 노드
        self.head.prev = tmp                
        tmp.next = self.head
        return True

    def deleteLast(self) -> bool:
        if self.count == 0: return False
        self.count -= 1
        
        tmp = self.tail.next.next
        self.tail.next = tmp
        tmp.prev = self.tail
        return True

    def getFront(self) -> int:
        return self.head.prev.val if self.count else -1

    def getRear(self) -> int:
        return self.tail.next.val if self.count else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size