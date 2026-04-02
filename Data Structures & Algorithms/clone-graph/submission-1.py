"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        key_dict = {}

        def clone_node(n):
            if n in key_dict:
                return key_dict[n]

            copy = Node(n.val)
            key_dict[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(clone_node(nei))

            return copy

        return clone_node(node)
        