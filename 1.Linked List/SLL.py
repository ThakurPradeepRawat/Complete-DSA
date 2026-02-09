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
        data = int(input("Enter data: "))

        if pos < 1 or pos > self.length + 1:
            print("Invalid position")
            return

        if pos == 1:
            self.head = Node(data)
            return
        new_node = Node(data)
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
7. Exit
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
                    print("Thank you!")
                    break
                case _:
                    print("Invalid choice")



Menu().run()


    
    
