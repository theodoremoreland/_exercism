class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        self.count = 0

        for data in tree_data:
            self.insert(data)


    def insert(self, value):
        new_node = TreeNode(value)
        new_value = new_node.data

        if self.root == None:
            self.root = new_node
            return None

        def searchTree(current_node):
            current_value = current_node.data

            if new_value <= current_value:
                if not current_node.left:
                    current_node.left = new_node
                else:
                    return searchTree(current_node.left)
            else:
                if not current_node.right:
                    current_node.right = new_node
                else:
                    return searchTree(current_node.right)

        searchTree(self.root)
            

    def data(self):
        return self.root


    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left) 
            print(root.data)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


    def sorted_data(self):
        return self.inorderTraversal(self.root)