class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side):
        if not self.root:
            print("Error: Tree is empty. Set root first.")
            return False

        parent = self._find(self.root, parent_name)
        if not parent:
            print(f"Error: Parent '{parent_name}' not found.")
            return False

        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(employee_name)
                return True
            else:
                print(f"Error: Left side of '{parent_name}' already filled.")
        elif side == "right":
            if parent.right is None:
                parent.right = DoctorNode(employee_name)
                return True
            else:
                print(f"Error: Right side of '{parent_name}' already filled.")
        else:
            print("Error: Side must be 'left' or 'right'.")
        return False

    def _find(self, node, name):
        if not node:
            return None
        if node.name == name:
            return node
        left = self._find(node.left, name)
        if left:
            return left
        return self._find(node.right, name)

    def preorder(self, node):
        if not node:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if not node:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    # Error Handling
    tree.insert("Dr. Smith", "Dr. Adams", "left")  # Parent not found
    tree.insert("Dr. Phan", "Dr. Blake", "middle")  # Invalid side
    tree.insert("Dr. Phan", "Dr. Brown", "left")    # Left side already filled

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
