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
        while(Current!=None):
            print(Current.data,end="-->")
            Current = Current.next
    def Insert_At_Begining(self):
        Data = int(input("Enter Data That you want to insert at begining "))
        if self.length == 0 :
            self.head = Node(Data)  
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
    def Insert_At_Position(self):
        pos = int(input("Enter Position where you want to insert Data : - "))
        Data = int(input(f"Enter Data that you want to insert  at {pos}: - "))
        if pos > self.length:
            print("Position out of Linked List")
        elif (pos==1):
            newNode = Node()
            newNode.data = Data
            newNode.next = self.head 
            self.head = newNode
            self.length+=1
        else :
            current = self.head 
            current_next = current.next
            i = 1
            while(i !=pos-1):
                current=current.next
                i+=1
            newNode = Node()
            newNode.data = Data
            newNode.next = current_next.data 
            current.next = newNode

class Menu :
    def Menu(self):
        print("*"*10 , "Menu" , "*"*50)
        menu = """
            1. Insert At Begining 
            2. Insert At End
            3. Insert At Position 
            4. Traverse Linked List
            """
        
    
        obj = SinglyLinkedList()
        
        while(True):
            print(menu)   
            choice = int(input("Choose what you want :- "))
            match choice:
                case 1 :
                    obj.Insert_At_Begining()
                case 2 : 
                    obj.Insert_At_End()
                case 3 :
                    obj.Insert_At_Position()
                case 4:
                    obj.Traverse()
                case _ :
                    break
val = Menu()
val.Menu()



            




    
    
