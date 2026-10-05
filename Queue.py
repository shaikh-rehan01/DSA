class Queue:
    def __init__(self,size=None):
        self.queue=[]
        self.size = size
        self.front=-1
        self.rear=-1
        
    def enque(self,value):
        if len(self.queue) == 0:
            self.front +=1
            self.rear +=1
            self.queue.append(value)
        elif len(self.queue)==self.size:
            print(" the queue is full cannot push value")
        else:
            self.rear += 1
            self.queue.append(value)
            
    def dequeue(self):
        if len(self.queue)==0:
            print(" the queue if empty cannot be pop value")
        else:
            value = self.queue.pop(self.front)
            self.front +=1
            return value
            
    def peek(self):
            return self.queue[self.front]
            
    def display(self):
        print(self.queue)
            
queue = Queue()
queue.enque(1)
queue.enque(2)
queue.display()
print(queue.dequeue())
queue.display()
            
            

            
