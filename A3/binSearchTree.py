class Node:
    def __init__(self, d):
        self.Data, self.Left, self.Right = d, None, None

class Tree:
    def __init__(self, d=None):
        if (d == None): # an empty tree
            self.Root = None
        else:
            self.Root = Node(d)
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d):   # if no node left insert here
                if (n.Left == None):
                    n.Left = Node(d)
                else:          # or try left child
                    __insertHere__(n.Left, d)
            elif (n.Data < d): # if no node right insert here
                if (n.Right == None):
                    n.Right = Node(d)
                else:          # or try right child
                    __insertHere__(n.Right, d)
        if (self.Root == None): # it was an empty tree
            self.Root = Node(d)
        else:
            if (self.Root.Data > d):          # try left child
                if (self.Root.Left == None):  # if empty insert here
                    self.Root.Left = Node(d)
                else:                         # try left subtree
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d):        # try right child
                if (self.Root.Right == None): # if empty insert here
                    self.Root.Right = Node(d)
                else:                         # try right subtree
                    __insertHere__(self.Root.Right, d)
    def check(self, d):
        def __check__(n, d):
            if (n == None):
                return False
            elif (n.Data == d):
                return True
            elif (n.Data > d):
                return __check__(n.Left, d)
            elif (n.Data < d):
                return __check__(n.Right, d)
        return __check__(self.Root, d)
    def printInorder(self):
        def __visit__(n):
            if (n != None):
                __visit__(n.Left)
                print(n.Data, end=" ")
                __visit__(n.Right)
        print("\n--------")
        __visit__(self.Root)
        print("\n--------")
    def printPreorder(self):
        def __visit__(n, h):
            if (n != None):
                print("---"*h, n.Data)
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")
    def printPostorder(self):
        def __visit__(n, h):
            if (n != None):
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
                print("---"*h, n.Data)
        print("==========")
        __visit__(self.Root, 1)
        print("==========")
        
    def adjacencymatrix(self):
        
        def getHeight(n, h):
            
            # if (n != None):
            #     # print("---"*h, n.Data)
            #     print(h)
            #     getHeight(n.Left, h+1)
            #     getHeight(n.Right, h+1)
            if n is None:
                return 0
            return max(getHeight(n.Left, h+1),getHeight(n.Right, h+1))+1 
        
        def countNodes(n):
            if n is None:
                return 0
            else:
                return 1 + countNodes(n.Left) + countNodes(n.Right)
        
        def preorderList(n):
            elements = []
            def __visit__(n, h):
                if (n != None):
                    elements.append(n.Data)
                    __visit__(n.Left, h+1)
                    __visit__(n.Right, h+1)
            __visit__(self.Root, 1)
            return elements

        print("^^^^^^^^^^")
        height = getHeight(self.Root, 0)
        numNodes = countNodes(self.Root)
        elementList = preorderList(self.Root)
        print(height)
        print(numNodes)
        print(elementList)
        print("^^^^^^^^^^")
        matrix = [[0] * (numNodes) for _ in range(numNodes)]
        def populateMatrix(n, height, position):
            # if n is not None:
            #     if n.Left is not None:
            #         matrix[height][position *2+1] = abs(n.Data - n.Left.Data)
            #     if n.Right is not None:
            #         matrix[height][position*2+2] = abs(n.Data - n.Right.Data)
            #     populateMatrix(n.Left, height + 1, position * 2)
            #     populateMatrix(n.Right, height + 1, position * 2 + 1)
            # if n.Data is equal to elementList data pos is 0
            # if element list is not equal to n.Left or n.Right pos is 0
            # if element list is equal to N.Left calculate the absolute value with n.Data
            # if element list is equal to N.Right calculate the absolute value with n.Data
            if n is not None:
                for node in elementList:
                    if node == n.Data:
                        matrix[height][position] = 0
                    if n.Left or n.Right is not None:
                        if n.Left is not None:
                            if node == n.Left.Data:
                                matrix[height][position] = abs(n.Data - n.Left.Data)
                        if n.Right is not None:
                            if node == n.Right.Data:
                                matrix[height][position] = abs(n.Data - n.Right.Data)
                    position += 1
                if n.Left is not None:
                    populateMatrix(n.Left, height + 1, 0)
                if n.Right is not None:
                    populateMatrix(n.Right, height + 1, 0)

        populateMatrix(self.Root, 0,0)

         # Print the adjacency matrix
        print('Adjacency Matrix')
        print('graph')
        for row in matrix:
            print(row)
            
        

def main():
    myTree = Tree()
    myTree.insert(21)
    myTree.insert(28)
    myTree.insert(14)
    myTree.insert(11)
    myTree.insert(18)
    myTree.insert(25)
    myTree.insert(32)
    myTree.insert(27)
    myTree.insert(12)
    myTree.insert(5)
    myTree.insert(15)
    myTree.insert(19)
    myTree.insert(23)
    myTree.insert(30)
    myTree.insert(37)
    myTree.printInorder()
    myTree.printPreorder()
    print("56 is in the tree:", myTree.check(56))
    print("17 is in the tree:", myTree.check(17))
    print("25 is in the tree:", myTree.check(25))
    print("15 is in the tree:", myTree.check(15))
    myTree.printPostorder()

# def adjacencymatrix(root):
#         def getheight(n):
#             if n is None:
#                 return 0
#             return max(getheight(n.Left),getheight(n.Right)) +1
#         height = getheight(root)
#         print(height)
        # Build Empty Matrix
        # Populate matrix with Absolute difference values

        

# main()
# Loads the text file of numbers
file = open("A3/numbers4.txt", "r")
# Reads the contents of the file to a variable.
content = file.read()
# Creates a list to store the numbers.
a = []
# Splits the numbers from the file by linebreak.
linestripped = content.split("\n")
# List comprehension that strips all whitespace.
a = [int(line.strip()) for line in linestripped if line.strip()]

myTree = Tree()
for item in a:
    myTree.insert(item)

# myTree.printInorder()
myTree.printPreorder()
# myTree.printPostorder()
myTree.adjacencymatrix()




