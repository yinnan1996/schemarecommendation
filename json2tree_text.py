# -*- coding: UTF-8 -*- 
class Node(object):

    def __init__(self, id, label, value, father, children, depth, weight=0):
        self.father = father
        self.children = children
        self.depth = depth
        self.weight = weight
        self.label = label
        self.id = id
        self.value = value
    
def json2tree(j):
    """
    Convert a JSON object into a tree structure.

    This function recursively constructs a tree from a JSON object. Each node in the tree represents
    a key-value pair in the JSON object. The tree is represented using a custom Node class, where each node
    contains a reference to its parent and its children.

    Args:
        j (dict): The JSON object to be converted into a tree.

    Returns:
        Node: The root node of the tree representing the JSON object.
    """
    def json2tree_inner(j, root):
        if root is None:
            root = Node(0, "root", j, None, [], 0, 0)
        nodes = []
        id = root.id + 1
        for k in j.keys():
            node = Node(id, k, j[k], root, [], root.depth+1, 0)
            id += 1
            nodes.append(node)

        root.children = nodes
        for f in nodes:
            if f.value is None:
                f.children = None
                continue
            if isinstance(f.value, dict):
                f.children = json2tree_inner(f.value, f).children
            else:
                f.children = []
        return root
    return json2tree_inner(j, None)

def tree2text(root):
    """
    Convert a tree structure back into a text representation.

    Args:
        root (Node): The root node of the tree to be converted.

    Returns:
        str: A string representation of the tree in the format of a JSON-like structure.
    """
    def tree2text_inner(root):
        children_str = ""
        for children in root.children:
            if not children.children:
                children_str += "{" + children.label + "}"
            else:
                children_str += "{" + children.label + tree2text_inner(children) + "}"
        return children_str
    return "{" + tree2text_inner(root) + "}"

if __name__ == '__main__':
    a = {"1": {"2": 2, "3": {"4": 4, "5": 0}}}
    print(tree2text(json2tree(a)))
    