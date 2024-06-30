class MyQueue:
    
    def __init__(self):
        self.st1 = []         
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        self.peek()          ### peek() 호출해서 st2에 원소 추가. 안하면 st2가 비어있는 경우 runtime error 발생
        return self.st2.pop()

    def peek(self) -> int:
        if not self.st2:           # 초기에 큐가 비어있을 때뿐만 아니라, 중간에 새로운 원소가 push되고 pop할 때 기존에 있던 원소들을 먼저 pop한 뒤 중간에 push된 원소를 pop하도록 함
            for _ in range(len(self.st1)):
                self.st2.append(self.st1.pop())
    
        return self.st2[-1]

    def empty(self) -> bool:
        return len(self.st1) == 0 and len(self.st2) == 0