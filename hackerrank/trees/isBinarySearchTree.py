import sys

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check(node, min, max):
    if not node:
        return True
    if node.data <= min or node.data >= max:
        return False
    return check(node.left, min, node.data) and check(node.right, node.data, max)

def checkBST(root):
    return check(root, -1 * sys.maxsize, sys.maxsize)