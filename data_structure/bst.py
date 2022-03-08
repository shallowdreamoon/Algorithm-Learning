class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None

class BST:
    def __init__(self,li=None):
        self.root=None
        if li:
            for l in li:
                self.insert_no_rec(l)


    def insert(self,node,val):
        #表示当前书为空地情况
        if not node:
            node=BiTreeNode(val)
        elif val<node.data:
            node.lchild=self.insert(node.lchid,val)
            node.lchild.parent=node
        elif val>node.data:
            node.rchild=self.insert(node.rchild,val)
            node.rchild.parent=node
        return node

    #插入的非递归实现
    def insert_no_rec(self,val):
        p=self.root
        #当前树为空
        if not p:
            self.root=BiTreeNode(val)
            return
        while True:
            if val<p.data:
                #表示左子树存在
                if p.lchild:
                    p=p.lchild
                else:                #表示左子树不存在
                    p.lchild=BiTreeNode(val)
                    p.lchild.parent=p
                    return
            if val>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=BiTreeNode(val)
                    p.rchild.parent=p
                    return
            #如果插入的值和根节点值相等，不做操作
            else:
                return
    #查找实现
    def query(self,node,val):
        if not node:
            return None
        if val<node.data:
            return self.query(node.lchild,val)
        if val>node.data:
            return self.query(node.rchild,val)
        else:
            return node
    #查找的非递归实现
    def query_no_rec(self,val):
        p=self.root
        while p:
            if val<p.data:
                p=p.lchild
            if val>p.data:
                p=p.rchild
            else:
                return p
        else:
            return None



    def pre_order(self,root):
        if root:
            print(root.data,end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data,end=',')
            self.in_order(root.rchild)

    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data,end=',')

tree=BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print()
print(tree.query(tree.root,5).data)