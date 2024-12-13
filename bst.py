from collections import deque
from audio import Notes
from termcolor import colored

class BSTNode:
    def __init__(self, value, note):
        self.value = value
        self.note = note
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value, note):
        """
        Insert a new node into the BST.

        Args:
            value (int): value of the node
            note (Notes): musical note assigned to the node
        """
        new_node = BSTNode(value, note)

        # If there is no root, make this node the root
        if self.root is None:
            self.root = new_node
        else:
            # Recursive search to find correct insertion point
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def build_balanced_bst(self, sorted_array):
        """
        Returns:
            BSTNode: the root of the balanced BST
        """
        if not sorted_array:
            return None

        mid_index = len(sorted_array) // 2
        root = BSTNode(sorted_array[mid_index], Notes.C4)  # Will need to adjust note-assigning functionality

        root.left = self.build_balanced_bst(sorted_array[:mid_index])        # index 0 to mid
        root.right = self.build_balanced_bst(sorted_array[mid_index + 1:])   # index mid+1 to end

        return root
    
    def get_height(self, node):
        if node is None:
            return 0
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return max(left_height, right_height) + 1
    
    def print_bst(self):
        """
        Prints the tree using an ASCII representation with connecting branches,
        adapted from the following Stack Overflow comment: https://stackoverflow.com/a/72497198
        """
        if self.root is None:
            print("Tree is empty.")
            return

        # Adjust height by subtracting 1
        nlevels = self.get_height(self.root) - 1
        width = 2 ** (nlevels + 1)

        # Queue holds tuples of (node, level, x_position, alignment)
        q = [(self.root, 0, width, 'c')]
        levels = []

        while q:
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, x, align])
                seg = width // (2 ** (level + 1))
                q.append((node.left, level + 1, x - seg, 'l'))
                q.append((node.right, level + 1, x + seg, 'r'))

        # Print each level
        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (2 ** (i + 1))
            for n in l:
                valstr = str(n[0].value)
                if n[3] == 'r':
                    # Right child
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2]
                if n[3] == 'l':
                    # Left child
                    linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr
                pre = n[2]
            print(linestr)
            print(pstr)

    def delete():
        pass

    def preorder_traversal():
        pass

    def inorder_traversal():
        pass

    def postorder_traversal():
        pass