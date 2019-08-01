#!/usr/bin/python

def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
    if root is None:
        return True

    if root.value == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)

    return False

def count_unival_subtrees(root):
    if root is None:
        return 0

    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)

    return 1 + left + right if is_unival(root) else left + right

