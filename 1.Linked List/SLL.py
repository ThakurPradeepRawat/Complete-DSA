class Node():
    def __init__(self , data=None , Next = None):
        self.data = data
        self.next = Next

class SinglyLinkedList():
    def __init__(self , node = None):
        self.length = 0
        self.head = node
    def Traverse(self):
        Current = self.head 
        print(self.head)
        while(Current!=None):
            print(Current.data,end="-->")
            Current = Current.next
    def Insert_At_Begining(self):
        Data = int(input("Enter Data That you want to insert at begining "))
        if self.length == 0 :
            self.head = Node(Data)  
            print(self.head)  
            self.length+=1       
        else:
            newNode = Node()
            newNode.data = Data 
            newNode.next = self.head 
            self.head = newNode
            self.length+=1   
    def Insert_At_End(self):
        Data = int(input("Enter Data That you want to insert at End "))
        if self.length == 0 :
            self.head = Node(Data)
            self.length+=1
        else:
            Current = self.head 
            while(Current.next !=None):
                Current = Current.next
            Current.next = Node(Data)
            self.length+=1




           
obj = SinglyLinkedList()
obj.Insert_At_Begining()
obj.Insert_At_Begining()
obj.Traverse()

    
    
