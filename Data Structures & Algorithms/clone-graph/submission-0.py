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
            key_dict[n] = Node(n.val)
            key_dict[n].neighbors = [] # 這行不需要(題目預設=[])
            for next_n in n.neighbors:
                
                if next_n not in key_dict:
                    clone_node(next_n)
                    # 第一次寫的錯誤:
                    # key_dict[n].neighbors.append(next_n)
                    key_dict[n].neighbors.append(key_dict[next_n])
                else:
                    # 第一次寫的錯誤:
                    # key_dict[n].neighbors.append(next_n)
                    key_dict[n].neighbors.append(key_dict[next_n])
        
        clone_node(node)
        return key_dict[node] 




        