import os

touches = 0

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

def generateTree(tree):
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

    return nodeList


def alpha_beta(current_node, alpha, beta): #, nodes_left):

        if (current_node.isRoot):
            alpha = float((-1) - (2**63))
            beta = float((-1) + (2**63))
        if (current_node.isLeaf):      #if current node is leaf node:
            global touches
            touches +=1 
            return int(current_node.data)       #return static evaluation of current node
        if current_node.maxMin == 'MAX':
            for child in current_node.children:
                alpha = max(alpha, alpha_beta(child, alpha, beta)) #compare children values
                if alpha >= beta:
                    return alpha
            return alpha
        if current_node.maxMin == 'MIN':
            for child in current_node.children:
                beta = min(beta, alpha_beta(child, alpha, beta))    #compsare children values
                if alpha >= beta:
                    return beta
            return beta


def printScore(graph, score):
    f = open("alpha_beta_out.txt", mode='a+')
    string = "Graph: %d, Score: %d, Nodes visited: %d \n" %(graph, score, touches)
    f.write(string)
    

def main():
    cwd = os.getcwd().replace('\\', '/') # gets the current working directory of this python file

    f1 = open(cwd + "/alphabeta.txt", mode='r')

    treeData = [line.rstrip('\n') for line in f1] # each index of treeData contains the 2 sets needed for that treeData
    graph = 0
    for tree in treeData:
        global touches
        touches = 0
        nodeList = generateTree(tree)
        graph += 1
        score = alpha_beta(nodeList[0], 0, 0)
        printScore(graph, score)



        # this prints the tree in the form "root, child, child, ..., child" each on a new line. followed by a line break before the next node
        # for node in nodeList:
        #     print(node.data)
        #     for child in node.children:
        #         print(child.data)
        #     print()

if __name__ == "__main__":
    main()
