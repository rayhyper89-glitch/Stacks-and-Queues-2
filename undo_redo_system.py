# undo_redo.py
from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        return None if self.top is None else self.top.value

    def print_stack(self):
        current = self.top
        if current is None:
            print("Stack is empty.")
            return
        while current:
            print(current.value)
            current = current.next


def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo stack
            print(f"Action performed: {action}")
        elif choice == "2":
            action = undo_stack.pop()
            if action:
                redo_stack.push(action)
                print(f"Action undone: {action}")
            else:
                print("No actions to undo.")
        elif choice == "3":
            action = redo_stack.pop()
            if action:
                undo_stack.push(action)
                print(f"Action redone: {action}")
            else:
                print("No actions to redo.")
        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack()
        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack()
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_undo_redo()
        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()
