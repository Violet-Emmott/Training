class Node(object):
    children=[]
    def add_child(self, name):
        self.children.append(name)
    def __init__(self, name, *parents):
        self.name = name
        self.parents = parents
        for parent in parents:
            parent.add_child(self)
    def get_children(self):
        children=[]
        for child in self.children:
            children.append(child.name)
        return(children)
    def get_parents(self):
        parents=[]
        for parent in self.parents:
            parents.append(parent.name)
        return(parents)