class Stack():
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack.pop())

    def size(self):
        print(len(self.stack))

    def empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[-1])

myStack = Stack()
orders = [input().split() for _ in range(int(input()))]

for order in orders:
    if order[0] == 'push':
        myStack.push(int(order[1]))
    elif order[0] == 'pop':
        myStack.pop()
    elif order[0] == 'size':
        myStack.size()
    elif order[0] == 'empty':
        myStack.empty()
    elif order[0] == 'top':
        myStack.top()
