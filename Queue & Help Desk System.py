# help_desk_queue.py
from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        return None if self.front is None else self.front.value

    def print_queue(self):
        current = self.front
        if current is None:
            print("Queue is empty.")
            return
        while current:
            print(current.value)
            current = current.next


def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")
        elif choice == "2":
            name = queue.dequeue()
            if name:
                print(f"{name} has been helped.")
            else:
                print("No customers to help.")
        elif choice == "3":
            name = queue.peek()
            if name:
                print(f"Next customer: {name}")
            else:
                print("No customers waiting.")
        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()
        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()
if __name__ == "__main__":
    run_help_desk()
