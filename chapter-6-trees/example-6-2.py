#!/usr/bin/python

def reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None

    if len(preorder) == len(inorder) == 1:
        return preorder[0]

    root = preorder[0]
    root_i = inorder.index(root)
    root.left = reconstruct(preorder[1:1 + root_i], inorder[0:root_i])
    root.right = reconstruct(preorder[1 + root_i:], inorder[root_i + 1:])

    return root

