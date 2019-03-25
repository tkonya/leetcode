import math

def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    depth = find_depth(root)
    width = 2 ** (depth - 1)
    print('depth: ' + str(depth) + ', width: ' + str(width))
    last_row_element = find_last_row_element(root, depth, width)
    print('last row element: ' + str(last_row_element))
    elements_except_last_row = 2 ** (depth - 1) - 1
    print('element except last row: ' + str(elements_except_last_row))
    return elements_except_last_row + last_row_element


def find_depth(root):
    if root is None:
        return 0
    elif root.left is None:
        return 1
    else:
        return 1 + find_depth(root.left)


def is_node_at(root, depth, width, target):
    if depth == 1:
        if target == 0 and root.left is not None:
            return True
        elif target == 1 and root.right is not None:
            return True
        else:
            return False
    else:
        if target < (width / 2):
            if root.left is not None:
                return is_node_at(root.left, depth - 1, (width / 2), target)
            else:
                return False
        elif target <= (width / 2):
            if root.right is not None:
                return is_node_at(root.right, depth - 1, (width / 2), target - (width / 2))
            else:
                return False


def find_last_row_element(root, depth, width):
    target = width / 2
    interval = width / 4
    left_most_empty = width
    right_most_full = 0

    while True:

        if is_node_at(root, depth, width, target):
            print('right_most_full full: ' + str(right_most_full))
            right_most_full = target
            target += target + interval
        else:
            print('left_most_empty empty: ' + str(left_most_empty))
            left_most_empty = target
            target -= interval
        interval /= 2

        if right_most_full + 1 == left_most_empty:
            return right_most_full


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_complete_tree(size):
    if size == 0:
        return None
    elif size == 1:
        return TreeNode(size)
    elif size > 1:
        x = TreeNode(size)
        x.left = create_complete_tree(math.ceil((size - 1) / 2))
        x.right = create_complete_tree(size - math.ceil((size - 1) / 2))
        return x

