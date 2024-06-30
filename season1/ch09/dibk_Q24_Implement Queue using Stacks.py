class MyQueue:
    
    def __init__(self):
        self.obj = []

    def push(self, x: int) -> None:
        self.obj.append(x)

    def pop(self) -> int:
        out = self.obj[0]
        self.obj = self.obj[1:]
        return out

    def peek(self) -> int:
        return self.obj[0]

    def empty(self) -> bool:
        return len(self.obj)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()