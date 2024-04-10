# -*- coding: UTF-8 -*- 
import copy

class Jsontree(object):
    def __init__(self, nodes, root):
        self.nodes = nodes
        self.root = root


class Node(object):

    def __init__(self, id, label, value, father, children, depth, weight=0):
        self.father = father
        self.children = children
        self.depth = depth
        self.weight = weight
        self.label = label
        self.id = id
        self.value = value
    

def json2tree(j, root):
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
            f.children = json2tree(f.value, f).children
        else:
            f.children = []

    return root

def json2kuohaoinner(aroot):
    # {a{b}{c}}
    # a
    # b c
    childrenstr = ""
    for children in aroot.children:
        if not children.children:
            childrenstr += "{" + children.label + "}"
        else:
            childrenstr += "{" + children.label + json2kuohaoinner(children) + "}"
    return childrenstr

def json2kuohao(aroot):
    return "{" + json2kuohaoinner(aroot) + "}"

if __name__ == '__main__':
    # f = json2tree({"test": {"ch": 1, "ch2": {"ch21": 21}}}, None)


    # print(f.children[0].children[1].children[0].id)

    a = {"1": {"2": 2, "3": {"4": 4, "5": 0}}}
    # a = {"1": 1}
    # {1{2}{3}}
    aroot = json2tree(a, None)
    # print(aroot.children[0].children)
    print(json2kuohao(aroot))
    