class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None
 
def isEqual(root1, root2):
        if root1 == None and root2 == None:
            return True
 
        if root1 == None and root2 != None:
            return False
 
        if root1 != None and root2 == None:
            return False
 
        if root1.data == root2.data:
            return isEqual(root1.lchild, root2.lchild) and isEqual(root1.rchild,root2.rchild)
        else:
            return False
 
def constructTree():
    root = BiTNode()
    node1 = BiTNode()
    node2 = BiTNode()
    node3 = BiTNode()
    node4 = BiTNode()
    root.data = 6
    root.lchild = node1
    root.rchild = node2
    node1.rchild = node3
    node1.lchild = node4
    node2.lchild = node2.rchild = node3.lchild = node3.rchild = node4.lchild = node4.rchild = None
    return root
 
if __name__ == "__main__":
    root1 =constructTree()
    root2 = constructTree()
    equal = isEqual(root1, root2)
    if equal:
        print("这两颗树相等")
    else:
        print("这两课树不相等")
