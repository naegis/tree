class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None
count = 0


def insert(root, value):
    global count
    new_node = Node(value)
    if root is None:
        new_node.left = new_node.right = None
        root = new_node
        count += 1
    else:
        if count % 2 != 0:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

#infix
def display_infix(root):
    if root:
        display_infix(root.left)
        print(root.data, end="\t")
        display_infix(root.right)

#prefix
def display_prefix(root):
    if root:
        print(root.data, end="\t")
        display_prefix(root.left)
        display_prefix(root.right)

#postfix
def display_postfix(root):
    if root:
        display_postfix(root.left)
        display_postfix(root.right)
        print(root.data, end="\t")

if __name__ == "__main__":
    while True:
        print("\n----- Binary Tree -----\n")
        print("***** MENU *****")
        print("1. Insert\n2. Display\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter the value to be insert: "))
            root = insert(root, value)
        elif choice == 2:
            print("Prefix: ")
            display_prefix(root)
            print("\nInfix: ")
            display_infix(root)
            print("\nPostfix: ")
            display_postfix(root)
        elif choice == 3:
            break
        else:
            print("Please select correct operations!!!")