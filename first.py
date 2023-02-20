class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return "Prvek vlozen"
        
        current_node = self.root
        while True:
            if val < current_node.val:
                if not current_node.left:
                    current_node.left = Node(val)
                    return "Prvek vlozen"
                current_node = current_node.left
            elif val > current_node.val:
                if not current_node.right:
                    current_node.right = Node(val)
                    return "Prvek vlozen"
                current_node = current_node.right
            else:
                return "Prvek uz ve strome byl"

    def delete(self, val):
        if not self.root:
            return "Prvek ve strome nebyl"

        # find the node to be deleted
        current_node = self.root
        parent_node = None
        while current_node and current_node.val != val:
            parent_node = current_node
            if val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if not current_node:
            return "Prvek ve strome nebyl"

        # case 1: the node to be deleted has no children
        if not current_node.left and not current_node.right:
            if not parent_node:
                self.root = None
            elif parent_node.left == current_node:
                parent_node.left = None
            else:
                parent_node.right = None
        
        # case 2: the node to be deleted has only one child
        elif not current_node.left or not current_node.right:
            if not current_node.left:
                child = current_node.right
            else:
                child = current_node.left
            if not parent_node:
                self.root = child
            elif parent_node.left == current_node:
                parent_node.left = child
            else:
                parent_node.right = child
        
        # case 3: the node to be deleted has two children
        else:
            # find the in-order successor (smallest value in the right subtree)
            successor_parent = current_node
            successor = current_node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # replace the value of the node to be deleted with the value of the successor
            current_node.val = successor.val

            # delete the in-order successor
            if successor_parent.left == successor:
                successor_parent.left = None
            else:
                successor_parent.right = None

        return "Prvek vypusten"
    def print_tree(self, node=None, level=0):
        if not node:
            node = self.root
        if node.left:
            self.print_tree(node.left, level + 1)
        print("  " * level + str(node.val))
        if node.right:
            self.print_tree(node.right, level + 1)

def read_commands(bst):
    with open("VSTUP.TXT", "r") as f:
        for line in f:
            command, *args = line.strip().split()
            print(line.strip())
            if command == "P":
                bst.print_tree()
            elif command == "I":
                val = int(args[0])
                print(bst.insert(val))
            elif command == "D":
                val = int(args[0])
                print(bst.delete(val))

bst = BST()