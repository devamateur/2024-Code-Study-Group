class MyCircularQueue:
    
    def __init__(self, k: int):
        self.len = k
        self.q = [0]*k
        self.front = self.q[0]
        self.rear = self.q[0]
        
    # 앞에서부터 입력
    def enQueue(self, value: int) -> bool:
        for i in range(self.len) :
            if not self.q[i] :
                self.q[i] = value
                self.rear = value
                return True
        return False

    # 앞에서부터 삭제
    def deQueue(self) -> bool:
        for i in range(self.len):
            if self.q[i] :
                self.q[i] = 0
                self.front = self.q[i+1]
                return True
        return False
        
    def Front(self) -> int:
        return self.fornt
        

    def Rear(self) -> int:
        return self.rear
        

    def isEmpty(self) -> bool:
        return len(self.q)==0
        

    def isFull(self) -> bool:
        return all(self.q)
        # all(iterble)
        # 모두 양수여야 True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()