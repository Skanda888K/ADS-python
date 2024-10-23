#treenode
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def add_node(self,root,value):
        if not self.root:
            self.root=Node(value)
        else:
            if value<root.value:
                if root.left is None:
                    root.left=Node(value)
                else:
                    self.add_node(root.left,value)
            else:
                if root.right is None:
                    root.right=Node(value)
                else:
                    self.add_node(root.right,value)
     



t1=tree()
t1.add_node(t1.root,'j')
t1.add_node(t1.root,'b')
t1.add_node(t1.root,'w')
t1.add_node(t1.root,'a')
t1.add_node(t1.root,'c')
t1.add_node(t1.root,'c')

def pre_order(root):
    if not root:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    if not root:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.value)
print("pre")
pre_order(t1.root)
print("post")
post_order(t1.root)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)

print("in")
in_order(t1.root)

