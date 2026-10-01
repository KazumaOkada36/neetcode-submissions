class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack2 and val<=self.stack2[-1]:
            self.stack2.append(val)
        elif len(self.stack2) == 0:
            self.stack2.append(val)

        

    def pop(self) -> None:
        june = self.stack.pop()
        if june == self.stack2[-1]:
            self.stack2.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        bro = self.stack2.pop()
        self.stack2.append(bro)
        return bro

        
