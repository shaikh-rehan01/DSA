class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next=next
        
class SLL:
    def __init__(self,head=None):
        self.head=head
        
    def insertAtend(self,data):
        newnode=Node(data)
        
        if self.head != None:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode
        else:
            self.head=newnode
            
    def insertAtstart(self,data):
            newnode=Node(data)
            newnode.next = self.head
            self.head = newnode
                
    def insertAtmiddle(self,data,position):
            newnode=Node(data)
            n=1
            temp = self.head
            while n!=position:
                temp=temp.next
                n+=1
            newnode.next=temp.next
            temp.next = newnode
                
    def insertNextTo(self,data,nextto):
        newnode=Node(data)
        temp=self.head
        while temp.data != nextto:
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
        
    def delete(self,value):
        temp = self.head
        if temp.data == value:
            self.head = temp.next
            temp.next = None
        else:
            while temp.next.data != value:
                temp=temp.next
            p = temp.next
            temp.next=temp.next.next
            p.next=None
    
    def display(self):
        temp=self.head
        while temp.next != None:
            print(temp.data)
            temp=temp.next
        print(temp.data)
        
n1 = SLL()
n1.insertAtend(4)
n1.insertAtend(5)
n1.insertAtend(6)
n1.insertAtstart(3)
n1.insertAtmiddle(7,2)
n1.insertNextTo(8,5)
n1.delete(4)
n1.display()

