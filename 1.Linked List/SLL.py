class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        print("Inserted at beginning")

    def insert_at_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.length += 1
        print("Inserted at end")

    def insert_at_position(self):
        pos = int(input("Enter position: "))
        Data = int(input("Enter data: "))

        if pos < 1 or pos > self.length + 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node = Node(Data)
            new_node.next = self.head 
            self.head = new_node
            return
        new_node = Node(Data)
        current = self.head
        for _ in range(pos - 2):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        print(f"Inserted at position {pos}")

    def delete_from_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next
        self.length -= 1
        print("Deleted from beginning")

    def delete_from_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

        self.length -= 1
        print("Deleted from end")
    
    def delete_from_position(self):
        pos = int(input("Enter Position:- "))
        if pos<1 or pos > self.length:
            print("Position is not valid")
        elif (pos ==1):
            self.head = self.head.next
        else:
            current = self.head 
            for _ in range(pos-2):
                current = current.next 
            current.next = current.next.next
        print(f"Delete from {pos} position")
        self.length-=1
     
    def Check_element_present(self):
        Data = int(input("Enter Data :- "))
        if(self.length==0):
            print("Linked List is empty") 
            return 
        current = self.head 
        while(current!=None):
            if current.data == Data :
                print(f"{Data} is present in Linked List")
                return
            current = current.next 
        print(f"{Data} is not present in Linked List")

    def Reverse_Linked_List(self):
        if self.head == None :
            print("Linked List is Empty")
            return  
        curr = self.head 
        prev = None
        next = None 
        while(curr!=None):
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        self.head = prev
        print("Reverse Linked List :- ")
        self.traverse()

    #  LeetCode Problem Number 876 
    def MiddleOfTheLinkedList(self):
        between = self.length//2 + 1
        i = 1
        current = self.head 
        while(i!=between):
            current=current.next 
            i+=1
        print("Middle element  of the linked list is :- " , current.data)
     
class Menu:
    def run(self):
        ll = SinglyLinkedList()
        while True:
            print("\n" + "*" * 20 + " MENU " + "*" * 20)
            print("""
1. Insert at Beginning
2. Insert at End
3. Insert at Position
4. Traverse
5. Delete from Beginning
6. Delete from End
7. Delete from Position
8. Check this element present or not 
9. Reverse Linked list
10.Middle  Element Of the Linked list 
11. Exit
""")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    ll.insert_at_beginning()
                case 2:
                    ll.insert_at_end()
                case 3:
                    ll.insert_at_position()
                case 4:
                    ll.traverse()
                case 5:
                    ll.delete_from_beginning()
                case 6:
                    ll.delete_from_end()
                case 7:
                    ll.delete_from_position()
                case 8:
                    ll.Check_element_present()
                case 9:
                    ll.Reverse_Linked_List()
                case 10:
                    ll.MiddleOfTheLinkedList()
                case 11:
                    print("Thank You ")
                    break
                case _:
                    print("Invalid choice")

Menu().run()

    
    
