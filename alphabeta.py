import os

class Node(object):
    def __init__(self, data, minMax):
        self.data = data
        self.children = []
        self.maxMin = minMax
        self.isLeaf = False
        self.isRoot = False

    def addChild(self, obj):
        self.children.append(obj)

def isNum(s): # function used when checking if the child value of an edge is a regualr node or leaf node
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    cwd = os.getcwd().replace('\\', '/') # gets the current working directory of this python file

    f1 = open(cwd + "/alphabeta.txt", mode='r')

    treeData = [line.rstrip('\n') for line in f1] # each index of treeData contains the 2 sets needed for that treeData

    for tree in treeData:
        nodeList = []

        tree = tree.replace('{', '')
        tree = tree.replace(')}', ' ')
        tree = tree.replace('(', '')
        tree = tree.split() # splits into node and tree lists

        nodes = tree[0].split('),') # splits the indiviual nodes and edges
        edges = tree[1].split('),')

        for node in nodes:
            node = node.split(',') # splits each individual node into data and minMax values
            newNode = Node(node[0], node[1])
            nodeList.append(newNode)

        nodeList[0].isRoot = True # the first node in this list will always be the root, I think

        for edge in edges:
            edge = edge.split(',') # splits each individual edge into parent and child
            parent = edge[0]
            child = edge[1]

            for node in nodeList: # finding the parent node of this edge in our pre-existing list of nodes
                if node.data == parent:
                    parentNode = node
                    break

            if isNum(child): # if the child of the edge is a number, then it will be a leaf
                newNode = Node(child, None) # create a new node for the leaf
                newNode.isLeaf = True # specify that it is a leaf
                parentNode.addChild(newNode) # this should add itself to the children list of its parent node


            else: # if the child is a node rather than a number (i.e. it is not a leaf)
                for node in nodeList:
                    if node.data == child:
                        childNode = node # find which pre-existing node is the child of this edge
                        parentNode.addChild(childNode) # create the edge
                        break # break out of this for loop because we already created the edge

        # this prints the tree in the form "root, child, child, ..., child" each on a new line. followed by a line break before the next node
        # for node in nodeList:
        #     print(node.data)
        #     for child in node.children:
        #         print(child.data)
        #     print()

if __name__ == "__main__":
    main()
