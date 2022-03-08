#模拟文件系统

class Node:
    def __init__(self,name,type="dir"):
        self.name=name
        self.type=type
        self.children=[]
        self.parent=None
    def __repr__(self):
        return self.name

class FileSystem:
    def __init__(self):
        self.root=Node("/")
        self.now=self.root

    def mkdir(self,name):
        #name要以 / 结尾
        if name[-1] != '/':
            name+='/'
        node=Node(name)
        self.now.children.append(node)
        node.parent=self.now

    def ls(self):
        return self.now.children

    def cd(self,name):
        if name[-1] != '/':
            name+='/'
        if name == "../":
            self.now=self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now=child
                return
        raise ValueError("Invalid dir!")


tree=FileSystem()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")

tree.cd("bin/")
tree.mkdir("python/")
tree.cd("../")

print(tree.ls())

