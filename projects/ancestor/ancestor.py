class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:            
            self.graph[node] = set()
    
    def add_edge(self, node1, node2):
        self.graph[node1].add(node2)
        
    def get_neighbor(self, node):
        return self.graph[node]
    
    def size(self):
        return len(self.graph)
    
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def build_graph(ancestors):
    gg = Graph()
    for parent, child in ancestors:
        #add nodes
        gg.add_node(parent)
        gg.add_node(child)
        #connect the nodes to the child
        gg.add_edge(child, parent)
    return gg


# 3 choose your fighter - DFT

def earliest_ancestor(ancestors, starting_node):
    gg = build_graph(ancestors)
    
    ss = Stack()    
    visited = set()
    
    ss.push([starting_node])
    
    max_path_len = 1
    earliest_anc = -1
    
    while ss.size() > 0:
        current_path = ss.pop()
        current_node = current_path[-1]
        
        if len(current_path) > max_path_len or (len(current_path) == max_path_len and current_node < earliest_anc):
            max_path_len = len(current_path)
            earliest_anc = current_node
        
        if current_node not in visited:
            visited.add(current_node)
            
            parents = gg.get_neighbor(current_node)
            
            for parent in parents:
                parent_copy = current_path + [parent]
                ss.push(parent_copy)
    return earliest_anc