class Stack:
    def __init__(self,size=None):
        self.stack=[]
        self.size=size
        self.top=-1
        
    def length(self):
        return len(self.stack)
        
    def is_full(self):
        if len(self.stack) == self.size:
            return True
        return False
        
    def is_empty(self):
        if self.top == -1:
            return True
        return False
        
        
    def push(self,value):
        if not self.is_full():
            self.stack.append(value)
            self.top += 1
        else:
            print("the stack is full you cannot push elements")
        
    def pop(self):
        if not self.is_empty():
            self.top-=1
            self.stack.pop()
        else:
            print("the stack is empty you cannot pop element")
        
    def peek(self):
        return self.stack[self.top]

print("stack 1")        
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.peek())
stack1.pop()
print(stack1.peek())

print("\n\n")
print("stack 2")
stack2 = Stack(3)
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
print(stack2.peek())
stack2.pop()
print(stack2.peek())
stack2.push(4)
print(stack2.peek())
        
        
