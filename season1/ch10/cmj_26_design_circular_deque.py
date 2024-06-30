class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [0]*k
        self.pointer = 0
        self.count = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.pointer = (self.pointer-1)%self.max_size
        self.deque[self.pointer] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.last = (self.pointer+self.count)%self.max_size
        self.deque[self.last] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.pointer = (self.pointer+1)%self.max_size
        #self.deque[self.pointer] = 0
        self.count -= 1
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        #self.deque[self.pointer] = 0
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.pointer]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.pointer+self.count-1)%self.max_size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.max_size
    
    
    '''def __init__(self, k: int):
        self.deque = []
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.max_size:
            self.deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.max_size:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.max_size'''

