""" Implementation of Stack using Linked List"""

class Node:
    def __init__(self , data):
        self.data = data 
        self.next = None
class Stack:
    def __init__(self):
        self.head = None 
        self.top = -1
    def Push(self , data):
        new_node = Node(data)
        if self.top==-1:
            self.head = new_node 
            self.top+=1
            return
        new_node.next  = self.head 
        self.head = new_node 
        self.top+=1
    def Pop(self):
        if(self.top==-1):
            print("Stack is Empty")
            return 
        self.head = self.head.next 
        self.top-=1 
    def Top(self):
        if(self.top==-1):
            print("Stack is Empty")
            return 
        print("Top of the stack is :- " , self.head.data)
ss = Stack()
ss.Top()
ss.Push(10)
ss.Top()
ss.Pop()
ss.Top()


    
        
    
        



    