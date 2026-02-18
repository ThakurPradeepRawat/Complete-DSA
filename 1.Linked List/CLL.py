class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
    def Traverse(self):
        if(self.head is None):
            print("None")
            return
        print(self.head.data , end="<==>")
        current = self.head.next 
        while(current!=self.head):
            print(current.data,end="<==>")
            current = current.next
        print("Head")
    def Insert_At_Begin(self):
        Data = int(input("Enter data :- "))
        newNode = Node(Data)
        if(self.head is None):
            self.head = newNode 
            newNode.next = self.head 
            self.tail = newNode
            self.length +=1 
            print("Data inserted at begining")
            return 
        newNode.next = self.head 
        self.head = newNode
        self.tail.next = self.head
        self.length+=1
        print("Data inserted at begining")
    def Insert_At_End(self):
        Data = int(input("Enter Data :- "))
        newNode = Node(Data)
        if self.head is None :
            self.head = self.tail = newNode 
            self.tail.next = self.head 
            self.length +=1
            print('Data insert at end ')
            return 
        newNode.next = self.head
        self.tail.next = newNode 
        self.tail = newNode 
        self.length+=1 
        print('Data inserted at end')
    def Delete_From_Begin(self):
        if(self.head is None):
            print("CLL is Empty")
            return 
        if (self.length == 1):
            self.head =  self.tail = None
            self.length-=1
            print("Data deleted from begining")
            return 
        self.tail.next = self.head.next  
        self.head = self.head.next
        self.length -=1 
        print("Data deleted from begining")
       
    def  Delete_From_End(self):
        if(self.head is None):
            print("CLL is empty")
            return 
        if(self.length == 1):
            self.head = self.tail = None 
            self.length -=1 
            print("Data deleted from End ")
            return 
        current = self.head 
        while(current.next != self.tail):
            current = current.next 
        self.tail = current 
        self.tail.next = self.head 
        self.length -=1 
        print("Data deleted from end ")
    
class Menu :
    def run(self):
        CLL = CircularLinkedList()
        while True:
            print("\n" + "*" * 20 + " MENU " + "*" * 20)
            print("""
1. Insert at Beginning
2. Insert at End
3. Traverse
4. Delete from Beginning
5. Delete from End
6. Exit
""")
            choice = int(input("Enter your choice: "))
            match(choice):
                case 1:
                    CLL.Insert_At_Begin()
                case 2:
                    CLL.Insert_At_End()
                case 3:
                    CLL.Traverse()
                case 4 :
                    CLL.Delete_From_Begin()
                case 5 :
                    CLL.Delete_From_End()
                case 6 :
                    print("Thank you ")
                    break 
                case _ :
                    print("Invalid Choice ")
Menu().run()


