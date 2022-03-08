from Bili_Algorithm.数据结构.bst import BiTreeNode,BST

class AVLNode(BiTreeNode):
    def __init__(self,data):
        BiTreeNode.__init__(self,data)
        self.bf=0

class AVLTree(BST):
    def __init__(self,li=None):
        BST.__init__(self,li)

    def rotate_left(self,p,c):
        """
        :param p: 表示当前不再保持平衡的节点 
        :param c: 表示p的右孩子
        :return: 
        """
        s2=c.lchild
        p.rchild=s2
        if s2:
            s2.parent=p
        c.lchild=p
        p.parent=c
        #更新节点p和c的平衡因子
        p.bf=0
        c.bf=0

    def rotate_right(self,p,c):
        """
        :param p: 表示当前不再保持平衡的节点 
        :param c: 表示p的左孩子
        :return: 
        """
        s2=c.rchild
        p.lchild=s2
        if s2:
            s2.parent=p
        c.rchild=p
        p.parent=c

        p.bf=0
        c.bf=0


    def insert_no_rec(self,val):
        pass