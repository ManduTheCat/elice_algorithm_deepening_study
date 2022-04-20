class Queue():
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue.pop(0))

    def size(self):
        print(len(self.queue))

    def empty(self):
        if len(self.queue) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[-1])

    def back(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])

myQueue = Queue()

orders = [input().split() for _ in range(int(input()))]

for order in orders:
    if order[0] == 'push':
        myQueue.push(int(order[1]))
    elif order[0] == 'pop':
        myQueue.pop()
    elif order[0] == 'size':
        myQueue.size()
    elif order[0] == 'empty':
        myQueue.empty()
    elif order[0] == 'front':
        myQueue.front()
    elif order[0] == 'back':
        myQueue.back()

