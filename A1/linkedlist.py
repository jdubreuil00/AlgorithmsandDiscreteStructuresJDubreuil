"""
Module 01 Programming Assignment 01
Jordan Dubreuil
5/15/2023
This Program uses the Linked List Example from class as a base. 
At first I tried modifying the LinkedList Class to add methods
for the functionality desired from the assignment. I dediced to 
program these features in the main function instead to change the class
as little as possible.

The Program reads the file numbers.txt a list of Integers
into a list and then using a for loop feeds the list into
the Linked List. Once the Linked List is created the user is
prompted to input an integer. After the integer is validated
we iterate through the linked list and look for matching integers.
If a matching integer is found it is removed. If there is not a match 
list values are then check to see if the integer is outside of the current range 
of integers in the list or if it is withing the range of current values
and then appropriately adds the integer to the corect order in the list.

Output displays the correct order of the list.
"""
import os


class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None


class LinkedList:
    def __init__(self, d=None):
        if (d == None):  # an empty list
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header

    def nextCurrent(self):
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header

    def resetCurrent(self):
        self.Current = self.Header

    def getCurrent(self):
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None

    def insertBeginning(self, d):
        if (self.Header is None):  # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp

    def insertCurrentNext(self, d):
        if (self.Header is None):  # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp

    def removeBeginning(self):
        if (self.Header is None):  # if list is empty
            return None
        else:                     # if list not empty
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans

    def removeCurrentNext(self):
        if (self.Current.Next is None):  # if there is no node
            return None  # after Current
        else:                           # if there is
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans

    def insertSort(self, data):
        newNode = Node(data)
        if self.Header == None or data < self.Header.Data:
            newNode.Next = self.Header
            self.Header = newNode
        else:
            self.Current = self.Header
            print(self.Current.Next, data, self.Header.Data, self.Current.Data)
            while self.Current.Next and data > self.Current.Data:
                self.Current = self.Current.Next

            newNode.Next = self.Current.Next
            self.Current.next = newNode

    def printList(self, msg="====="):
        p = self.Header
        print("====", msg)
        while (p is not None):
            print(p.Data, end=" ")
            p = p.Next
        if (self.Current is not None):
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")
        input("Press Enter (Return) to continue")

    def search(self, data):
        if self.Header is None:
            return "Empty list"

        current = self.Header
        while current is not None:
            if current.Data == data:
                # current = self.removeCurrentNext()
                return True
            else:
                print(current.Data)
                current = current.Next

        return False

    def size(self):
        size = 0
        if self.Header is None:
           return size
        current = self.Header

        while current is not None:
            size += 1
            current = current.Next
        return size


def main():
    # Loads the text file of numbers
    file = open("A1/numbers.txt", "r")
    # Reads the contents of the file to a variable.
    content = file.read()
    # Creates a list to store the numbers.
    a = []
    # Splits the numbers from the file by linebreak.
    linestripped = content.split("\n")
    # List comprehension that strips all whitespace.
    a = [int(line.strip()) for line in linestripped if line.strip()]
    # Sorts the list of numbers using the sort method.
    a.sort()

    # Creates the Linked List using the file provided from class.
    L = LinkedList()
    # Uses a for loop to add the items from the list to the Linked List
    for i in range(len(a)):
        L.insertCurrentNext(a[i])
        L.nextCurrent()

    # Resets the current item in list to the beginning
    L.resetCurrent()
    # Prints the Linked list Items
    L.printList()

    # Asks for a valid integer
    while True:
        try:
            # Asks for a valid integer
            x = int(input("Please enter an integer value..."))
        except ValueError:
            # Validate input
            print('Sorry please try a valid integer...')
            continue
        else:
            # Exits the while loop because input is valid.
            break

    # Sets the header of the linked list as the current value locally
    current = L.Header
    # Stores a previous value to check the pointer for beginging or end of list.
    prev = None

    while current:
        # Commented this out for brevity.
        # print(current.Data)
        # Checks if input value matches the current data for list removal.
        if current.Data == x:
            if prev is None:
                # If the node to remove is the header node, update the header
                L.Header = current.Next
            else:
                # If the node to remove is not the header node, update the previous node's next pointer
                prev.Next = current.Next
            break
        # Checks to see if value needs to be inserted at begining of list.
        elif x < L.Header.Data:
            newNode = Node(x)
            newNode.Next = current
            L.Header = newNode
            break
        # Checks to see if velue needs to be inserted at end of list.
        elif current.Next == None:
            newNode = Node(x)
            current.Next = newNode
            break
        # Checks to see if value exisits and needs to be inserted at a certain position in the list.
        elif current.Data < x and current.Next and current.Next.Data > x:
            newNode = Node(x)
            newNode.Next = current.Next
            current.Next = newNode
            break
        # Used to continue iterating through the list until a condition is found.
        prev = current
        current = current.Next
    # Prints the final sorted list
    L.printList("Press enter or return to see sorted linked list")


# Calls the main fucntion
if __name__ == "__main__":
    main()
