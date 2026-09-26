class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtend(self,data):
        newnode=Node(data)
        temp = self.head
        if temp == None:
            self.head = newnode
        else:
            while temp.next != None:
                temp=temp.next
            temp.next=newnode
            newnode.prev = temp
            
    def insertAtstart(self, data):
            newnode=Node(data)
            temp = self.head
            if temp == None:
                self.head = newnode
                return
            newnode.next=temp
            self.head =newnode
            temp.prev=newnode
            
    def insertNextTo(self,value,nextto):
        newnode=Node(value)
        temp = self.head
        while temp.data != nextto:
            temp = temp.next
        newnode.next=temp.next
        temp.next = newnode
        newnode.prev = temp
        newnode.next.prev = newnode
    
    def delete(self,value):
        temp = self.head 
        while temp.data !=value:
            temp=temp.next
        if temp.prev == None:
            self.head = temp.next
            temp.next=None
            self.head.prev=None
            return
        if temp.next==None:
            temp.prev.next=None
            temp.prev=None
            return
        temp.prev.next = temp.next
        temp.next.prev=temp.prev
        temp.prev = None
        temp.next = None
            
        
        
    def display(self):
        temp=self.head
        while temp.next != None:
            print(temp.prev)
            print(temp.data)
            print(temp.next)
            temp=temp.next
        print(temp.prev)
        print(temp.data)
        print(temp.next)
        
    
        
dll=DoublyLinkedList()
dll.insertAtstart(3)
dll.insertAtend(4)
dll.insertAtend(6)
dll.insertAtstart(2)
dll.insertAtend(8)
dll.insertNextTo(5,4)
dll.delete(5)

dll.display()