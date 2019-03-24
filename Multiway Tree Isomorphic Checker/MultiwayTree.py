#  File: MultiwayTree.py
#  Description: Determines if trees have the same shape
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E
#  Unique Number: 51470
#
#  Date Created: 12/7/2017
#  Date Last Modified: 12/8/2017

# creates class for Multiway Tree
class MultiwayTree:

    def __init__(self,pyTree):

        # base case
        if pyTree == []:
            return None

        else:

            # gives the root data
            self.data = pyTree[0]

            # gives the children of the root
            self.children = pyTree[1]
            self.childrenObjects = []

            # creates objects from the children and puts them in a list
            for i in self.children:

                obj = MultiwayTree(i)
                self.childrenObjects.append(obj)


    def preOrder(self):
        # print out the node-and-pointer representation of a tree using preorder.

        s = ""
        if self != []:
            root = self.data
            s += str(root) + "  "

            for i in self.childrenObjects:
                s += i.preOrder()
        return s


    def isIsomorphicTo(self,other):
        # return True if the tree "self" has the same structure as the
        # tree "other", "False" otherwise.

        if len(self.childrenObjects) == len(other.childrenObjects):

            # goes through list of children objects
            for i in range(len(self.childrenObjects)):

                if self.childrenObjects[i].isIsomorphicTo(other.childrenObjects[i]) == False:

                    return False

            return True

        else:
            return False


def main():

    # opens file for reading
    inputFile = open("MultiwayTreeInput.txt","r")

    count = 1
    for line in inputFile:

        # reads in two lines at a time and makes a pair of trees
        line = line.strip()
        line2 = inputFile.readline().strip()

        tree1 = MultiwayTree(eval(line))
        tree2 = MultiwayTree(eval(line2))

        # first tree data
        print("Tree " + str(count) + ":  " + str(line))
        """
        print("\nThese are the children:")
        for i in range(len(tree1.childrenObjects)):
            print(tree1.childrenObjects[i].data)
        """

        print("Tree " + str(count) + " preorder:   " + str(tree1.preOrder()))
        print()

        # second tree data
        print("Tree " + str(count + 1) + ":  " + str(line2))

        """
        print("\nThese are the children:")
        for i in range(len(tree2.childrenObjects)):
            print(tree2.childrenObjects[i].data)
        """

        print("Tree " + str(count + 1) + " preorder:   " + str(tree2.preOrder()))
        print()

        # prints if trees are isomorphic or not
        if tree1.isIsomorphicTo(tree2) == True:
            print("Tree " + str(count) + " is isomorphic to Tree " + str(count + 1))

        else:
            print("Tree " + str(count) + " is not isomorphic to Tree " + str(count + 1))

        print()
        print()

        count += 2

main()
