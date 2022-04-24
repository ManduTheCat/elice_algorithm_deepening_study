class Rotate_Q:
    def __init__(self, n):
        self.n = n
        self.data = list(range(1, self.n+1))
        self.count = 0

    def print_Q(self):
        print(self.data)

    def print_count(self):
        print(self.count)

    def pop(self):
        self.data.pop(0)

    def left(self):
        self.data.append(self.data.pop(0))
        self.count += 1

    def right(self):
        self.data.insert(0, self.data.pop())
        self.count += 1

    def rotate(self, pos):
        if self.data.index(pos)==0:
            self.pop()

        elif self.data.index(pos) <= len(self.data)//2:
            while(pos in self.data):
                self.left()
                if(self.data.index(pos)==0):
                    self.pop()
                    break
        else:
            while(pos in self.data):
                self.right()
                if(self.data.index(pos)==0):
                    self.pop()
                    break

N, M = map(int, input().split())
position = list(map(int, input().split()))
myQ = Rotate_Q(N)

for pos in position:
    myQ.rotate(pos)

myQ.print_count()