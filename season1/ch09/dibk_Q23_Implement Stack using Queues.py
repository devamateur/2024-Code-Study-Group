'''
time : 5m
top과 pop을 반대로 이해했다.
top은 마지막에 입력된 값을 확인
pop은 마지막에 입력된 값을 확인하며, 제거
'''

class MyStack:
    
    def __init__(self):
        self.obj = []
        

    def push(self, x: int) -> None:
        self.obj.append(x)

    def pop(self) -> int:
        out = self.obj[-1]
        self.obj = self.obj[:-1]
        return out
        

    def top(self) -> int:
        return self.obj[-1]
        

    def empty(self) -> bool:
        return len(self.obj)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()