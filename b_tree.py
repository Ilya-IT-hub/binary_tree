class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def build_binary_tree(sequence):
    root = None
    for num in sequence:
        root = insert_node(root, num)
    return root

def find_min_max_leaves(root):
    if root is None:
        return None, None
    if root.left is None and root.right is None:
        return root.value, root.value

    left_min, left_max = find_min_max_leaves(root.left)
    right_min, right_max = find_min_max_leaves(root.right)

    min_leaf = min(left_min, right_min) if left_min is not None and right_min is not None else left_min or right_min
    max_leaf = max(left_max, right_max) if left_max is not None and right_max is not None else left_max or right_max

    return min_leaf, max_leaf


sequence = [17, 6, 8, 20, 13, 11, 4, 7, 19, 100, 1, 27, 5]
root = build_binary_tree(sequence)
min_leaf, max_leaf = find_min_max_leaves(root)

print("Минимальный лист:", min_leaf)
print("Максимальный лист:", max_leaf)