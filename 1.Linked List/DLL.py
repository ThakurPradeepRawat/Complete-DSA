#Doubly Linked List

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self ):
        self.head = None 
        self.length = 0 
    def Traverse(self):
        current = self.head 
        while(current!=None):
            print(current.data , end="<==>")
            current=current.next 
        print("None")
    def Insert_At_Begin(self):
        Data  = int(input("Enter data :- "))
        newNode = Node(Data)
        if self.length == 0 :
            self.head = newNode  
            self.length+=1
            print("Data Inserted at begining")
            return
        newNode.next = self.head 
        self.head.prev = newNode 
        self.head = newNode
        self.length+=1
        print("Data inserted at begining ")
    def Insert_At_End(self):
        Data = int(input("Enter Data :- " ))
        newNode = Node(Data)
        current = self.head 
        if(self.head is None):
            self.head=newNode 
            self.length+=1
            print("Data inserted at end")
            return
        while(current.next!=None):
            current=current.next 
        newNode.prev = current 
        current.next = newNode 
        self.length+=1
        print("Data Inserted at end")
    def Delete_From_Begin(self):
        if(self.head is None):
            print("DLL is empty")
            return 
        self.head = self.head.next 
        self.head.prev = None 
        self.length-=1 
        print("Data delete from begining")
    def Delete_From_Last(self):
        if(self.head is None):
            print("DLL is Empty")
            return 
        if(self.length == 1):
            self.head = None 
            self.length-=1
            print("Data Deleted from end")
            return
        current = self.head 
        while(current.next.next !=None):
            current = current.next 
        current.next = None 
        self.length -=1
        print("Data Deleted from end")
        
class Menu:
    def run(self):
        Dll = DoublyLinkedList()
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

            match choice:
                case 1:
                    Dll.Insert_At_Begin()
                case 2:
                    Dll.Insert_At_End()
                case 3:
                    Dll.Traverse()
                case 4:
                    Dll.Delete_From_Begin()
                case 5:
                    Dll.Delete_From_Last()
                case 6:
                    print("Thank You ")
                    break
                case _:
                    print("Invalid choice")

Menu().run()

    