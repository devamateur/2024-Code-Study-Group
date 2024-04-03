class MyCircularQueue:
    
    def __init__(self, k: int):
        self.q = [None] * k
        self.q_len = k
        self.front_pointer = 0         # 앞 원소를 가리키는 포인터
        self.rear_pointer = 0          # 뒤 원소를 가리키는 포인터

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear_pointer] is None:          # 포인터가 가리키는 큐가 비어있을 때
            self.q[self.rear_pointer] = value
            print(self.rear_pointer, self.q[self.rear_pointer])
            self.rear_pointer = (self.rear_pointer+1) % self.q_len       # rear pointer 이동
            return True
        return False

    def deQueue(self) -> bool:
        if self.q[self.front_pointer] is not None:
            self.q[self.front_pointer] = None
            self.front_pointer = (self.front_pointer+1)%self.q_len       # front pointer 이동
            return True
        return False
        
    def Front(self) -> int:
        if self.q[self.front_pointer] is not None:
            return self.q[self.front_pointer]
        return -1

    def Rear(self) -> int:
        if self.q[self.rear_pointer-1] is None:
            return -1
        
        return self.q[self.rear_pointer-1]

    def isEmpty(self) -> bool:
        return self.front_pointer == self.rear_pointer and self.q[self.front_pointer] is None      # 초기상태 혹은 deque를 많이 해서 빈 경우

    def isFull(self) -> bool:
        return self.front_pointer == self.rear_pointer and self.q[self.front_pointer] is not None
    
'''
76 ms

class MyCircularQueue:
    
    def __init__(self, k: int):
        self.q = []
        self.q_len = k                     # 큐의 크기
        self.rear_pointer = 0              # rear 위치

    def enQueue(self, value: int) -> bool:
        if len(self.q) < self.q_len:
            self.q.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.q) > 0:
            self.q.pop(0)
            return True
        return False

    def Front(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if not self.q:
            return -1
        self.rear_pointer = 0
        while self.rear_pointer < len(self.q): 
            self.rear_pointer += 1
        return self.q[self.rear_pointer-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.q_len
'''