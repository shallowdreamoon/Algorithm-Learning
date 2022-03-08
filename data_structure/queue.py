class Queue:
    def __init__(self,maxsize=100):
        self.queue=[0 for _ in range(maxsize)]
        self.size=maxsize
        self.front=0  #队首指针
        self.rear=0   #队尾指针
    def push(self,element):
        if not self.is_filled():
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
        else:
            raise IndexError("Queue is filled. ")
    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty. ")
    def is_empty(self):
        return self.front==self.rear
    def is_filled(self):
        return (self.rear+1)%self.size==self.front

queue=Queue(5)
for i in range(4):
    queue.push(i)

print(queue.pop())
print(queue.pop())
print(queue.pop())