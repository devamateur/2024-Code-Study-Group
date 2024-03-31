class MyStack:
    def __init__(self):
        self.q1 = []       # push하는 큐
        self.q2 = []       # pop하는 큐

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.q2 = self.q1[::-1]        # pop 하는 큐는 기존 큐의 역순, 맨 앞 원소가 스택의 맨 위가 됨

    def pop(self) -> int:
        pop_item = self.q2.pop(0)      # 맨 앞 원소(여기서는 스택의 top)를 pop
        self.q1 = self.q2[::-1]        # pop한 내용을 q1에도 저장
        return pop_item

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return len(self.q2) == 0
