from collections import deque
from audio import Notes
from termcolor import colored
# Available termcolor colors:
# text colors: black, red, green, yellow, blue, magenta, cyan, white,
# highlight colors: on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white

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
            print(colored("Tree is empty.", "red"))
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
            print(colored(linestr, "green"))
            print(colored(pstr, "green"))

    def assign_notes(self):
        """
        Assign notes to each layer of the tree. Nodes in the same layer get the same note.
        Layer 0: C6, Layer 1: B6, Layer 2: A6, etc.
        """
        if not self.root:
            print(colored("Tree is empty. Cannot assign notes.", "red"))
            return

        # Notes to assign, starting from C6 and descending
        note_sequence = [
            Notes.C6, Notes.B6, Notes.A6, Notes.G6, Notes.F6,
            Notes.E6, Notes.D6, Notes.C5, Notes.B5, Notes.A5
        ]

        # Breadth-first traversal using a queue
        queue = deque([(self.root, 0)])  # (node, layer)
        while queue:
            node, layer = queue.popleft()

            # Assign note based on the layer, wrap around if layer exceeds note_sequence length
            node.note = note_sequence[layer % len(note_sequence)]

            # Add children to the queue if they exist
            if node.left:
                queue.append((node.left, layer + 1))
            if node.right:
                queue.append((node.right, layer + 1))


    def print_notes(self, node=None):
        """Print value + note for every node (in-order)."""
        # If called with no arg, start at root.
        if node is None:
            node = self.root
            # If the tree is empty, stop now.
            if node is None:
                return

        # Now this is the recursive part where node is guaranteed not None
        if node.left:
            self.print_notes(node.left)

        note_name = getattr(node.note, "name", None) or "None"
        print(f"Node Value: {node.value}, Note: {note_name}")

        if node.right:
            self.print_notes(node.right)



    def delete():
        pass

    def preorder_traversal():
        pass

    def inorder_traversal():
        pass

    def postorder_traversal():
        pass